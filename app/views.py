import datetime
from django.shortcuts import render
from common.Helper import ops_render, get_date_form_str, getFormatDate, get_current_date
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from .models import User, MajorClass, MajorFirst, MajorSecond, ProfessionalCertificationOrQualification, ThesisWorks, \
    NationalPatent, TechnologicalInnovation, SkillsCompetition, Honour, Professional, Edu, Mark, Enroll
from common.UserService import UserService


# Create your views here.
def index(request):
    return ops_render(request, "user/login.html")


def register(request):
    response = {'code': 200, 'msg': "注册成功", "data": {}}
    if request.method == "POST":
        request_json = request.POST
        username = request_json.get("login_name", "")
        password = request_json.get("login_pwd", "")
        if not username or len(username) < 4:
            response['code'] = 1
            response['msg'] = "请输入规范的用户名~"
            return JsonResponse(response)
        if not password or len(password) < 4:
            response['code'] = 2
            response['msg'] = "请输入规范的密码~"
            return JsonResponse(response)

        if len(User.objects.filter(username=username)) >= 1:
            response['code'] = 3
            response['msg'] = "用户名已存在，请重新输入~"
            return JsonResponse(response)

        salt = UserService.gene_salt()
        password = UserService.gene_pwd(password, salt)
        save_user = {"username": username, "password": password, "salt": salt}
        User.objects.create(**save_user)
        return JsonResponse(response)
    else:
        response['code'] = -1
        response['msg'] = "此接口不支持GET请求"
        return JsonResponse(response)


def login(request):
    response = {'code': 200, 'msg': "登陆成功～", "data": {}}
    if request.method == "POST":
        request_json = request.POST
        username = request_json.get("login_name", "")
        password = request_json.get("login_pwd", "")
        login_type = request_json.get("login_type", 1)
        if not username or len(username) < 4:
            response['code'] = 1
            response['msg'] = "请输入规范的用户名~"
            return JsonResponse(response)
        if not password or len(password) < 4:
            response['code'] = 2
            response['msg'] = "请输入规范的密码~"
            return JsonResponse(response)

        users = User.objects.filter(username=username, type=login_type)
        if users:
            user = users[0]
            salt = user.salt
            login_password = UserService.gene_pwd(password, salt)
            save_password = user.password
            if login_password == save_password:

                if user.status != 1:
                    response['code'] = 5
                    response['msg'] = "您的账号不能使用，请联系相关管理人员~"
                    return JsonResponse(response)

                i_data = {"path": "/resume"}
                if user.type == 2:
                    response['msg'] = "管理员登陆成功.."
                    i_data['path'] = "/cms"
                response["data"] = i_data
                json_response = JsonResponse(response)
                auth_code = UserService.gene_auth_code(user)
                json_response.set_cookie("jobs", auth_code)
                return json_response
            else:
                response['code'] = 4
                response['msg'] = "密码错误~"
                return JsonResponse(response)
        else:
            response['code'] = 3
            response['msg'] = "用户不存在~"
            return JsonResponse(response)

    else:
        response['code'] = -1
        response['msg'] = "此接口不支持GET请求"
        return JsonResponse(response)


