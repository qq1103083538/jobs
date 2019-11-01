;
const new_index_ops = {
    init: function () {
        this.eventBind();

    },
    commit_success: function () {
        $(".new-user-info").addClass("hidden");
        $(".new-major").removeClass("hidden");
        $(".circle-last").removeClass("step-1");
        $(".circle-last").addClass("step2");
    },
    eventBind: function () {
        const self = this;
        const btn_next_page = $(".new-resume .nextPage");
        btn_next_page.click(function () {
            if (btn_next_page.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }
            const nickname = $(".wrap_new_resume_set input[name=nickname]").val();
            const gender = $(".wrap_new_resume_set input[name=gender]:checked").val();
            const birthday = $(".wrap_new_resume_set input[name=birthday]").val();
            const enter_the_employment_time = $(".wrap_new_resume_set input[name=enter_the_employment_time]").val();
            const household_register_province = $(".wrap_new_resume_set input[name=household_register_province]").val();
            const household_register_city = $(".wrap_new_resume_set input[name=household_register_city]").val();
            const live_province = $(".wrap_new_resume_set input[name=live_province]").val();
            const live_city = $(".wrap_new_resume_set input[name=live_city]").val();
            const live_district = $(".wrap_new_resume_set input[name=live_district]").val();
            const mobile = $(".wrap_new_resume_set input[name=mobile]").val();
            const email = $(".wrap_new_resume_set input[name=email]").val();
            const work_unit = $(".wrap_new_resume_set input[name=work_unit]").val();
            const department = $(".wrap_new_resume_set input[name=department]").val();
            const marriage_status = $(".marriage_status  option:selected").val();
            const politics = $(".politics option:selected").val();
            const globetrotters = $(".globetrotters option:selected").val();
            if (nickname == undefined || nickname.length < 1) {
                common_ops.alert("请输入正确的用户名~~");
                return;
            }
            if (birthday == undefined || birthday.length < 4) {
                common_ops.alert("请输入正确的出身年月~~");
                return;
            }
            if (household_register_province == undefined || household_register_province.length < 2) {
                common_ops.alert("请输入正确的籍贯~~");
                return;
            }
            if (household_register_city == undefined || household_register_city.length < 2) {
                common_ops.alert("请输入正确的籍贯~~");
                return;
            }
            var uid = $("#my_uid").attr("uid");
            btn_next_page.addClass("disabled");
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
                    type: "user-info"
                },
                dataType: 'json',
                success: function (res) {
                    btn_next_page.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            self.commit_success();
                        }
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (data) {
                    btn_next_page.removeClass("disabled");
                }
            });
        });

        const btn_commit_major = $(".new-major .save");

        btn_commit_major.click(function () {
            const button = $(this);
            if (button.hasClass("disabled")) {
                common_ops.alert("当前专业不可申报~");
                return;
            }
            const uid = $("#my_uid").attr("uid");
            const major_second_id = button.attr("major_second_id");
            $.ajax({
                url: common_ops.buildUrl("new/add_major"),
                type: 'POST',
                data: {
                    uid: uid,
                    major_second_id:major_second_id
                },
                dataType: 'json',
                success: function (res) {
                    btn_next_page.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/resume");
                        }
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (data) {
                    btn_next_page.removeClass("disabled");
                }
            });
        });

    }
};

$(document).ready(function () {
    new_index_ops.init();
});