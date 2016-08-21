<script>
navbar active
$("#navbar-nav li").click(function(){
	 $(this).siblings().removeClass('active'); 
	 $(this).addClass('active'); 
});

</script>
