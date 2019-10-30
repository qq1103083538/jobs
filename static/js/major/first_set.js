;
var food_cat_set_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".wrap_first_set .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var major_id_target = $(".wrap_first_set select[name=major_id]");
            var major_id = major_id_target.val();

            var name_target = $(".wrap_first_set input[name=first_name]");
            var name = name_target.val();

            var weight_target = $(".wrap_first_set input[name=weight]");
            var weight = weight_target.val();

            if (major_id < 1) {
                common_ops.tip("请选择分类", major_id_target);
                return false;
            }

            if (name.length < 1) {
                common_ops.tip("请输入符合规范的一级专业名称名称~~", name_target);
                return false;
            }

            if (parseInt(weight) < 1) {
                common_ops.tip("请输入符合规范的权重，并且至少要大于1~~", weight_target);
                return false;
            }

            btn_target.addClass("disabled");

            var data = {
                name: name,
                weight: weight,
                major_id: major_id,
                id: $(".wrap_first_set input[name=id]").val()
            };

            $.ajax({
                url: common_ops.buildUrl("/cms/major/first-set"),
                type: 'POST',
                data: data,
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/cms/major/first");
                        }
                    }
                    common_ops.alert(res.msg, callback);
                }
            });


        });
    }
};

$(document).ready(function () {
    food_cat_set_ops.init();
});