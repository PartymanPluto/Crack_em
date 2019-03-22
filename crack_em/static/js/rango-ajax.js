<script src="{% static "js/jquery.min.js" %}"></script>
<script src="{% static "js/rango-ajax.js" %}"></script>

<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js">
</script>

$('#likes').click(function(){
	var userid;
	userid = $(this).attr("data-userid");
	$.get('/crack_em/like/', {profile_id: userid}, function(data){
		$('#like_count').html(data);
			$('#likes').hide();
	});
});
