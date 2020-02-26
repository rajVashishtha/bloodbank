function change(){
    if( $(".login").css("display") == "block"){
        $(".navbutton button").text("Login")
        $(".design > h2").text("Register")
    $(".login").css({'display':'none'})
    $(".signup").css({'display':'block'})
    }
    else{
        $(".navbutton button").text("Register")
        $(".design > h2").text("Login")
        $(".signup").css({'display':'none'})
        $(".login").css({'display':'block'})
        
    }
}

