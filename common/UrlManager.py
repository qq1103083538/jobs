from jobs.settings import *
import time


def build_url(path):
    return path


def build_static_url(path):
    # debug 版本通过时间撮来刷新静态文件，避免浏览器缓存
    if DEBUG:
        ver = "%s" % (int(time.time()))
    else:
        ver = RELEASE_VERSION if not RELEASE_VERSION else ""
    path = "/static" + path + "?ver=" + ver
    return build_url(path)


def buildImageUrl(path):
    return path
