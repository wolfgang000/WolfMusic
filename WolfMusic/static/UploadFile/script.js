var UploadFile = function() {
	var data;
	var uploadForm = document.getElementById("uploadForm");
	$.ajax({
		type: "POST",
		url: tracksUrl ,
		data: uploadForm,
		contentType: false,
		success: function(data){
			alert("Archivo subido con exito");
		},
		error: function control(){
			alert("Error al subir archivo");
		}
		
	});
	return false;
	console.log('a');
	alert('b');
	return false;
};