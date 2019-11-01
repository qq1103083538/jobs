;
var food_cat_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;

        $(".wrap_search select[name=c]").change(function () {
            $(".wrap_search").submit();
        });
        $(".wrap_search select[name=f]").change(function () {
            $(".wrap_search").submit();
        });
        $(".wrap_search select[name=s]").change(function () {
            $(".wrap_search").submit();
        });
        $(".wrap_search select[name=sort]").change(function () {
            $(".wrap_search").submit();
        });
    }

};

$(document).ready(function () {
    food_cat_ops.init();
});