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
	setTracksFromAlbum : function (albums){
		this.tracks=[];
		albums.forEach(
			function (item, index) {
				item.tracks.forEach(
					function (item, index) {
						console.log(this.tracks)
						this.tracks.push(item.url);
					},this);
			},this);
	},
	play :  function (index){
			if(index == null) {
				index = 0;
			}
			this.iterator = makeIterator(this.tracks,index);
			this.playNext();
		},
	
	getResourse : 
		function(url) {
			return Promise.resolve(
				$.ajax({
					url: url,
					tryCount : 0,
					retryLimit : 3
				})
			);
		},
	
	playNext : function (){
			this.it = this.iterator.next();
			if(!this.it.done){
				this.getResourse(this.it.value).then(
					function(response) {
						setPlayerSource(response)
					},
					function(error) {
						 console.error("Failed!", error);
					}
				);
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
	$(player).bind("ended", function(){
		currentContext.playNext();
		$(player).unbind( "ended");
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
		url: url.album,
		success: function(data) {
			console.log(data);
			currentContext.setTracksFromAlbum(data);
			list = document.getElementById("list");
			list.innerHTML = "";
			globalIndex=0;
			data.forEach(
				function (item, index) {
					var album = document.createElement("div");
					album.style = "margin-bottom:30px;";
					divArtwork = document.createElement("div");
					divArtwork.style = "height:142px; width:142px; display:inline-block;";
					artwork = document.createElement("img");
					artwork.style = "width:140px;height:140px;";
					artwork.src = item.artwork;
					divArtwork.appendChild(artwork);
					
					divContent =  document.createElement("div");
					divContent.style = "display:inline-block; vertical-align:top;";
					
					albumTitle = document.createElement("font");
					albumTitle.size = 6 ;
					albumTitle.innerHTML = item.name;
					divContent.appendChild(albumTitle);
					divContent.appendChild(document.createElement("br"));
					
					albumArtist = document.createElement("font");
					albumArtist.size = 3 ;
					albumArtist.innerHTML = item.name;
					divContent.appendChild(albumArtist);
					divContent.appendChild(document.createElement("br"));
					
					tracksDiv = document.createElement("div");
					tracksDiv.style = "list-style-type:none;margin: 0; padding: 0;margin-top:80px";
					
					tracks = document.createElement("ul");
					tracks.style = "list-style-type:none;margin: 0; padding: 0;";
										
					item.tracks.forEach(
						function (item, index) {
							
							track = document.createElement("li");
							$(track).hover(function(){
								$(this).css("background-color", "#0066ff");
								$(this).find("font").css("color", "white");
								$(this).find("i").css("visibility", "visible");
								$(this).find("i").css("color", "white");
								}, function(){
								$(this).css("background-color", "transparent");
								$(this).find("font").css("color", "black");
								$(this).find("i").css("visibility", "hidden");
								$(this).find("i").css("color", "black");
							});
							track.style = "margin-bottom:3px";
							icon = document.createElement("i");
							icon.setAttribute("class","fa fa-play-circle fa-lg");
							icon.setAttribute("aria-hidden", "true");
							icon.style = "margin-left:4px;margin-right:4px;margin-bottom:4px;visibility:hidden;";
							
							var auxIndex = globalIndex;
							icon.onclick = function() {currentContext.play(auxIndex)};
							
							font = document.createElement("font");
							font.size = 4;
							font.innerHTML = item.title;
							
							track.appendChild(icon);
							track.appendChild(font);
							tracks.appendChild(track);
							
							globalIndex++;
						});
					
					tracksDiv.appendChild(tracks);
					divContent.appendChild(tracksDiv);
					
					album.appendChild(divArtwork);
					album.appendChild(divContent);
					
					list.appendChild(album);
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