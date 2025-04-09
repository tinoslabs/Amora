$(function(){
    // Load the style-switcher.css with static tag
    $('head').append('<link rel="stylesheet" href="{% static "assets/css/colors/style-switcher.css" %}" type="text/css" />');
    
    // Style container
    var switcher = $('<div class="switcher"><span class="switch"><i class="fas fa-cog fa-spin"></i></span><h4>Color Options</h4><hr><div class="s-color"><a href="#" data-code="default"></a><a href="#" data-code="color-1"></a><a href="#" data-code="color-2"></a><a href="#" data-code="color-3"></a><a href="#" data-code="color-4"></a><a href="#" data-code="color-5"></a></div><div class="layout-btn-group"><ul><li><button id="box-layout">Box width</button></li><li><button id="full-width">full width</button></li></ul></div></div>');
    
    $('body').append(switcher);
    
    // Display after some time 
    $(".switcher .switch-h").delay("1500").fadeIn(3000);
    
    setTimeout(function(){ $('.switcher .switch-h').fadeOut() }, 10000);	

    $('.switch').click(function() {
        var $slidebox=$('.switcher');
        if($slidebox.css('left')=="-251px"){
            $slidebox.animate({left:0},300);
        }
        else{
            $slidebox.animate({left:-251},300);
        }
    });   

    // Box layout toggle
    $("#box-layout").bind("click", function() {
        $("body").addClass('box-layout');
    });
    $("#full-width").bind("click", function() {
        $("body").removeClass('box-layout');
    });
    
    // Color Changer - Updated with static path
    $('.s-color a').click(function(e){
        e.preventDefault();
        var color_code = $(this).attr('data-code');
        var colorPath = "{% static 'assets/css/colors/" + color_code + ".css' %}";
        $('link[id="color_theme"]').attr('href', colorPath);
    });
});