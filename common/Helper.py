import datetime

from django.shortcuts import render

import jobs.settings as settings


def ops_render(request, template_name, context=None, content_type=None, status=None, using=None):
    """
    统一渲染方法
    """
    if not context:
        context = {}
    if hasattr(request, 'myself'):
        myself = request.myself
        context['that'] = myself
    context['config'] = settings
    response = render(request=request, template_name=template_name,
                      context=context, content_type=content_type, status=status, using=using)
    return response


def get_current_date(format="%Y-%m-%d %H:%M:%S"):
    '''
    获取当前时间
    '''
    return datetime.datetime.now(format=format)


def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
    '''
    获取格式化的时间
    '''
    if date is None:
        date = datetime.datetime.now()
    return date.strftime(format)


def get_date_form_str(detester="", format="%y-%m-%s"):
    return datetime.datetime.strptime(detester, format)
