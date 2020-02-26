$(document).ready(function() {
    // alert("hello")
    // var names = document.getElementsByTagName("input");
    // for(var i=0;i<names.length;i++){
    //     names[i].setAttribute("name","name")
    // }

    // var groups = ["A-","A+","B-","B+","AB-","AB+","O-","O+"];
    // var i=0,j=0;
    //  for(i=0;i<groups.length;i++){
    //    var temp1 = `<tr id="tr-${i}"></tr>`
    //    $("#tbody").append(temp1);
    //     $("#tr-"+i).append("<td scope='col'>"+groups[i]+"</td>")
    //     for(j=0;j<5;j++){
    //       var name = createName(i,j);
    //       var temp = `<td scope='col'>
    //       <input disabled value='${generateValue(i,j)}' class='myinput' name='${name}' type='number' />
    //       </td>`;
    //       $("#tr-"+i).append(temp)
    //     }
    //  }
    $("input").attr("min","0");

    $("#btn_update").click(function(event) {
      event.preventDefault();
      $(".myinput").prop("disabled", false);
      $("#btn_update").css({'display':'none'})
      $("#save_btn").css({'display':'inline'})
    });
  
  });

  function createName(i,j){
    var first = i.toString();
    var second = j.toString();
    return first+second;
  }
  function generateValue(i,j){
    return i*j
  }
  