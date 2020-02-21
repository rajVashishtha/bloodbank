function change(){
    if( $(".login").css("display") == "block"){
        $(".navbutton button").text("Login")
        $(".design").text("Register")
    $(".login").css({'display':'none'})
    $(".signup").css({'display':'block'})
    }
    else{
        $(".design").text("Login")
        $(".navbutton button").text("Register")
        $(".signup").css({'display':'none'})
        $(".login").css({'display':'block'})
        
    }
}