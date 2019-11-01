;
const user_login_ops = {
    init: function () {
        this.eventBind();

    },
    show_login: function () {
        this.createCode(4);
        const login_wrap = $(".login_wrap");
        const register_wrap = $(".register_wrap");
        const admin_login_wrap = $(".admin_login_wrap");
        login_wrap.removeClass("hide");
        register_wrap.addClass("hide");
        admin_login_wrap.addClass("hide");
    },
    show_register: function () {
        this.createCode(4);
        const login_wrap = $(".login_wrap");
        const register_wrap = $(".register_wrap");
        // login_wrap.fadeOut();
        // register_wrap.fadeIn();
        login_wrap.addClass("hide");
        register_wrap.removeClass("hide");
    },
    show_admin_login: function () {
        const login_wrap = $(".login_wrap");
        const admin_login_wrap = $(".admin_login_wrap");
        login_wrap.addClass("hide");
        admin_login_wrap.removeClass("hide");
    },
    createCode: function (length) {
        //生成验证码的方法
        let code = "";
        const codeLength = parseInt(length); //验证码的长度
        const checkCode = $("#verification_code");
        ////所有候选组成验证码的字符，当然也可以用中文的
        const codeChars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
        //循环组成验证码的字符串
        for (let i = 0; i < codeLength; i++) {
            //获取随机验证码下标
            const charNum = Math.floor(Math.random() * 62);
            //组合成指定字符验证码
            code += codeChars[charNum];
        }
        checkCode.addClass("verification_code");
        checkCode.html(code);
    },
    //检查验证码是否正确
    validateCode: function () {
        //获取显示区生成的验证码
        // var checkCode = document.getElementById("checkCode").innerHTML;
        // //获取输入的验证码
        // var inputCode = document.getElementById("inputCode").value;

        const input_verification_code = $("#input_verification_code");
        const verification_code = $("#verification_code");
        const checkCode = verification_code.text();
        const inputCode = input_verification_code.val();
        if (inputCode.length <= 0) {
            return false;
        } else if (inputCode.toUpperCase() != checkCode.toUpperCase()) {
            this.createCode(4);
            return false;
        } else {
            // alert("验证码正确！");
            return true;
        }
    },

    eventBind: function () {
        const self = this;
        const btn_do_login = $(".login_wrap .do-login");
        const btn_just_register = $(".login_wrap .do-just-register");
        const btn_do_register = $(".register_wrap .do-register");
        const btn_just_login = $(".register_wrap .do-black");
        const btn_admin_just_login = $(".admin_login_wrap .do-black");
        const btn_just_admin_login = $(".login_wrap .do-admin-login");

        const btn_do_admin_login = $(".admin_login_wrap .do-login");

        btn_do_admin_login.click(function () {
            if (btn_do_admin_login.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            const login_name = $(".admin_login_wrap input[name=login_name]").val();
            const login_pwd = $(".admin_login_wrap input[name=login_pwd]").val();

            if (login_name == undefined || login_name.length < 4) {
                common_ops.alert("请输入正确的登录用户名~~");
                return;
            }
            if (login_pwd == undefined || login_pwd.length < 4) {
                common_ops.alert("请输入正确的密码~~");
                return;
            }
            btn_do_admin_login.addClass("disabled");
            var is_admin = $(".login_wrap").hasClass("hide");
            $.ajax({
                url: common_ops.buildUrl("/user/login"),
                type: 'POST',
                data: {'login_name': login_name, 'login_pwd': login_pwd, 'login_type': is_admin ? 2 : 1},
                dataType: 'json',
                success: function (res) {
                    btn_do_admin_login.removeClass("disabled");
                    var callback = null;

                    if (res.code == 200) {
                        var data = res.data;
                        var path = data.path;
                        callback = function () {
                            window.location.href = common_ops.buildUrl(path);
                        }
                    } else {
                        callback = null;
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (error) {
                    const callback = function () {
                        btn_do_admin_login.removeClass("disabled");
                    };

                    common_ops.alert("网络失败～ 请求状态码:" + error.status, callback);
                }
            });
        });


        btn_do_login.click(function () {
            if (btn_do_login.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            const login_name = $(".login_wrap input[name=login_name]").val();
            const login_pwd = $(".login_wrap input[name=login_pwd]").val();

            if (login_name == undefined || login_name.length < 4) {
                common_ops.alert("请输入正确的登录用户名~~");
                return;
            }
            if (login_pwd == undefined || login_pwd.length < 4) {
                common_ops.alert("请输入正确的密码~~");
                return;
            }
            btn_do_login.addClass("disabled");
            btn_just_register.addClass("disable");
            var is_admin = $(".login_wrap").hasClass("hide");
            $.ajax({
                url: common_ops.buildUrl("/user/login"),
                type: 'POST',
                data: {'login_name': login_name, 'login_pwd': login_pwd, 'login_type': is_admin ? 2 : 1},
                dataType: 'json',
                success: function (res) {
                    btn_do_login.removeClass("disabled");
                    btn_just_register.removeClass("disable");
                    var callback = null;

                    if (res.code == 200) {
                        var data = res.data;
                        var path = data.path;
                        callback = function () {
                            window.location.href = common_ops.buildUrl(path);
                        }
                    } else {
                        callback = null;
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (error) {
                    const callback = function () {
                        btn_do_login.removeClass("disabled");
                        btn_just_register.removeClass("disable");
                    };

                    common_ops.alert("网络失败～ 请求状态码:" + error.status, callback);
                }
            });
        });

        btn_just_register.click(function () {
            if (btn_just_register.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要切换~~");
                return;
            }
            self.show_register();
        });
        btn_just_admin_login.click(function () {
            if (btn_just_admin_login.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要切换~~");
                return;
            }
            self.show_admin_login();
        });

        btn_do_register.click(function () {
            if (btn_do_register.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            const login_name = $(".register_wrap input[name=login_name]").val();
            const login_pwd = $(".register_wrap input[name=login_pwd]").val();
            const confirm_login_pwd = $(".register_wrap input[name=confirm_login_pwd]").val();

            if (login_name == undefined || login_name.length < 4) {
                common_ops.alert("请输入正确的用户名~~");
                return;
            }
            if (login_pwd == undefined || login_pwd.length < 4) {
                common_ops.alert("请输入正确的密码~~");
                return;
            }
            if (confirm_login_pwd == undefined || confirm_login_pwd.length < 4) {
                common_ops.alert("请输入正确的密码~~");
                return;
            }

            if (login_pwd != confirm_login_pwd) {
                common_ops.alert("两次输入的密码不一致~~");
                return;
            }
            if (!self.validateCode()) {
                common_ops.alert("验证码错误~~");
                return;
            }
            btn_do_register.addClass("disabled");
            btn_just_login.addClass("disable");
            $.ajax({
                url: common_ops.buildUrl("/user/register"),
                type: 'POST',
                data: {'login_name': login_name, 'login_pwd': login_pwd},
                dataType: 'json',
                success: function (res) {
                    btn_do_register.removeClass("disabled");
                    btn_just_login.removeClass("disable");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            // window.location.href = common_ops.buildUrl("/");
                            self.show_login();
                            $(".login_wrap input[name=login_name]").val(login_name);
                            $(".login_wrap input[name=login_pwd]").val(login_pwd);
                        }
                    } else {
                        callback = null;
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (error) {
                    const callback = function () {
                        btn_do_register.removeClass("disabled");
                        btn_just_login.removeClass("disable");
                    };

                    common_ops.alert("网络失败～ 请求状态码:" + error.status, callback);
                }
            });

        });
        btn_just_login.click(function () {
            if (btn_just_login.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要切换~~");
                return;
            }
            self.show_login();
        });
        btn_admin_just_login.click(function () {
            if (btn_admin_just_login.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要切换~~");
                return;
            }
            self.show_login();
        });
        $("#verification_code").click(function () {
            self.createCode(4);
        });
    }
};

$(document).ready(function () {
    user_login_ops.init();
});