$(document).ready(function() {
    vars = get_url_vars();
    if (typeof(vars["offset"]) == "undefined"){
        vars["offset"] = 0
    }else{
        vars["offset"] = parseInt(vars["offset"])
    }
    if (typeof(vars["limit"]) == "undefined"){
        vars["limit"] = 10
    }else{
        vars["limit"] = parseInt(vars["limit"])
    }
    $("table tbody").empty();
    get_users(function (data) {
        check_return(data);
        var data=data["data"];
        $.each(data["users"], function(i, n) {
            var tr = $("<tr></tr>");
            tr.append($("<td></td>").text(n["name"]));
            var action = $("<td></td>");
            action.append($("<a href=\"/users/"+n["id"].toString()+"/hosts\">主机</a>"));
            action.append($("<span class=\"cut-line\">&nbsp;¦&nbsp;</span>"));
            action.append($("<a href=\"/users/"+n["id"].toString()+"/projects\">项目</a>"));
            tr.append(action);
            $("table tbody").append(tr);
        });
        $(".pagination").empty();
        for(var i=1, offset=0; offset < data["count"]; i++){
            $(".pagination").append($("<li><a href=\"/users?offset="+offset+"&limit="+vars["limit"]+"\">"+i.toString()+"</a></li>"));
            offset += vars["limit"];
        }
    }, vars["offset"], vars["limit"]);
})
