from django.shortcuts import render
from common.Helper import ops_render, get_date_form_str, getFormatDate, get_current_date
from django.http import JsonResponse, HttpResponse

from .models import User, MajorClass, MajorFirst, MajorSecond
from common.UserService import UserService

import time
import os


def pic(request):
    response = {'code': 200, 'msg': "上传成功", "data": {}}
    try:
        my_file = request.FILES.get("pic", None)
        uid = request.POST.get("uid", "0")
        file_name = my_file.name
        new_file_name = "%s_%s_%s" % (uid, int(time.time()), file_name)
        path = "/upload/img/%s" % new_file_name
        save_path = "./static" + path
        # save_path = os.path.join("./static", path)
        destination = open(save_path, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in my_file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        data = {"path": path, "data": request.POST.get("data", "")}
        response["data"] = data
        return JsonResponse(response)
    except Exception as e:
        response["code"] = -1
        response["msg"] = str(e)
        return JsonResponse(response)
