$(document).ready(function() {
    $("#ssp").change(function() {
        if ($(this).val() == "1") {
            $.get("https://jsonplaceholder.typicode.com/users", function(data, status) {
            	var i = 0
            	while(i < 3 ){
            		$(".ssp-dy").append(
            			'<div class="checkbox"><label class="ssp_inputs"><input type="checkbox" name="'+data[i].name+'">'+data[i].name+'</label></div>'
            			)
            		i ++;
            	}
            });
            $('#h-ssp').removeClass('hidden');
        } else {
            $('#h-ssp').addClass('hidden');
            $(".ssp-dy").empty()
        }
    });
    $("#sib").change(function() {
        if ($(this).val() == "1") {
            $('#h-sib').removeClass('hidden');
            $.get("https://jsonplaceholder.typicode.com/users", function(data, status) {
 				var i = 3
            	while(i < 6){
            		$(".sib-dy").append(
            			'<div class="checkbox"><label class="sib_inputs"><input type="checkbox" name="'+data[i].name+'">'+data[i].name+'</label></div>'
            			)
            		i ++;
            	}
            });
        } else {
            $('#h-sib').addClass('hidden');
            $(".sib-dy").empty()
        }
    });
    $("#seb").change(function() {
        if ($(this).val() == "1") {
            $('#h-seb').removeClass('hidden');
            $.get("https://jsonplaceholder.typicode.com/users", function(data, status) {
            	var i = 6
            	while(i < 10 ){
            		$(".seb-dy").append(
            			'<div class="checkbox"><label class="seb_inputs"><input type="checkbox" name="'+data[i].name+'">'+data[i].name+'</label></div>'
            			)
            		i ++;
            	}
            });
        } else {
            $('#h-seb').addClass('hidden');
            $(".seb-dy").empty()
        }
    });
    $('#ssp-search').keyup(function() {
        val = $(this).val().toLowerCase();
        $(".ssp_inputs").each(function() {
            if ($(this).text().toLowerCase().indexOf(val) > -1) {
                $(this).parent().removeClass('hidden');
            } else {
                $(this).parent().addClass('hidden');
            }
        });
    });
    $('#ssp-all').change(function() {
        if (this.checked) {
            $(".ssp_inputs").each(function() {
                if (!$(this).parent().hasClass('hidden')) {
                    $(this).children().prop('checked', true);
                }
            });
            this.checked = false;
        }
    });
    // sib search
    $('#sib-search').keyup(function() {
        val = $(this).val().toLowerCase();
        $(".sib_inputs").each(function() {
            if ($(this).text().toLowerCase().indexOf(val) > -1) {
                $(this).parent().removeClass('hidden');
            } else {
                $(this).parent().addClass('hidden');
            }
        });
    });
    $('#sib-all').change(function() {
        if (this.checked) {
            $(".sib_inputs").each(function() {
                if (!$(this).parent().hasClass('hidden')) {
                    $(this).children().prop('checked', true);
                }
            });
            this.checked = false;
        }
    });
    // seb search
    $('#seb-search').keyup(function() {
        val = $(this).val().toLowerCase();
        $(".seb_inputs").each(function() {
            if ($(this).text().toLowerCase().indexOf(val) > -1) {
                $(this).parent().removeClass('hidden');
            } else {
                $(this).parent().addClass('hidden');
            }
        });
    });
    $('#seb-all').change(function() {
        if (this.checked) {
            $(".seb_inputs").each(function() {
                if (!$(this).parent().hasClass('hidden')) {
                    $(this).children().prop('checked', true);
                }
            });
            this.checked = false;
        }
    });
});