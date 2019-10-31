;

var upload = {
    error: function (msg) {
        common_ops.alert(msg);
    },
    success: function (response) {
        var data = response.data;
        // console.log(data.data.data);
        // $.parseJSON()
        var object_data = JSON.parse(data.data);
        // var html = '<img src="./static/' + common_ops.buildPicUrl(file_key) + '"/>'
        //     + '<span class="fa fa-times-circle del del_image" data="' + file_key + '"></span>';
        var target_id = object_data.target_id;

        var html = '<img src="./static' + data.path + '"/>'
            + '<span class="fa fa-times-circle del del_image" data="' + data.path + '"></span>';
        // if ($(" .pic-each").size() > 0) {
        //     $(".upload_pic_wrap .pic-each").html(html);
        // } else {
        //     $(".upload_pic_wrap").append('<span class="pic-each">' + html + '</span>');
        // }
        $("#" + target_id).append('<span class="pic-each">' + html + '</span>');
        new_resume_ops.delete_img();
    }
};

var new_resume_ops = {
    init: function () {
        this.eventBind();
        this.delete_img();
    },
    eventBind: function () {
        var that = this;
        $(".upload_pic_wrap input[name=pic]").change(function () {
            var file_obj = this.files[0];
            var fd = new FormData();
            var uid = $("#my_uid").attr("uid");
            var data = {"target_id": $(this).attr('target_id')};
            fd.append('username', 'root');
            fd.append('pic', file_obj);
            fd.append('uid', uid);
            fd.append("data", JSON.stringify(data));
            $.ajax({
                url: '/upload/pic',
                type: 'POST',
                data: fd,
                processData: false,  //tell jQuery not to process the data
                contentType: false,  //tell jQuery not to set contentType
                //这儿的三个参数其实就是XMLHttpRequest里面带的信息。
                success: function (arg, a1, a2) {
                    upload.success(arg, a1, a2);
                }

            })
        });

        $("div.item-info div.header a.btn").click(function () {
            var button = $(this);
            //获取点击的root原素
            var root = button.parents(".item-info");
            // 获取edit编辑原素
            var edit = root.children(".edit");
            // 如果edit原素是显示的，那么后面无需操作
            if (!edit.hasClass("hidden")) {
                return;
            }
            // 获取当前展示的列表
            var list = root.children(".edu-list");
            list.addClass("hidden");
            edit.find(".describe_name").val("");
            edit.find(".obtain_time").val("");
            edit.find(".level").find("option[value='-1']").attr("selected", true);
            var upload_pic_wrap = edit.find(".upload_pic_wrap");
            var def_images = upload_pic_wrap.find(".del_image");
            for (var i = 0; i < def_images.length; i++) {
                var children_image = def_images[i];
                $(children_image).parent().remove();
            }
            edit.removeClass("hidden");
        });
        $(".edit .cancel").click(function () {
            var root = $(this).parents(".item-info");
            root.find(".edu-list").removeClass("hidden");
            root.find(".edit").addClass("hidden");
        });
        $("div.item-info .edu-list").mouseover(function () {
            $(this).find(".btn-edit").removeClass("hidden");
        });
        $("div.item-info .edu-list").mouseout(function () {
            if(!$(".edit").hasClass("hidden")){
                return;
            }
            $(this).find(".btn-edit").addClass("hidden");
        });
        $("div.edu-list label.btn-edit").click(function () {
            var button = $(this);
            var root = button.parents(".item-info");
            // 获取edit编辑原素
            var edit = root.children(".edit");
            // 如果edit原素是显示的，那么后面无需操作
            if (!edit.hasClass("hidden")) {
                return;
            }

            // 获取当前展示的列表
            var list = button.parents(".edu-list");
            var m_name = list.attr("m_name");
            var item_id = list.attr("item_id");
            var m_obtion_time = list.attr("m_obtion_time");
            var m_level = list.attr("m_level");
            var m_img = list.attr("m_img");
            edit.find(".describe_name").val(m_name);
            edit.find(".obtain_time").val(m_obtion_time);
            edit.find(".level").find("option[value='" + m_level + "']").attr("selected", true);
            var upload_pic_wrap = edit.find(".upload_pic_wrap");
            var def_images = upload_pic_wrap.find(".del_image");
            for (var i = 0; i < def_images.length; i++) {
                var children_image = def_images[i];
                $(children_image).parent().remove();
            }
            var imgs = m_img.split("#@#");
            for (var i = 0; i < imgs.length; i++) {
                var html = '<img src="/static' + imgs[i] + '"/>'
                    + '<span class="fa fa-times-circle del del_image" data="' + imgs[i] + '"></span>';
                // if ($(" .pic-each").size() > 0) {
                //     $(".upload_pic_wrap .pic-each").html(html);
                // } else {
                //     $(".upload_pic_wrap").append('<span class="pic-each">' + html + '</span>');
                // }
                upload_pic_wrap.append('<span class="pic-each">' + html + '</span>');
            }
            console.log("~~~~~~~");
            console.log(item_id);
            var save_button = root.find("button.save");
            save_button.attr("item_id",item_id);
            edit.removeClass("hidden");
        });
    },
    delete_img: function () {
        $(".del_image").unbind().click(function () {
            $(this).parent().remove();

        });
    }
};
$(document).ready(function () {
    new_resume_ops.init();
});