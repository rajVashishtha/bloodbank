$(document).ready(function() {
 
setData(); // applaying data

$("input").attr("min","0");

    $("#btn_update").click(function() {
      $(".myinput").prop("disabled", false);
      $("#btn_save").css({'display':'inline'})
      $("#btn_update").css({'display':'none'})
    });

    $("#btn_save").click(function(){
       var field = document.getElementsByClassName("myinput")
       for(var i=0;i<field.length;i++){
           var temp = field[i].value;
           temp = Number(temp)
           if(temp <0){
               temp = Math.abs(temp)
               field[i].value = temp
           }
       }
       //to update data with real data
      /*
      setdata()  //to call ajax
       */




      $(".myinput").prop("disabled", true);
      $("#btn_update").css({'display':'inline'});
      $("#btn_save").css({'display':'none'});

    });

    function applyData(){
        var groups = ["A-","A+","B-","B+","AB-","AB+","O-","O+"]
 var first_set = `<tr>
 <td scope='col'>`;
 var second_set = `</td>
 <td scope='col'>
   <input disabled value='`
 var third_set=`' class='myinput' type='number' />
 </td>
 <td scope='col'>
   <input disabled value='`
  var forth_set =`' class='myinput' type='number' />
 </td>
 <td scope='col'>
   <input disabled value='`
  var fifth_set =`' class='myinput' type='number' />
 </td>
 <td scope='col'>
   <input disabled value='`
   var sixth_set = `' class='myinput' type='number' />
 </td>
 <td scope='col'>
   <input disabled value='`
   var seventh_set = `' class='myinput' type='number' />
 </td>
 <td scope='col'>
   <input disabled value='`
  var eighth_set=`' class='myinput' type='number' />
 </td>
</tr>`;
for(var i=0;i<groups.length;i++){
  $("#my_tbody").append(first_set+groups[i]+second_set+(i+1)+third_set+(i+2)+forth_set+(i+3)+fifth_set+(i+4)+sixth_set+(i+5)+seventh_set+(i+6)+eighth_set);

}
    }


   function setData(){
       //make ajax call here
    applyData();

   } 

});
  
// REMEMBER YOU HAVE TO CALL TO API METHODS :-
// 1. AT TIME OF PAGE LOAD
// 2. AT TIME OF DATA UPDATE