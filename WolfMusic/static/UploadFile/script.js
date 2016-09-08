var UploadFile = function() {
	var data;
	var uploadForm = document.getElementById("uploadForm");
	var form = new FormData(document.forms.namedItem("fileUpload"));
	$.ajax({
		type: "POST",
		url: url.tracks ,
		data: form,
		contentType: false,
		processData: false,
		success: function(data){
			alert("Archivo subido con exito");
			loadList();
		},
		error: function control(){
			alert("Error al subir archivo");
		}
		
	});
	return false;
};