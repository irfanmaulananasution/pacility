$(document).ready(function(){
	showAnnouncements();
	var username = $('#username').attr("value");
	$('#id_username').attr({"value": username, "readonly": true});

	$('.btn-submit').attr('disabled', true);
	$('.btn-submit').css('background-color', "#A4A4A4");
	$('.btn-submit').hover(function(){
	  $(this).css('color', '#FFFFFF');
	});

	$('#id_title').keyup(function(){
		if($('#id_title').val() != "" && $('#id_content').val() != ""){
			$('.btn-submit').attr('disabled', false);
			$('.btn-submit').css('background-color', "#303C6C");
			$('.btn-submit').hover(function(){
			  	$(this).css('color', '#303C6C');
			  	$(this).css('background-color', '#F4976C');
			}, function(){
				$(this).css('color', '#FFFFFF');
			  	$(this).css('background-color', '#303C6C');
			});
		} else{
			$('.btn-submit').attr('disabled', true);
			$('.btn-submit').css('background-color', "#A4A4A4");
		}
	})

	$('#id_content').keyup(function(){
		if($('#id_title').val() != "" && $('#id_content').val() != ""){
			$('.btn-submit').attr('disabled', false);
			$('.btn-submit').css('background-color', "#303C6C");
			$('.btn-submit').hover(function(){
			  $(this).css('color', '#303C6C');
			  $(this).css('background-color', '#F4976C');
			}, function(){
				$(this).css('color', '#FFFFFF');
			  	$(this).css('background-color', '#303C6C');
			});
		} else{
			$('.btn-submit').attr('disabled', true);
			$('.btn-submit').css('background-color', "#A4A4A4");
		}
	})

    $('#announcement-form').ajaxForm({
        url: 'add_announcement',
        type: 'POST',
        success: function(){
            $("#id_title").val("");
            $("#id_content").val("");
            $("#id_title").css('box-shadow', 'none');
            $("#id_content").css('box-shadow', 'none');
          	showAnnouncements();
        }
    });

    function showAnnouncements(){
		$(".announcement-list").empty();
		$.ajax({
			url: "get_announcements",
			success: function(list){
				$.each(list.announcements.reverse(), function(index, announcement){
					$(".announcement-list").append(`
						<div class="announcement-div bg-light">
							<div class="d-flex justify-content-start">
								<div class="initial-profile">
									${announcement.initial}
								</div>
								<div class="announcement-detail">
									<p class="announcement-title">${announcement.title}</p>
									<p class="announcement-time">by <span class="announcement-author">${announcement.username}</span> - ${announcement.date } at ${announcement.time }</p>
								</div>
							</div>

							<div class="announcement-content">
								${announcement.content}
							</div>
						</div>
					`);

				});
			}
		});
	}
});