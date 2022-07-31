window.onload = function () {
    $('.table-responsive').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
            $.ajax({
            url: "/cart/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
            $('.table-responsive').html(data.result);
            },
        });
        event.preventDefault();
    });
}