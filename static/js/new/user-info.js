;
var user_info_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
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
            var head = root.find('.profile-edit-crop img').src;
            var uid = button.attr("m_uid");
            $.ajax({
                url: common_ops.buildUrl("/"),
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
                    head: head
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
    }
};

$(document).ready(function () {
    user_info_ops.init();
});