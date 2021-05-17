$(document).ready(function(){
    $.ajax({
        url: "data.json",
        dataType: "json",
        success: function(data){
            console.log(success, data);
        },
        error: function() { alert("error loading file");}
    });
});