var loadPlayer  = function() {
	$("<link/>", {
		rel: "stylesheet",
		type: "text/css",
		href:  staticDomain + "player/style.css"
	}).appendTo("head");
	var body = document.getElementsByTagName("BODY")[0];
	$.get(staticDomain + "player/player.html", function(data, status){
		document.body.innerHTML += data;
	});
}

var setPlayerSource = function(idDataObject){
	var divPlayer = document.getElementById("divPlayer");
	var divArtwork = document.getElementById("divArtwork");
	var player = divPlayer.getElementsByTagName("audio")[0];
	var image = divArtwork.getElementsByTagName("img")[0];
	
	dataObject = $('#'+idDataObject).data();
	console.log(dataObject);
	
	image.src = dataObject.artwork;
	player.innerHTML = "";
	var src = document.createElement("source");
	src.src = dataObject.file.replace('"','');
	src.type = dataObject.type;
	player.appendChild(src);
	player.load();
	player.play();
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
			list.innerHTML = "";
			data.forEach(
				function (item, index) {
					var divId = "divTrack"+index;
					var div = document.createElement("div");
					div.setAttribute("id",divId);
					$(div).data(item)
					console.log($(div).data());
					
					var lable = document.createElement("lable");
					lable.innerHTML = item.title;
					var btn = document.createElement("button");
					btn.innerHTML = "Select";
					btn.onclick = function() {setPlayerSource(divId)};
					
					
					div.appendChild(lable)
					div.appendChild(btn);
					div.appendChild(document.createElement("br"));
					
					list.appendChild(div);
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