function change(){
    if( $(".login").css("display") == "block"){
        $(".navbutton button").text("Login")
        $(".contact2-form-title").text("Register")
    $(".login").css({'display':'none'})
    $(".signup").css({'display':'block'})
    }
    else{
        $(".contact2-form-title").text("Login")
        $(".navbutton button").text("Register")
        $(".signup").css({'display':'none'})
        $(".login").css({'display':'block'})
        
    }
}
function reset(){
    $("input").val("")
    $("input").text("")
}
