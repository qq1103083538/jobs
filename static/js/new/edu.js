;
var edu_opt = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        // 点击保存的时候提交到服务器
        $("div.edu button.save").click(function (e) {
            var button = $(this);
            var root = button.parents(".item-info");
            var name = root.find(".edit input[name=name]").val();
            var graduate_start_time = root.find(".edit input[name=graduate_start_time]").val();
            var graduate_end_time = root.find(".edit input[name=graduate_end_time]").val();
            var major = root.find(".edit input[name=major]").val();
            var colleges = root.find(".edit input[name=colleges]").val();
            var education = root.find(".education  option:selected").val();
            var degree = root.find(".degree  option:selected").val();

            var uid = $("#my_uid").attr("uid");
            var item_id = button.attr("item_id");

            $.ajax({
                url: common_ops.buildUrl("resume/update_info"),
                type: 'POST',
                data: {
                    uid: uid,
                    type: "edu",
                    name: name,
                    graduate_start_time: graduate_start_time,
                    graduate_end_time: graduate_end_time,
                    major: major,
                    colleges: colleges,
                    education: education,
                    degree: degree,
                    item_id: item_id
                },
                dataType: 'json',
                success: function (res) {
                    button.removeClass("disable");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert(res.msg, callback);
                },
                error: function (data) {
                    button.removeClass("disable");
                }
            });
        });
    }
};

$(document).ready(function () {
    edu_opt.init();
});