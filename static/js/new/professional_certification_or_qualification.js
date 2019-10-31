;
var professional_certification_or_qualification_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        // 点击保存的时候提交到服务器
        $("div.Professional_certification_or_qualification button.save").click(function (e) {
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
                    type: "professional_certification_or_qualification",
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
    professional_certification_or_qualification_ops.init();
});