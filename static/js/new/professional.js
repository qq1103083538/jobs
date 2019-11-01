;
var professional = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        // 点击保存的时候提交到服务器
        $("div.professional button.save").click(function (e) {
            var button = $(this);
            var root = button.parents(".item-info");
            var describe_name = root.find(".edit input[name=describe_name]").val();
            var obtain_time = root.find(".edit input[name=obtain_time]").val();
            var level = root.find(".level  option:selected").val();
            var upload_pic_wrap = root.find(".upload_pic_wrap");
            var imgs = $(upload_pic_wrap.children(".pic-each"));
            var extra = "";
            for (var i = 0; i < imgs.length; i++) {
                var img_span = imgs[i];
                var data = $(img_span).children("span").attr("data");
                if (extra.length != 0) {
                    extra += "#@#";
                }
                extra += data;
            }

            var uid = $("#my_uid").attr("uid");
            var item_id = button.attr("item_id");
            
            $.ajax({
                url: common_ops.buildUrl("resume/update_info"),
                type: 'POST',
                data: {
                    uid: uid,
                    type: "professional",
                    describe_name: describe_name,
                    obtain_time: obtain_time,
                    level: level,
                    extra: extra,
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
    professional.init();
});