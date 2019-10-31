from datetime import datetime

from django.db import models


# Create your models here.


class User(models.Model):
    """
    用户model
    """
    username = models.CharField(
        max_length=16, verbose_name=u"用户名", unique=True)
    password = models.CharField(max_length=32, verbose_name=u"密码")

    nickname = models.CharField(
        max_length=16, verbose_name=u"昵称", default=u"", blank=True, null=True)
    gender = models.CharField(choices=(("male", u"男"), ("female", "女")), max_length=10, default='male',
                              verbose_name=u"性别")
    birthday = models.DateTimeField(
        verbose_name=u"出生日期", blank=True, null=True)
    enter_the_employment_time = models.DateTimeField(
        verbose_name=u"入职时间", blank=True, null=True)
    household_register_province = models.CharField(
        verbose_name=u"户口所在（省）", blank=True, null=True, max_length=32, default="")
    household_register_city = models.CharField(
        verbose_name=u"户口所在（市）", blank=True, null=True, max_length=32, default="")
    live_province = models.CharField(
        verbose_name=u"现居城市（省）", blank=True, null=True, max_length=32, default="")
    live_city = models.CharField(
        verbose_name=u"现居城市（市）", blank=True, null=True, max_length=32, default="")
    live_district = models.CharField(
        verbose_name=u"现居城市（县）", blank=True, null=True, max_length=32, default="")
    mobile = models.CharField(
        max_length=11, default=u"", verbose_name=u"手机号码", null=True, blank=True)
    email = models.CharField(
        max_length=64, verbose_name=u"邮箱", default=u"", blank=True, null=True)
    work_unit = models.CharField(
        verbose_name=u"工作单位", blank=True, null=True, max_length=32, default="")
    department = models.CharField(
        verbose_name=u"所在部门", blank=True, null=True, max_length=32, default="")
    marriage_status = models.CharField(verbose_name=u"婚姻状况", blank=True, null=True, max_length=32,
                                       choices=(("未婚", "未婚"), ("已婚", "已婚"), ("离异", "离异")), default="未婚")
    politics = models.CharField(verbose_name=u"政治面貌", blank=True, null=True, max_length=32,
                                choices=(("群众", "群众"), ("团员", "团员"), ("中共党员(含预备党员)", "中共党员(含预备党员)"), ("民主党派", "民主党派"),
                                         ("无党派人士", "无党派人士")), default="群众")
    globetrotters = models.CharField(verbose_name=u"海外经历", blank=True, null=True, max_length=32,
                                     choices=(("有", "有"), ("无", "无")), default="无")
    id_card = models.CharField(
        max_length=18, verbose_name=u"身份证号码", default="")
    portrait = models.CharField(
        max_length=300, blank=True, null=True, verbose_name=u"头像", default="")
    salt = models.CharField(max_length=36, verbose_name="密码密钥")
    type = models.IntegerField(
        choices=((1, u'用户'), (2, u'管理员')), default=1, verbose_name=u"用户权限")
    status = models.IntegerField(
        choices=((1, u"有效"), (0, u"无效")), default=1, verbose_name=u"是否是有效用户")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"注册时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"修改时间")

    class Mate:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Edu(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"学校名称", default="")

    graduate_start_time = models.DateTimeField(verbose_name=u"开始时间", null=True, blank=True, auto_now_add=True)
    graduate_end_time = models.DateTimeField(verbose_name=u"结束时间", null=True, blank=True, auto_now_add=True)
    major = models.CharField(max_length=32, verbose_name=u"专业", default="")
    colleges = models.CharField(max_length=32, verbose_name=u"院校", default="")
    education = models.IntegerField(choices=(
        (1, u"初中"),
        (2, u"中技"),
        (3, u"高中"),
        (4, u"大专"),
        (5, u"本科"),
        (6, u"硕士"),
        (7, u"MBA"),
        (8, u"EMBA"),
        (9, u"博士"),
        (10, u"其他")
    ), default=1, verbose_name=u"学历")
    degree = models.IntegerField(choices=(
        (1, "学士学位"),
        (2, "硕士学位"),
        (3, "博士学位"),
        (4, "其他"),
    ), default=1, verbose_name=u"学位")

    class Mate:
        verbose_name = u'教育'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Professional(models.Model):
    """
    职称/职鉴
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"职称/职鉴", default="")
    obtain_time = models.DateTimeField(verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)
    level = models.IntegerField(verbose_name=u"等级", choices=(
        (1, "初级"), (2, "中级(中级技师)"), (3, "高级(高级技师)")), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'职称/职鉴'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Honour(models.Model):
    """
    荣誉奖章
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"荣誉奖章", default="")
    obtain_time = models.DateTimeField(
        verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)
    level = models.IntegerField(verbose_name=u"等级", choices=(
        (1, "国家级技术能手、五一劳动奖章、劳动模范（先进工作者、标兵)"),
        (2, "省、部、集团级技术能手、五一劳动奖章、劳动模范（先进工作者、标兵)"),
        (3, "地、厅、省公司级技术能手、五一劳动奖章、劳动模范（先进工作者、标兵)")), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'荣誉奖章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SkillsCompetition(models.Model):
    """
    技能竞赛
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"技能竞赛", default="")
    obtain_time = models.DateTimeField(
        verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)
    level = models.IntegerField(verbose_name=u"等级", choices=(
        (1, "国家级(一等奖)"),
        (2, "国家级(二等奖)"),
        (3, "国家级(三等奖)"),
        (4, "国家级(优秀奖或团体奖)"),
        (5, "省、部、集团级(一等奖)"),
        (6, "省、部、集团级(二等奖)"),
        (7, "省、部、集团级(三等奖)"),
        (8, "省、部、集团级(优秀奖或团体奖)"),
        (9, "地、厅、省公司级(一等奖)"),
        (10, "地、厅、省公司级(二等奖)"),
        (11, "地、厅、省公司级(三等奖)")
    ), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'技能竞赛'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TechnologicalInnovation(models.Model):
    """
    科技创新
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"科技创新", default="")
    obtain_time = models.DateTimeField(
        verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)
    level = models.IntegerField(verbose_name=u"等级", choices=(
        (1, "国家级(一等奖)"),
        (2, "国家级(二等奖)"),
        (3, "国家级(三等奖)"),
        (4, "省、部、集团级(一等奖)"),
        (5, "省、部、集团级(二等奖)"),
        (6, "省、部、集团级(三等奖)"),
        (7, "地、厅、省公司级(已等奖)"),
        (8, "地、厅、省公司级(已等奖)"),
        (9, "地、厅、省公司级(已等奖)"),
    ), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'科技创新'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class NationalPatent(models.Model):
    """
    国家专利
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"国家专利", default="")
    obtain_time = models.DateTimeField(
        verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)
    level = models.IntegerField(verbose_name=u"等级", choices=(
        (1, "国家发明专利"), (2, "实用行新型专利")), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'国家专利'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ThesisWorks(models.Model):
    """
    论文著作
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"论文著作", default="")
    obtain_time = models.DateTimeField(
        verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)

    level = models.IntegerField(verbose_name=u"等级", choices=((1, "在核心期刊发表论文或被SCI、EI、ISTP等收录的论文(第一作者)"),
                                                             (2, "在核心期刊发表论文或被SCI、EI、ISTP等收录的论文(合著者)"),
                                                             (3, "在CN期刊上发表的论文(第一作者)"),
                                                             (4, "在CN期刊上发表的论文(合著者)"),
                                                             (5, "著作第一主编"),
                                                             (6, "副主编或编委"),), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'论文著作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProfessionalCertificationOrQualification(models.Model):
    """
    专业认证或资质
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    name = models.CharField(max_length=32, verbose_name=u"专业认证或资质", default="")
    obtain_time = models.DateTimeField(
        verbose_name=u"获取时间", null=True, blank=True, auto_now_add=True)

    level = models.IntegerField(verbose_name=u"等级", choices=((1, "国际认证证书高级"),
                                                             (2, "国际认证证书中级"),
                                                             (3, "国际认证证书初级"),
                                                             (4, "国内认证证书高级"),
                                                             (5, "国内认证证书中级"),
                                                             (6, "国内认证证书初级"),), default=1)
    extra = models.CharField(verbose_name=u"额外的资料",
                             max_length=255, blank=True, null=True, default="")

    class Mate:
        verbose_name = u'专业认证或资质'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    """
    个人信息model
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=u"账号")
    photo = models.ImageField(upload_to="image/%Y/%m",
                              default=u"image/default.png", max_length=100)
    nick = models.CharField(max_length=16, verbose_name=u"姓名")
    gender = models.CharField(max_length=6, choices=(
        ("male", u"男"), ("female", u"女")), verbose_name=u"性别")
    birth_time = models.DateTimeField(default=datetime.strptime('2019-1-1 12:0:0', '%Y-%m-%d %H:%M:%S'),
                                      verbose_name=u"出生日期")
    id_card = models.CharField(max_length=18, verbose_name=u"身份证号码")
    political_landscape = models.CharField(
        max_length=20, default=u"群众", verbose_name=u"政治面貌")
    native_place = models.CharField(
        max_length=20, default=u"", verbose_name=u"籍贯")
    work_units = models.CharField(
        max_length=100, default=u"", verbose_name=u"工作单位")
    department = models.CharField(
        max_length=100, default=u"", verbose_name=u"所在部门")

    class Mate:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.username, self.nick)


