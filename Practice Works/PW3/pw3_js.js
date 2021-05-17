$(document).ready(function () {
    $("#todotext").hide();

    $("#todotext").on("focus", function () {
        $(this).addClass("input-border");
    });

    $("#todotext").on("blur", function () {
        $(this).removeClass("input-border");
    });

    $("#add-button").click(function () {
        $("#todotext").toggle();
    });

    $("#todotext").keypress(function () {

        if (event.which === 13) {
            if (!$(this).val()) {
                alert("You can't create blank item in ToDo list!");
                return;
            }
            $("ul").append("<li><button class='deleteButton btn btn-dark'><i class='fa fa-trash-o fa-lg'></i></button><span class='list-text'>" + $(this).val() + "</span></li>");
            $(this).val("");
        }
    });

    $("ul").on("mouseenter", "li", function () {
        $(this).find(".deleteButton").show();
    });

    $("ul").on("mouseleave", "li", function() {
        $(this).find(".deleteButton").hide();
    });

    $("ul").on("click", ".deleteButton", function(){
        $(this).closest("li").remove();
    });

    $("ul").on("click", "li", function(){
        $(this).toggleClass("striketext");
    });
});