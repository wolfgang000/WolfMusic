var loadPlayer  = function() {
	var divPlayer = document.getElementById("divPlayer");
	$.get(staticDomain + "player/player.html", function(data, status){
		divPlayer.innerHTML = data;
	});
}

var setPlayerSource = function(url,type){
	var divPlayer = document.getElementById("divPlayer");
	
	var player = divPlayer.getElementsByTagName("audio")[0];
	player.innerHTML = "";
	var src = document.createElement("source");
	src.src = url;
	src.type = type;
	player.appendChild(src);
	player.load();
};

var setUploadFileForm  = function() {
	
	$.getScript( staticDomain + "UploadFile/script.js")
	.done(function( script, textStatus ) {
		console.log( "loaded UploadFile/script.js" );
	})
	.fail(function( jqxhr, settings, exception ) {
		console.log( "Error at loading UploadFile/script.js");
	});
	
	var divPlayer = document.getElementById("divUploadForm");
	divPlayer.innerHTML = "";
	$.get(staticDomain +"UploadFile/form.html", function(data, status){
		divPlayer.innerHTML = data;
	});
};

var loadList = function() {
	$.ajax({
		url: url.tracks,
		success: function(data) {
			console.log(data);
			list = document.getElementById("list");
			data.forEach(
				function (item, index) {
					var lable = document.createElement("lable");
					lable.innerHTML = item.title;
					var btn = document.createElement("button");
					btn.innerHTML = "Select";
					btn.onclick = function() {setPlayerSource(item.file,item.type)};
					list.appendChild(lable);
					list.appendChild(btn);
					list.appendChild(document.createElement("br"));
				}
			)
		}
	})
};

$(document).ready(function() {
	loadRootUrls();
	loadPlayer();
	loadList();
});