function makeIterator(array,startAt){
    var nextIndex = 0;
    if(startAt != null){
      nextIndex=startAt;
    }
    return {
       next: function(){
           return nextIndex < array.length ?
               {value: array[nextIndex++], done: false} :
               {done: true};
       }
    }
}

var currentContext = {
	tracks:[],
	iterator:{},
	it:{},
	play :  function (index){
			if(index == null) {
				index = 0;
			}
			this.iterator = makeIterator(this.tracks,index);
			this.playNext();
		},
		
	
	playNext : function (){
			this.it = this.iterator.next();
			if(!this.it.done){
				setPlayerSource(this.it.value)
			}
		} 
};




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

var setPlayerSource = function(dataObject){
	var divPlayer = document.getElementById("divPlayer");
	var divArtwork = document.getElementById("divArtwork");
	var player = divPlayer.getElementsByTagName("audio")[0];
	var image = divArtwork.getElementsByTagName("img")[0];
	
	image.src = dataObject.artwork;
	player.innerHTML = "";
	var src = document.createElement("source");
	src.src = dataObject.file.replace('"','');
	src.type = dataObject.type;
	player.appendChild(src);
	player.load();
	player.play();
	player.addEventListener("ended", function(){
		currentContext.playNext();
	});
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
		url: url.track,
		success: function(data) {
			console.log(data);
			currentContext.tracks = data;
			list = document.getElementById("list");
			list.innerHTML = "";
			data.forEach(
				function (item, index) {
					var divId = "divTrack"+index;
					var div = document.createElement("div");
					div.setAttribute("id",divId);
					
					var lable = document.createElement("lable");
					lable.innerHTML = item.title;
					var btn = document.createElement("button");
					btn.innerHTML = "Select";
					btn.onclick = function() {currentContext.play(index)};
										
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