def admin_users(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    admins = User.objects.filter(type=2)
    rep_admins = []
    for admin in admins:
        item = {"id": admin.id, "nickname": admin.nickname, "username": admin.username, "add_time": admin.add_time,
                "status": admin.status}
        rep_admins.append(item)
    rep = {"list": rep_admins}
    return ops_render(request, "account/index.html", rep)


def admin_set(request):
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加管理员账号成功～", "data": {}}
        request_json = request.POST
        # TODO 此处应该出参数校验
        nickname = request_json.get("nickname", "")
        mobile = request_json.get("mobile", "")
        email = request_json.get("email", "")
        login_name = request_json.get("login_name", "")
        login_pwd = request_json.get("login_pwd", "")
        id = request_json.get("id", "")

        if id:
            user = User.objects.filter(id=id)[0]
            user.nickname = nickname
            user.mobile = mobile
            user.email = email
            user.username = login_name
            if login_pwd == "******":
                pass
            else:
                password = UserService.gene_pwd(login_pwd, user.salt)
                user.password = password
            user.save()
            response["msg"] = "修改成功"
        else:
            if len(User.objects.filter(username=login_name)) > 0:
                response["msg"] = "登录名已经存在~"
                response["code"] = 1
            else:
                salt = UserService.gene_salt()
                password = UserService.gene_pwd(login_pwd, salt)
                save_user = {
                    "username": login_name,
                    "password": password,
                    "salt": salt,
                    "type": 2,
                    "nickname": nickname,
                    "email": email,
                    "mobile": mobile
                }
                User.objects.create(**save_user)

        return JsonResponse(response)
    rep = {}
    id = request.GET.get("id", "")
    info = {'type': -1}
    if id:
        user = User.objects.filter(id=id).first()
        if user:
            info["nickname"] = user.nickname
            info["mobile"] = user.mobile
            info['email'] = user.email
            info['login_name'] = user.username
            info['id'] = user.id
            info['type'] = user.type
    else:
        pass
    rep["info"] = info
    return ops_render(request, "account/set.html", rep)


def admin_info(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    rep = {}
    id = request.GET.get("id", "")
    info = {'type': -1}
    if id:
        user = User.objects.filter(id=id).first()
        if user:
            info["nickname"] = user.nickname
            info["mobile"] = user.mobile
            info['email'] = user.email
            info['login_name'] = user.username
            info['id'] = user.id
            info['type'] = user.type
    else:
        pass
    rep["info"] = info
    return ops_render(request, "account/info.html", rep)


def admin_ops(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加管理员账号成功～", "data": {}}
        request_json = request.POST
        # TODO 此处应该出参数校验
        act = request_json.get("act", "")
        id = request_json.get("id", "")
        user = User.objects.filter(id=id)[0]
        if act == "recover":
            user.status = 1
            response["msg"] = "恢复账号"
        else:
            user.status = 0
            response["msg"] = "禁用账号"
        user.save()
        return JsonResponse(response)
    return HttpResponse(status=404)


def major_class(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    rep = {}
    my_list = []

    major_class_array = MajorClass.objects.all()
    for class_item in major_class_array:
        item = {
            "id": class_item.id,
            "name": class_item.name,
            "status_desc": "正常" if class_item.status == 1 else "删除",
            "weight": class_item.weight,
            "status": class_item.status,
        }
        my_list.append(item)
    rep["list"] = my_list
    rep["current"] = "class"
    rep["status_mapping"] = ["正常", "删除"]
    rep["search_con"] = {"status": "正常"}

    return ops_render(request, "major/major_class.html", rep)


def major_class_set(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加分类成功～", "data": {}}
        request_json = request.POST
        name = request_json.get("name", "")
        weight = request_json.get("weight", 1)
        id = request_json.get("id")
        if id:
            majors = MajorClass.objects.filter(id=id)
            if majors:
                major = majors[0]
                major.name = name
                major.weight = weight
                major.save()
            return JsonResponse(response)
        save_dice = {
            "name": name,
            "weight": weight
        }
        MajorClass.objects.create(**save_dice)

        return JsonResponse(response)

    rep = {}
    id = request.GET.get("id")

    info = {}
    major_class_array = MajorClass.objects.filter(id=id)
    if major_class_array:
        major = major_class_array[0]
        name = major.name
        weight = major.weight
        info["name"] = name
        info["weight"] = weight
        info["id"] = major.id
    rep["info"] = info

    return ops_render(request, "major/major_class_set.html", rep)


def major_class_ops(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加管理员账号成功～", "data": {}}
        request_json = request.POST
        # TODO 此处应该出参数校验
        act = request_json.get("act", "")
        id = request_json.get("id", "")
        major = MajorClass.objects.filter(id=id)[0]
        if act == "remove":
            major.status = 0
            response["msg"] = "禁用分类"
        else:
            major.status = 1
            response["msg"] = "恢复分类"
        major.save()
        return JsonResponse(response)
    return HttpResponse(status=404)


def major_first(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    rep = {}
    my_list = []
    major_class_array = MajorFirst.objects.all()
    for class_item in major_class_array:
        major = class_item.major_class
        item = {
            "id": class_item.id,
            "name": class_item.name,
            "status_desc": "正常" if class_item.status == 1 else "删除",
            "weight": class_item.weight,
            "status": class_item.status,
            "class_name": major.name
        }
        my_list.append(item)
    rep["list"] = my_list
    rep["current"] = "first"
    rep["status_mapping"] = ["正常", "删除"]
    rep["search_con"] = {"status": "正常"}

    return ops_render(request, "major/major_first.html", rep)


def major_first_set(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加一级专业成功～", "data": {}}
        request_json = request.POST
        name = request_json.get("name", "")
        weight = request_json.get("weight", 1)
        id = request_json.get("id")
        major_id = request_json.get("major_id")

        major = MajorClass.objects.filter(id=major_id)[0]
        if id:
            firsts = MajorFirst.objects.filter(id=id)
            if firsts:
                first = firsts[0]
                first.name = name
                first.weight = weight
                first.major_class = major
                first.save()
            return JsonResponse(response)
        save_dice = {
            "name": name,
            "weight": weight,
            "major_class": major
        }
        MajorFirst.objects.create(**save_dice)

        return JsonResponse(response)

    rep = {}
    id = request.GET.get("id")

    info = {}
    major_first_array = MajorFirst.objects.filter(id=id)
    if major_first_array:
        first = major_first_array[0]
        name = first.name
        weight = first.weight
        info["name"] = name
        info["weight"] = weight
        info["id"] = first.id
        info['major_id'] = first.major_class.id
    rep["info"] = info

    major_list = []
    # 查询所有可以使用的分类
    majors = MajorClass.objects.filter(status=1)
    for major in majors:
        id = major.id
        name = major.name
        major_list.append({"id": id, "name": name})

    rep["major_list"] = major_list
    return ops_render(request, "major/major_first_set.html", rep)


def major_first_ops(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加管理员账号成功～", "data": {}}
        request_json = request.POST
        # TODO 此处应该出参数校验
        act = request_json.get("act", "")
        id = request_json.get("id", "")
        major = MajorFirst.objects.filter(id=id)[0]
        if act == "remove":
            major.status = 0
            response["msg"] = "禁用专业"
        else:
            major.status = 1
            response["msg"] = "恢复专业"
        major.save()
        return JsonResponse(response)
    return HttpResponse(status=404)


def major_second(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    rep = {}
    my_list = []
    major_class_array = MajorSecond.objects.all()
    for class_item in major_class_array:
        first = class_item.major_first
        item = {
            "id": class_item.id,
            "name": class_item.name,
            "status_desc": "正常" if class_item.status == 1 else "删除",
            "weight": class_item.weight,
            "status": class_item.status,
            "first_name": first.name,
            "class_name": first.major_class.name,
            "declare": {
                "start": class_item.declare_start_time,
                "end": class_item.declare_end_time
            },
            "review": {
                "start": class_item.review_start_time,
                "end": class_item.review_end_time
            }
        }
        my_list.append(item)
    rep["list"] = my_list
    rep["current"] = "second"
    rep["status_mapping"] = ["正常", "删除"]
    rep["search_con"] = {"status": "正常"}

    return ops_render(request, "major/major_second.html", rep)


def major_second_set(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    if request.method == "POST":
        response = {'code': 200, 'msg': "添加一级专业成功～", "data": {}}
        request_json = request.POST
        name = request_json.get("name", "")
        weight = request_json.get("weight", 1)
        id = request_json.get("id")
        first_id = request_json.get("first_id")
        declare_start = request_json.get("declare_start")
        declare_end = request_json.get("declare_end")
        review_start = request_json.get("review_start")
        review_end = request_json.get("review_end")

        first = MajorFirst.objects.filter(id=first_id)[0]
        if id:
            seconds = MajorSecond.objects.filter(id=id)
            if seconds:
                second = seconds[0]
                second.name = name
                second.major_first = first
                second.weight = weight
                second.declare_start_time = get_date_form_str(declare_start, "%Y-%m-%d %H:%M")
                second.declare_end_time = get_date_form_str(declare_end, "%Y-%m-%d %H:%M")
                second.review_start_time = get_date_form_str(review_start, "%Y-%m-%d %H:%M")
                second.review_end_time = get_date_form_str(review_end, "%Y-%m-%d %H:%M")
                second.save()
            return JsonResponse(response)
        save_dice = {
            "name": name,
            "weight": weight,
            "major_first": first,
            "declare_start_time": get_date_form_str(declare_start, "%Y-%m-%d %H:%M"),
            "declare_end_time": get_date_form_str(declare_end, "%Y-%m-%d %H:%M"),
            "review_start_time": get_date_form_str(review_start, "%Y-%m-%d %H:%M"),
            "review_end_time": get_date_form_str(review_end, "%Y-%m-%d %H:%M"),
        }
        MajorSecond.objects.create(**save_dice)

        return JsonResponse(response)

    rep = {}
    id = request.GET.get("id")

    info = {}
    major_second_array = MajorSecond.objects.filter(id=id)
    if major_second_array:
        second = major_second_array[0]
        name = second.name
        weight = second.weight
        info["name"] = name
        info["weight"] = weight
        info["id"] = second.id
        info['first_id'] = second.major_first.id
        info['class_id'] = second.major_first.major_class.id
        info["declare_start"] = getFormatDate(second.declare_start_time, "%Y-%m-%d %H:%M")
        info["declare_end"] = getFormatDate(second.declare_end_time, "%Y-%m-%d %H:%M")
        info["review_start"] = getFormatDate(second.review_start_time, "%Y-%m-%d %H:%M")
        info["review_end"] = getFormatDate(second.review_end_time, "%Y-%m-%d %H:%M")
    rep["info"] = info

    major_list = []
    # 查询所有可以使用的分类
    firsts = MajorFirst.objects.filter(status=1)
    for first in firsts:
        id = first.id
        name = first.name
        first_in_major_class = first.major_class
        c_id = first_in_major_class.id
        c_name = first_in_major_class.name
        major_list.append({"id": id, "name": name, "c_id": c_id, "c_name": c_name})

    rep["major_list"] = major_list
    return ops_render(request, "major/major_second_set.html", rep)


def major_second_ops(request):
    return None


def user(request):
    if request.myself.type == 1:
        return HttpResponse("普通用户不用来管理员界面玩耍～")
    args = request.GET
    # 分类 过滤
    c = int(args.get("c", -1))
    # first major 过滤
    f = int(args.get("f", -1))
    # second major 过滤
    s = int(args.get("s", -1))
    # 排序 1 = 分数倒叙 2 = 分数顺序 3 = 创建时间倒叙 4 = 创建时间顺序
    sort = int(args.get("sort", 0))
    rep_admins = []

    admins = User.objects.filter(type=1)

    for admin in admins:
        enroll_name = "没有报名"
        enroll_time = get_date_form_str(detester="1900-1-1", format="%Y-%m-%d")
        enrolls = Enroll.objects.filter(uid=admin)
        second_id = -1
        if len(enrolls) == 1:
            enroll_name = enrolls[0].major.name
            enroll_time = enrolls[0].add_time
            second_id = enrolls[0].major
        marks = Mark.objects.filter(uid=admin)
        mark = 0

        if len(marks) == 1:
            mark = marks[0].sum

        item = {"id": admin.id,
                "nickname": admin.nickname,
                "username": admin.username,
                "add_time": admin.add_time,
                "enroll_name": enroll_name,
                "enroll_time": enroll_time,
                "mark": mark,
                "status": admin.status,
                "major_second_id": second_id
                }
        rep_admins.append(item)

    major_class_array = MajorClass.objects.all()

    # 如果c不对-1，说明要通过id去过滤类别
    if int(c) > 0:
        # 第一专业需要过滤
        major_first_array = MajorFirst.objects.filter(major_class_id=c)
    else:
        major_first_array = MajorFirst.objects.all()

    # 如果f不是-1 ，那么也需要过滤第二专业
    if int(f) > 0:
        item_major_first_array = major_first_array.filter(id=f)
    else:
        item_major_first_array = major_first_array

    if sort == 0:
        pass
    elif sort == 1:
        rep_admins = sorted(rep_admins, key=lambda x: x['enroll_time'], reverse=True)
    elif sort == 2:
        rep_admins = sorted(rep_admins, key=lambda x: x['enroll_time'], reverse=False)
    elif sort == 3:
        rep_admins = sorted(rep_admins, key=lambda x: x['mark'], reverse=True)
    elif sort == 4:
        rep_admins = sorted(rep_admins, key=lambda x: x['mark'], reverse=False)

    sorts = [
        {"id": 1, "name": "报名时间倒叙"},
        {"id": 2, "name": "报名时间顺序"},
        {"id": 3, "name": "分数倒序"},
        {"id": 4, "name": "分数顺序"}
    ]

    ids = list([first_id.id for first_id in item_major_first_array])
    major_second_array = MajorSecond.objects.filter(major_first_id__in=ids)
    new_rep_admins = []
    for item in major_second_array:
        for rep_admins_item in rep_admins:
            if rep_admins_item["enroll_name"] == item.name:
                print("我被添加了")
                new_rep_admins.append(rep_admins_item)
    rep_admins = new_rep_admins
    rep = {
        "list": rep_admins,
        "classs": major_class_array,
        "firsts": major_first_array,
        "seconds": major_second_array,
        "c": c,
        "f": f,
        "s": s,
        "sorts": sorts,
        "sort_status": sort
    }
    return ops_render(request, "user/index.html", rep)


def add_major(request):
    # uid:2
    # major_second_id:3
    try:
        uid = request.POST.get("uid")
        major_second_id = request.POST.get("major_second_id")
        Enroll.objects.create(uid_id=uid, major_id=major_second_id)
        response = {'code': 200, 'msg': "申报成功～", "data": {}}
        return JsonResponse(response)
    except:
        response = {'code': -1, 'msg': "申报失败～", "data": {}}
        return JsonResponse(response)


def new(request):
    if request.myself.type == 2:
        return HttpResponse("管理员就不用进来了～，服务器会奔溃的")
    major_second_array = MajorSecond.objects.all()

    majors = []
    for major_second_item in major_second_array:
        major_first = major_second_item.major_first
        major_first_id = major_second_item.major_first.id
        major_first_name = major_second_item.major_first.name
        major_class = major_first.major_class
        major_class_id = major_class.id
        major_class_name = major_class.name
        major_second_id = major_second_item.id
        major_second_name = major_second_item.name
        major_second_declare_start_time = major_second_item.declare_start_time
        major_second_declare_end_time = major_second_item.declare_end_time
        major_second_review_start_time = major_second_item.review_start_time
        major_second_review_end_time = major_second_item.review_end_time
        major_second_add_time = major_second_item.add_time
        majors.append({
            "major_first_id": major_first_id,
            "major_first_name": major_first_name,
            "major_class_id": major_class_id,
            "major_class_name": major_class_name,
            "major_second_id": major_second_id,
            "major_second_name": major_second_name,
            "major_second_declare_start_time": major_second_declare_start_time,
            "major_second_declare_end_time": major_second_declare_end_time,
            "major_second_review_start_time": major_second_review_start_time,
            "major_second_review_end_time": major_second_review_end_time,
            "major_second_add_time": major_second_add_time,
        })
    ret = {
        "majors": majors
    }
    return ops_render(request, "new/index.html", ret)


def sum_mark(user,
             p_c_or_q_array=[],
             thesis_works_array=[],
             national_patent_array=[],
             technological_innovation_array=[],
             skills_competition_array=[],
             honour_array=[],
             professional_array=[],
             edu_array=[]
             ):
    ret = {}
    mark = None
    models = Mark.objects.filter(uid=user)
    if len(models) == 1:
        mark = models[0]
    else:
        mark = Mark.objects.create(uid=user)
    total = 0
    # TODO 这里可以把表达式提出去做扩展，时间问题cv操作。
    # 专业认证或资质 权重 10%
    # 定义一个集合接收所有的分数
    mark_p_c_or_q_array = []
    for item in p_c_or_q_array:
        level = item.level
        if level == 1:
            temp = 50
        elif level == 2:
            temp = 30
        elif level == 3:
            temp = 20
        elif level == 4:
            temp = 40
        elif level == 5:
            temp = 20
        elif level == 6:
            temp = 10
        else:
            temp = 0
        # 添加
        mark_p_c_or_q_array.append(temp)
    # 倒叙排序取最高的两个
    mark_p_c_or_q_array = sorted(mark_p_c_or_q_array, reverse=True)[:2]
    p_c_or_q_array_sum = sum(mark_p_c_or_q_array) * 10 / 100
    ret["p_c_or_q_array_sum"] = p_c_or_q_array_sum
    ret['p_c_or_q_must'] = 10
    mark.professional_certification_or_qualification = p_c_or_q_array_sum
    total += p_c_or_q_array_sum

    # 专业认证或资质 权重 20%
    # 定义一个集合接收所有的分数
    mark_thesis_works_array = []
    for item in thesis_works_array:
        level = item.level
        if level == 1:
            temp = 100
        elif level == 2:
            temp = 80
        elif level == 3:
            temp = 50
        elif level == 4:
            temp = 30
        elif level == 5:
            temp = 80
        elif level == 6:
            temp = 40
        else:
            temp = 0
        # 添加
        mark_thesis_works_array.append(temp)
    # 倒叙排序取最高的两个
    mark_thesis_works_array = sorted(mark_thesis_works_array, reverse=True)[:3]
    thesis_works_array_sum = sum(mark_thesis_works_array)
    if thesis_works_array_sum > 100:
        thesis_works_array_sum = 100
    thesis_works_array_sum = thesis_works_array_sum * 20 / 100
    ret["thesis_works_array_sum"] = thesis_works_array_sum
    ret['thesis_works_array_must'] = 20
    mark.thesis_works = thesis_works_array_sum
    total += thesis_works_array_sum
    # 国家专利 权重 5%
    # 定义一个集合接收所有的分数
    mark_national_patent_array = []
    for item in national_patent_array:
        level = item.level
        if level == 1:
            temp = 100
        elif level == 2:
            temp = 50
        else:
            temp = 0
        # 添加
        mark_national_patent_array.append(temp)
    # 倒叙排序取最高的两个
    mark_national_patent_array = sorted(mark_national_patent_array, reverse=True)[:2]
    national_patent_array_sum = sum(mark_national_patent_array)
    if national_patent_array_sum > 100:
        national_patent_array_sum = 100
    national_patent_array_sum = national_patent_array_sum * 5 / 100
    ret["national_patent_array_sum"] = national_patent_array_sum
    ret['national_patent_array_must'] = 5
    mark.national_patent = national_patent_array_sum
    total += national_patent_array_sum
    # 科技进步、创新奖 权重 20%
    # 定义一个集合接收所有的分数
    mark_technological_innovation_array = []
    for item in technological_innovation_array:
        level = item.level
        if level == 1:
            temp = 100
        elif level == 2:
            temp = 90
        elif level == 3:
            temp = 85
        elif level == 4:
            temp = 60
        elif level == 5:
            temp = 50
        elif level == 6:
            temp = 45
        elif level == 7:
            temp = 30
        elif level == 8:
            temp = 20
        elif level == 9:
            temp = 15
        else:
            temp = 0
        # 添加
        mark_technological_innovation_array.append(temp)
    # 倒叙排序取最高的两个
    mark_technological_innovation_array = sorted(mark_technological_innovation_array, reverse=True)[:3]
    technological_innovation_array_sum = sum(mark_technological_innovation_array)
    if technological_innovation_array_sum > 100:
        technological_innovation_array_sum = 100
    technological_innovation_array_sum = technological_innovation_array_sum * 20 / 100
    ret["technological_innovation_array_sum"] = technological_innovation_array_sum
    ret['technological_innovation_array_must'] = 20
    mark.technological_innovation = technological_innovation_array_sum
    total += technological_innovation_array_sum

    # 技能竞赛、创新奖 权重 20%
    # 定义一个集合接收所有的分数
    mark_skills_competition_array = []
    for item in skills_competition_array:
        level = item.level
        if level == 1:
            temp = 100
        elif level == 2:
            temp = 80
        elif level == 3:
            temp = 60
        elif level == 4:
            temp = 40
        elif level == 5:
            temp = 60
        elif level == 6:
            temp = 50
        elif level == 7:
            temp = 40
        elif level == 8:
            temp = 30
        elif level == 9:
            temp = 40
        elif level == 10:
            temp = 35
        elif level == 11:
            temp = 30
        else:
            temp = 0
        # 添加
        mark_skills_competition_array.append(temp)
    # 倒叙排序取最高的两个
    mark_skills_competition_array = sorted(mark_skills_competition_array, reverse=True)[:3]
    skills_competition_array_sum = sum(mark_skills_competition_array)
    if skills_competition_array_sum > 100:
        skills_competition_array_sum = 100
    skills_competition_array_sum = skills_competition_array_sum * 20 / 100
    ret["skills_competition_array_sum"] = skills_competition_array_sum
    ret['skills_competition_array_must'] = 20
    mark.skills_competition = skills_competition_array_sum
    total += skills_competition_array_sum

    # 荣誉奖章 权重 10%
    # 定义一个集合接收所有的分数
    mark_honour_array = []
    for item in honour_array:
        level = item.level
        if level == 1:
            temp = 100
        elif level == 2:
            temp = 60
        elif level == 3:
            temp = 30
        else:
            temp = 0
        # 添加
        mark_honour_array.append(temp)
    # 倒叙排序取最高的两个
    mark_honour_array = sorted(mark_honour_array, reverse=True)[:3]
    honour_array_sum = sum(mark_honour_array)
    if honour_array_sum > 100:
        honour_array_sum = 100
    honour_array_sum = honour_array_sum * 10 / 100
    ret["honour_array_sum"] = honour_array_sum
    ret['honour_array_must'] = 10
    mark.honour = honour_array_sum
    total += honour_array_sum

    # 职称/职鉴 权重 5%
    # 定义一个集合接收所有的分数
    mark_professional_array = []
    for item in professional_array:
        level = item.level
        if level == 1:
            temp = 30
        elif level == 2:
            temp = 60
        elif level == 3:
            temp = 100
        else:
            temp = 0
        # 添加
        mark_professional_array.append(temp)
    # 倒叙排序取最高的两个
    mark_professional_array = sorted(mark_professional_array, reverse=True)[:1]
    professional_array_sum = sum(mark_professional_array)
    if professional_array_sum > 100:
        professional_array_sum = 100
    professional_array_sum = professional_array_sum * 5 / 100
    ret["professional_array_sum"] = professional_array_sum
    ret['professional_array_must'] = 5
    mark.professional = professional_array_sum
    total += professional_array_sum

    # 学历/学位 权重 5%
    # 定义一个集合接收所有的分数
    mark_edu_array = []
    for item in edu_array:
        level = item.degree
        if level == 1:
            temp = 50
        elif level == 2:
            temp = 80
        elif level == 3:
            temp = 100
        else:
            temp = 0
        # 添加
        mark_edu_array.append(temp)
    # 倒叙排序取最高的两个
    mark_edu_array = sorted(mark_edu_array, reverse=True)[:1]
    edu_array_sum = sum(mark_edu_array)
    if edu_array_sum > 100:
        edu_array_sum = 100
    edu_array_sum = edu_array_sum * 10 / 100
    ret["edu_array_sum"] = edu_array_sum
    ret["edu_array_must"] = 10
    mark.edu = edu_array_sum
    total += edu_array_sum
    mark.sum = total
    mark.save()
    ret['total'] = total
    return ret


def resume(request):
    that = request.myself
    ret = {'that': that}
    uid = request.GET.get("uid", "")
    user = that
    if uid:
        users = User.objects.filter(id=uid)
        if len(users) == 1:
            user = users[0]
            ret["that"] = user
        else:
            return HttpResponse("服务器异常，没有该用户～")
    enrolls = Enroll.objects.filter(uid=user, status=1)
    if len(enrolls) != 1:
        if request.myself.type == 2:
            return HttpResponse("管理员就不用进来了～，服务器会奔溃的")
        return HttpResponseRedirect("/new")
    p_c_or_q_array = ProfessionalCertificationOrQualification.objects.filter(uid=user)
    ret['p_c_or_q_array'] = p_c_or_q_array
    thesis_works_array = ThesisWorks.objects.filter(uid=user)
    ret['thesis_works_array'] = thesis_works_array
    national_patent_array = NationalPatent.objects.filter(uid=user)
    ret['national_patent_array'] = national_patent_array
    technological_innovation_array = TechnologicalInnovation.objects.filter(uid=user)
    ret['technological_innovation_array'] = technological_innovation_array
    skills_competition_array = SkillsCompetition.objects.filter(uid=user)
    ret['skills_competition_array'] = skills_competition_array
    honour_array = Honour.objects.filter(uid=user)
    ret['honour_array'] = honour_array
    professional_array = Professional.objects.filter(uid=user)
    ret['professional_array'] = professional_array
    edu_array = Edu.objects.filter(uid=user)
    ret['edu_array'] = edu_array
    mark_ret = sum_mark(user, p_c_or_q_array=p_c_or_q_array,
                        thesis_works_array=thesis_works_array,
                        national_patent_array=national_patent_array,
                        technological_innovation_array=technological_innovation_array,
                        skills_competition_array=skills_competition_array,
                        honour_array=honour_array,
                        professional_array=professional_array,
                        edu_array=edu_array)
    ret['mark'] = mark_ret
    major = enrolls[0].major
    ret['major_second'] = major
    n_time = datetime.datetime.now()

    is_update = False
    if n_time > major.declare_start_time and n_time < major.declare_end_time:
        is_update = True
    if request.myself.type == 2:
        is_update = True
    ret["is_update"] = is_update
    return ops_render(request, "new/resume.html", ret)


def resume_update(request):
    if request.method == "GET":
        return HttpResponse("异常请求～")

    req_dict = request.POST
    uid = req_dict.get("uid")
    type = req_dict.get("type")
    user = None
    if uid:
        users = User.objects.filter(id=uid)
        if len(users) == 1:
            user = users[0]
        else:
            return HttpResponse("服务器异常，没有该用户～")
    else:
        return HttpResponse("服务器异常，没有该用户～")
    if type == "user-info":
        user.nickname = req_dict.get("nickname", "")
        user.gender = req_dict.get("gender", "")
        birthday = req_dict.get("birthday")
        if not birthday:
            birthday = "2000-12-12"
        user.birthday = get_date_form_str(birthday)
        enter_the_employment_time = req_dict.get("enter_the_employment_time", "2000-12-12")
        if not enter_the_employment_time:
            enter_the_employment_time = "2000-12-12"
        user.enter_the_employment_time = get_date_form_str(enter_the_employment_time)
        user.household_register_province = req_dict.get("household_register_province", "")
        user.household_register_city = req_dict.get("household_register_city", "")
        user.live_province = req_dict.get("live_province", "")
        user.live_city = req_dict.get("live_city", "")
        user.live_district = req_dict.get("live_district", "")
        user.mobile = req_dict.get("mobile", "")
        user.email = req_dict.get("email", "")
        user.work_unit = req_dict.get("work_unit", "")
        user.department = req_dict.get("department", "")
        user.marriage_status = req_dict.get("marriage_status", "")
        user.politics = req_dict.get("politics", "")
        user.globetrotters = req_dict.get("globetrotters", "")
        user.portrait = req_dict.get("portrait", "")
        user.save()
        pass
    elif type == "professional_certification_or_qualification":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = ProfessionalCertificationOrQualification.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]

        if not model:
            model = ProfessionalCertificationOrQualification.objects.create(uid=user)

        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "thesis_works":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = ThesisWorks.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]

        if not model:
            model = ThesisWorks.objects.create(uid=user)

        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "national_patent":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = NationalPatent.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]

        if not model:
            model = NationalPatent.objects.create(uid=user)

        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "technological_innovation":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = TechnologicalInnovation.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]
        if not model:
            model = TechnologicalInnovation.objects.create(uid=user)
        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "skills_competition":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = SkillsCompetition.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]

        if not model:
            model = SkillsCompetition.objects.create(uid=user)

        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "honour":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = Honour.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]

        if not model:
            model = Honour.objects.create(uid=user)

        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "professional":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = Professional.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]

        if not model:
            model = Professional.objects.create(uid=user)

        model.name = req_dict.get("describe_name")
        model.level = req_dict.get("level")
        obtain_time = req_dict.get("obtain_time", "2000-12-12")
        if not obtain_time:
            obtain_time = "2000-12-12"
        model.obtain_time = get_date_form_str(obtain_time)
        model.extra = req_dict.get('extra')
        model.save()
    elif type == "edu":
        item_id = req_dict.get("item_id", "")
        model = None
        if item_id:
            models = Edu.objects.filter(id=item_id)
            if len(models) == 1:
                model = models[0]
        if not model:
            model = Edu.objects.create(uid=user)
        model.name = req_dict.get("name")
        graduate_start_time = req_dict.get("graduate_start_time", "2000-12-12")
        if not graduate_start_time:
            graduate_start_time = "2000-12-12"
        model.graduate_start_time = get_date_form_str(graduate_start_time)
        graduate_end_time = req_dict.get("graduate_end_time", "2000-12-12")
        if not graduate_end_time:
            graduate_end_time = "2000-12-12"
        model.graduate_end_time = get_date_form_str(graduate_end_time)
        model.major = req_dict.get('major')
        model.colleges = req_dict.get('colleges')
        model.education = req_dict.get('education')
        model.degree = req_dict.get('degree')
        model.save()

    response = {'code': 200, 'msg': "更新成功", "data": {"type": type}}
    return JsonResponse(response)
