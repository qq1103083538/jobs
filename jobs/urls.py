"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import app.views as view
import app.upload as upload

app_name = "app"
user_patterns = [
    path('register', view.register),
    path('login', view.login),
]
cms_patterns = [
    path('', view.admin_users),
    path('set/', view.admin_set),
    path('info/', view.admin_info),
    path('ops/', view.admin_ops),
    path('major/class', view.major_class),
    path('major/class-set', view.major_class_set),
    path('major/class-ops', view.major_class_ops),
    path('major/first', view.major_first),
    path('major/first-set', view.major_first_set),
    path('major/first-ops', view.major_first_ops),
    path('major/', view.major_second),
    path('major/second', view.major_second),
    path('major/second-set', view.major_second_set),
    path('major/second-ops', view.major_second_ops),
    path('user/', view.user),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name="index"),
    path('user/', include(user_patterns)),
    path('cms/', include(cms_patterns)),
    path('new', view.new),
    path('new/add_major', view.add_major),
    path('resume', view.resume),
    path('resume/update_info', view.resume_update),
    path('upload/pic', upload.pic),
]