class EducationInfo(models.Model):
    """
    教育信息
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=u"账号")
    graduate_school = models.CharField(
        max_length=200, default=u"", verbose_name=u"毕业院校")
    graduate_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"毕业院校")
    education_type = models.CharField(
        max_length=100, choices=(), default=u"", verbose_name=u"受教育类型")
    degree = models.CharField(
        max_length=100, choices=(), default=u"", verbose_name=u"学位")
    education = models.CharField(
        max_length=100, choices=(), default=u"", verbose_name=u"学历")
    institutions = models.CharField(
        max_length=100, choices=(), default=u"", verbose_name=u"院校")
    professional = models.CharField(
        max_length=100, choices=(), default=u"", verbose_name=u"专业")
    work_experience = models.CharField(
        max_length=100, choices=(), default=u"", verbose_name=u"海外工作/学习经历")

    class Mate:
        verbose_name = u'教育信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.username, self.graduate_school)


class MajorClass(models.Model):
    name = models.CharField(max_length=16, verbose_name=u"类别名称")
    weight = models.IntegerField(default=1, verbose_name=u"权重")
    status = models.IntegerField(
        choices=((1, u"有效"), (0, u"无效")), default=1, verbose_name=u"状态 1：有效 0：无效")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"最后一次更新时间")

    class Mate:
        verbose_name = u'类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MajorFirst(models.Model):
    major_class = models.ForeignKey(
        MajorClass, verbose_name=u"类别", on_delete=models.CASCADE)
    name = models.CharField(max_length=16, verbose_name=u"一级专业名称")
    weight = models.IntegerField(default=1, verbose_name=u"权重")
    status = models.IntegerField(
        choices=((1, u"有效"), (0, u"无效")), default=1, verbose_name=u"状态 1：有效 0：无效")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"最后一次更新时间")

    class Mate:
        verbose_name = u'类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MajorSecond(models.Model):
    major_first = models.ForeignKey(
        MajorFirst, verbose_name=u"一级专业", on_delete=models.CASCADE)
    name = models.CharField(max_length=16, verbose_name=u"二级专业名称")
    weight = models.IntegerField(default=1, verbose_name=u"权重")
    status = models.IntegerField(
        choices=((1, u"有效"), (0, u"无效")), default=1, verbose_name=u"状态 1：有效 0：无效")
    declare_start_time = models.DateTimeField(verbose_name=u"申报开始时间")
    declare_end_time = models.DateTimeField(verbose_name=u"申报结束时间")
    review_start_time = models.DateTimeField(verbose_name=u"评审开始时间")
    review_end_time = models.DateTimeField(verbose_name=u"评审结束时间")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"最后一次更新时间")

    class Mate:
        verbose_name = u'类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Mark(models.Model):
    """
    成绩
    """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"账号")
    # 专业认证或资质
    professional_certification_or_qualification = models.FloatField(verbose_name="专业认证或资质", default=0)
    thesis_works = models.FloatField(verbose_name="论文著作", default=0)
    national_patent = models.FloatField(verbose_name="国家专利", default=0)
    technological_innovation = models.FloatField(verbose_name="科技创新", default=0)
    skills_competition = models.FloatField(verbose_name="技能竞赛", default=0)
    honour = models.FloatField(verbose_name="荣誉奖章", default=0)
    professional = models.FloatField(verbose_name="职称/职鉴", default=0)
    edu = models.FloatField(verbose_name="教育经历", default=0)
    sum = models.FloatField(verbose_name="总成绩", default=0)

    class Mate:
        verbose_name = u'成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uid.nickname
