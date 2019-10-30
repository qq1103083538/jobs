;
var user_info_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        //点击编辑的时候显示编辑框，同时因此显示信息
        $("div.user-info div.edit").click(function () {
            var root = $(this).parents(".user-info");
            root.children(".edit-form").removeClass("hidden");
            root.children(".edu-list").addClass("hidden");
        });
        //点击取消的时候
        $("div.user-info button.cancel").click(function () {
            var root = $(this).parents(".user-info");
            root.children(".edit-form").addClass("hidden");
            root.children(".edu-list").removeClass("hidden");
        });
        // 点击保存的时候提交到服务器
        $("div.user-info button.save").click(function () {
            var button = $(this);
            var root = button.parents(".user-info");
            var nickname = root.find(".profile-edit-form input[name=first_name]").val();
            var gender = root.find(".profile-edit-form input[name=gender]:checked").val();
            var birthday = root.find(".profile-edit-form input[name=birthday]").val();
            var enter_the_employment_time = root.find(".profile-edit-form input[name=enter_the_employment_time]").val();
            var household_register_province = root.find(".profile-edit-form input[name=household_register_province]").val();
            var household_register_city = root.find(".profile-edit-form input[name=household_register_city]").val();
            var live_province = root.find(".profile-edit-form input[name=live_province]").val();
            var live_city = root.find(".profile-edit-form input[name=live_city]").val();
            var live_district = root.find(".profile-edit-form input[name=live_district]").val();
            var mobile = root.find(".profile-edit-form input[name=mobile]").val();
            var email = root.find(".profile-edit-form input[name=email]").val();
            var work_unit = root.find(".profile-edit-form input[name=work_unit]").val();
            var department = root.find(".profile-edit-form input[name=department]").val();
            var marriage_status = root.find(".marriage_status option:selected").val();
            var politics = root.find(".politics option:selected").val();
            var globetrotters = root.find(".globetrotters option:selected").val();
            var portrait = $(root.find('.profile-edit-crop img')[0]).attr("m_src");
            var uid = $("#my_uid").attr("uid");
            $.ajax({
                url: common_ops.buildUrl("resume/update_info"),
                type: 'POST',
                data: {
                    uid: uid,
                    nickname: nickname,
                    gender: gender,
                    birthday: birthday,
                    enter_the_employment_time: enter_the_employment_time,
                    household_register_province: household_register_province,
                    household_register_city: household_register_city,
                    live_province: live_province,
                    live_city: live_city,
                    live_district: live_district,
                    mobile: mobile,
                    email: email,
                    work_unit: work_unit,
                    department: department,
                    marriage_status: marriage_status,
                    politics: politics,
                    globetrotters: globetrotters,
                    portrait: portrait,
                    type: "user-info"
                },
                dataType: 'json',
                success: function (res) {
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (data) {

                }
            });
        });
        // 监听图片上传
        $(".upload_pic_wrap_user_info input[name=pic]").change(function () {
            var self = $(this);
            var file_obj = this.files[0];
            var fd = new FormData();
            var uid = $("#my_uid").attr("uid");
            fd.append('username', 'root');
            fd.append('pic', file_obj);
            fd.append('uid', uid);
            fd.append("data", "");
            $.ajax({
                url: '/upload/pic',
                type: 'POST',
                data: fd,
                processData: false,  //tell jQuery not to process the data
                contentType: false,  //tell jQuery not to set contentType
                //这儿的三个参数其实就是XMLHttpRequest里面带的信息。
                success: function (response, a1, a2) {
                    var data = response.data;
                    // data.path
                    self.parent().find(".profile-edit-crop-image").attr('src', "./static/" + data.path);
                    self.parent().find(".profile-edit-crop-image").attr('m_src', data.path);
                },
                error: function () {
                    common_ops.alert("上传失败");
                }

            })
        });
    }
};

$(document).ready(function () {
    user_info_ops.init();
});