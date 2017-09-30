$(document).ready(function() {

    //全选和反选
    $("#SelectAll").click( 
        function(){ 
            if(this.checked){ 
                $("input[name='checkbox']").each(function(){this.checked=true;}); 
            }else{ 
                $("input[name='checkbox']").each(function(){this.checked=false;}); 
            } 
    });
})
