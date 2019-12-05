$(document).ready(function(){
    $(".project").hide();
    $(".croseover").hover(function(){
        $(this).find(".project").toggle(400);
    });

    $(".click0").click(function(){
        $(".hide0").slideToggle(500);
        $(".show0").slideToggle(1200);
    });

    $(".click1").click(function(){
        $(".hide1").slideToggle(100);
        $(".show1").slideToggle(1200);
    });
    
    $(".click2").click(function(){
        $(".hide2").slideToggle(500);
        $(".show2").slideToggle(1200);
    }); 

    $("button").click(function() {
        var user = document.getElementById("names").Value;
        alert('Thank you'  +  'we have recieved your comment successfully' + '!');
        // party.preventDefault();
    });

});