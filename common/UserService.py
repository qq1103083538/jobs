# -*- coding: utf-8 -*-
import base64
import hashlib
import uuid


class UserService:

    @staticmethod
    def gene_auth_code(user_info=None):
        m = hashlib.md5()
        s = "%s-%s-%s-%s-%s" % (user_info.id, user_info.username, user_info.password, user_info.salt, user_info.type)
        m.update(s.encode("utf-8"))
        res = "%s#%s#%s#%s" % (m.hexdigest(), user_info.id, user_info.type,user_info.username)
        return res

    @staticmethod
    def auth_code_get_user_id(auth_code):
        s = str(auth_code).split("#")
        return s


    @staticmethod
    def gene_pwd(pwd, salt):
        m = hashlib.md5()
        s = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(s.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def gene_salt():
        return str(uuid.uuid1())
