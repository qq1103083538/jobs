try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, redirect
from app.models import User


class MyAuthInterceptorMiddle(MiddlewareMixin):
    # 在视图执行前调用
    def process_request(self, request):
        path = str(request.path)
        if path.startswith("/user/") or path == "/":
            pass
        else:
            jobs = request.COOKIES.get("jobs", "")
            if not jobs:
                redirect("/")
            else:
                try:
                    infos = str(jobs).split("#")
                    if len(infos) < 3:
                        raise Exception()

                    users = User.objects.filter(id=infos[1])
                    if not users:
                        redirect("/")
                    else:
                        request.myself = users[0]
                except Exception as e:
                    # redirect(reverse('index'))

                    return HttpResponseRedirect("/")

    def process_response(self, request, response):
        return response
