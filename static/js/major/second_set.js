;
var food_cat_set_ops = {
        init: function () {
            this.eventBind();
        },
        eventBind: function () {
            $('#datetimepicker1').datetimepicker();
            $('#datetimepicker2').datetimepicker();
            $('#datetimepicker3').datetimepicker();
            $('#datetimepicker4').datetimepicker();
            $(".wrap_second_set .save").click(function () {
                var btn_target = $(this);
                if (btn_target.hasClass("disabled")) {
                    common_ops.alert("正在处理!!请不要重复提交~~");
                    return;
                }

                var first_id_target = $(".wrap_second_set select[name=first_id]");
                var first_id = first_id_target.val();

                var name_target = $(".wrap_second_set input[name=second_name]");
                var name = name_target.val();


                var declare_start_target = $(".wrap_second_set input[name=declare_start]");
                var declare_start = declare_start_target.val();


                var declare_end_target = $(".wrap_second_set input[name=declare_end]");
                var declare_end = declare_end_target.val();


                var review_start_target = $(".wrap_second_set input[name=review_start]");
                var review_start = review_start_target.val();

                var review_end_target = $(".wrap_second_set input[name=review_end]");
                var review_end = review_end_target.val();

                var weight_target = $(".wrap_second_set input[name=weight]");
                var weight = weight_target.val();



                if (first_id < 1) {
                    common_ops.tip("请选择分类", first_id_target);
                    return false;
                }

                if (name.length < 1) {
                    common_ops.tip("请输入符合规范的二级专业名称名称~~", name_target);
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
                    first_id: first_id,
                    id: $(".wrap_second_set input[name=id]").val(),
                    declare_start: declare_start,
                    declare_end: declare_end,
                    review_start: review_start,
                    review_end: review_end
                };

                $.ajax({
                    url: common_ops.buildUrl("/cms/major/second-set"),
                    type: 'POST',
                    data: data,
                    dataType: 'json',
                    success: function (res) {
                        btn_target.removeClass("disabled");
                        var callback = null;
                        if (res.code == 200) {
                            callback = function () {
                                window.location.href = common_ops.buildUrl("/cms/major/second");
                            }
                        }
                        common_ops.alert(res.msg, callback);
                    }
                });


            });
        }
    }
;

$(document).ready(function () {
    food_cat_set_ops.init();
});