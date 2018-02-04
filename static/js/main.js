$(document).ready(function(){
    $("#ssp").change(function(){
        if ($(this).val() == "1"){
        	$('#h-ssp').removeClass('hidden');
        }
        else{
        	$('#h-ssp').addClass('hidden');
        }
    });
    $("#sib").change(function(){
        if ($(this).val() == "1"){
        	$('#h-sib').removeClass('hidden');
        }
        else{
        	$('#h-sib').addClass('hidden');
        }
    });
    $("#seb").change(function(){
        if ($(this).val() == "1"){
        	$('#h-seb').removeClass('hidden');
        }
        else{
        	$('#h-seb').addClass('hidden');
        }
    });
    $('#ssp-search').keyup(function(){
    	val = $(this).val().toLowerCase();
    	$(".ssp_inputs").each(function(){
    		if($(this).text().toLowerCase().indexOf(val) > -1){
    		 	$(this).parent().removeClass('hidden');
    		}
    		else{
    			$(this).parent().addClass('hidden');
    		}
    	});
    });
    $('#ssp-all').change(function(){
    	if(this.checked){
    		$(".ssp_inputs").each(function(){
    			if(!$(this).parent().hasClass('hidden')){
    				$(this).children().prop('checked', true);
    			}
    		});
    		this.checked = false;
    	}
    });
    // sib search
     $('#sib-search').keyup(function(){
        val = $(this).val().toLowerCase();
        $(".sib_inputs").each(function(){
            if($(this).text().toLowerCase().indexOf(val) > -1){
                $(this).parent().removeClass('hidden');
            }
            else{
                $(this).parent().addClass('hidden');
            }
        });
    });
    $('#sib-all').change(function(){
        if(this.checked){
            $(".sib_inputs").each(function(){
                if(!$(this).parent().hasClass('hidden')){
                    $(this).children().prop('checked', true);
                }
            });
            this.checked = false;
        }
    });
    // seb search
     $('#seb-search').keyup(function(){
        val = $(this).val().toLowerCase();
        $(".seb_inputs").each(function(){
            if($(this).text().toLowerCase().indexOf(val) > -1){
                $(this).parent().removeClass('hidden');
            }
            else{
                $(this).parent().addClass('hidden');
            }
        });
    });
    $('#seb-all').change(function(){
        if(this.checked){
            $(".seb_inputs").each(function(){
                if(!$(this).parent().hasClass('hidden')){
                    $(this).children().prop('checked', true);
                }
            });
            this.checked = false;
        }
    });
});