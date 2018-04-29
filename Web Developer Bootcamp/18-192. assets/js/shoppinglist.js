$("ul").on('click', 'li', function () {
    $(this).toggleClass("completed");
});

$("ul").on('click', 'span', function (event) {
    event.stopPropagation();
    $(this).parent().fadeOut(500, function () {
        $(this).remove();
    });
});
$("input[type='text']").keypress(function (event) {
    console
    if (event.which === 13) {
        var shopitem = $(this).val();
        $(this).val("");
        $("ul").append("<li><span><i class='fa fa-trash'></i></span> " + shopitem + "</li>");
    };
});
$(".fa-plus").on('click', function () {
    $("input[type='text']").fadeToggle();
})