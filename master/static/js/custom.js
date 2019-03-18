$(document).ready(function(){
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
});

$(document).on('.item-amount' , function(event){
	var total = $('#sub_total').val() * 1;
	var sgst = (total/100)*9;
	var num1 = sgst;
	var obj1 = document.getElementById('sgst')
	obj1.value = num1;
	var cgst = (total/100)*9;
	var num2 = cgst;
	var obj2 = document.getElementById('cgst')
	obj2.value = num2;

});


});