$(document).ready(function() {
    $("input").attr("min","0");

    $("#btn_update").click(function() {
      $(".myinput").prop("disabled", false);
    });
    $("#btn_save").click(function() {
       var field = document.getElementsByClassName("myinput")
       for(var i=0;i<field.length;i++){
           var temp = field[i].value;
           temp = Number(temp)
           if(temp <0){
               temp = Math.abs(temp)
               field[i].value = temp
           }
       }



      $(".myinput").prop("disabled", true);
    });
  });
  