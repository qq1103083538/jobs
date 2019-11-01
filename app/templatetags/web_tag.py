import datetime
import math
from django import template
from django.utils.safestring import mark_safe
from common.Helper import getFormatDate

import common.UrlManager as UrlManager

register = template.Library()


@register.simple_tag
def build_url(path):
    return UrlManager.build_url(path)


@register.simple_tag
def build_static_url(path):
    return UrlManager.build_static_url(path)


@register.simple_tag
def buildImageUrl(path):
    return UrlManager.buildImageUrl(path)


@register.simple_tag
def p_to_js_date(date):
    return getFormatDate(date, "%Y-%m-%d")

@register.simple_tag
def p_to_js_date_min(date):
    return getFormatDate(date)

@register.simple_tag
def is_commint(start_data,end_data):
    n_time = datetime.datetime.now()
    if n_time>start_data and n_time<end_data:
        return ""
    else:
        return "disabled"

def month_differ(x, y):
    """暂不考虑day, 只根据month和year计算相差月份
    Parameters
    ----------
    x, y: 两个datetime.datetime类型的变量

    Return
    ------
    differ: x, y相差的月份
    """
    month_differ = abs((x.year - y.year) * 12 + (x.month - y.month) * 1)
    return month_differ



@register.simple_tag
def date_to_now_from_year(date):
    if not date:
        return 0
    now_date = datetime.datetime.now()
    y = month_differ(date, now_date)
    return math.ceil(y / 12)
