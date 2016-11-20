
var currentContext = {
	tracks:[],
	iterator:{},
	it:{},
	currentTrack:-1,
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
	
	getResourse : function(url) {
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
		
		if(this.currentTrack != -1) {
			$('#'+this.currentTrack.toString()).css("background-color", "transparent");
			$('#'+this.currentTrack.toString()).find("font").css("color", "black");
			$('#'+this.currentTrack.toString()).find("i").css("visibility", "hidden");
			$('#'+this.currentTrack.toString()).css("background-color", "transparent");
			$('#'+this.currentTrack.toString()).css("color", "black");
			
			$('#'+this.currentTrack.toString()).hover(function(){
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
		}
		
		this.currentTrack=this.it.index;
		
		$('#'+this.it.index.toString()).off( "mouseenter mouseleave" );
		$('#'+this.it.index.toString()).css("background-color", "#0066ff");
		$('#'+this.it.index.toString()).find("font").css("color", "white");
		$('#'+this.it.index.toString()).find("i").css("visibility", "visible");
		$('#'+this.it.index.toString()).find("i").css("color", "white");
		
		
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
	$.get(staticDomain + "player/mobilePlayerBar.html", function(data, status){
		document.body.innerHTML += data;
		playerDOM.init();
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
				albumArtist.innerHTML = item.artist;
				divContent.appendChild(albumArtist);
				divContent.appendChild(document.createElement("br"));
				
				tracksDiv = document.createElement("div");
				tracksDiv.style = "list-style-type:none;margin: 0; padding: 0;margin-top:80px";
				
				tracks = document.createElement("ul");
				tracks.style = "list-style-type:none;margin: 0; padding: 0;";
				
				item.tracks.forEach(
					function (item, index) {
						var auxIndex = globalIndex;
						
						track = document.createElement("li");
						track.id = auxIndex;
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


var makeTrackList = function(tracks) {
	var divList = htmlToElement('<div class="list-group"></div>');
	tracks.forEach(
		function (item, index) {
			var track = htmlToElement('<a href="#" class="list-group-item"></a>');
			track.id = "track"+item.id;
			track.onclick = function() {currentContext.play(item.id)};
			track.innerHTML = item.title;
			divList.appendChild(track);
		});
	return divList;
};

var makeAlbumList = function(albums) {
	var divList = htmlToElement('<div class="list-group"></div>');
	albums.forEach(
		function (item, index) {
			var album = htmlToElement('<a href="#" class="list-group-item" style="display: flex;"></a>');
			
			album.appendChild(
				htmlToElement('<div style=" display: flex;flex-direction: column;justify-content: center;"></div>')
				).appendChild(
					$(htmlToElement('<img src="" alt="artwork" style="width:128px;height:128px;">')).attr('src',item.artwork).get(0)
				).parentNode.appendChild(
					$(htmlToElement('<font size="4" style="color: black;"></font>')).html(item.name).get(0)
				)
			album.id = "album"+item.id;
			album.href = "#albums/"+item.id;
			//album.onclick = function() {currentContext.play(auxIndex)};
			//<i class="fa fa-play-circle fa-lg" aria-hidden="true" style="margin-left: 4px; margin-right: 4px; margin-bottom: 4px; visibility: hidden; color: black;"></i><font size="4" style="color: black;">01. Selfcontrol- </font>
			divList.appendChild(album);
		});
	return divList;
};

var updateContent = function(newContent,divId) {
	oldContent = document.getElementById(divId);
	oldContent.innerHTML = "";
	if(Array.isArray(newContent)){
		newContent.forEach(
			function (item, index) {
				oldContent.appendChild(item);
		});
	} else {
		oldContent.appendChild(newContent);
	}
	oldContent.style.display = "initial";
};

var globalAlbums = {};

var getAlbums = function(newContent) {
	$.ajax({
		url: url.album,
		success: function(data) {
			globalAlbums = data;
			$(window).trigger('hashchange');
		}
	})
};


$(window).on('hashchange', function(){
	// On every hash change the render function is called with the new hash.
	// This is how the navigation of our app happens.
	
	render(decodeURI(window.location.hash));
});

function render(url) {
	var urlBase = url.split('/')[0];
	document.getElementById('content').style.display = "none";
	document.getElementById('tracklist').style.display = "none";
	
	var map = {
		'': function() {
			var albums = makeAlbumList(globalAlbums);
			updateContent(albums,"content");
		},
		'#albums': function() {
			var path = url.split('/');
			//var index = url.split('#albums/')[1].trim();
			console.log(path)
			if(path[1] == ""){
				var albums = makeAlbumList(globalAlbums);
				updateContent(albums,"content");
			} else {
				var index = path[1].trim();
				album = globalAlbums.find(function (d) {
					return d.id == index;
				});
				var tracklist = makeTrackList(album.tracks);
				var tracklistDiv = document.getElementById('tracklist');
				updateContent(tracklist,"tracklist")
			}
			
		}
	}
	if(map[urlBase]){
		map[urlBase]();
	}
};

var playerDOM =  {
	playerView : {
		playButton : {},
		init : function () {
			var children = document.getElementById('playerView');
			this.playButton = children.getElementsByClassName('play-button')[0]
		}
	},
	audioTag :{},
	play_pause :function () {
		if (this.audioTag.paused) {
			this.audioTag.play();
			$(this.playerView.playButton).toggleClass("fa-play fa-pause");
		} else {
			this.audioTag.pause();
			$(this.playerView.playButton).toggleClass("fa-pause fa-play");
		}
	},
	init : function () {
		this.audioTag =  document.getElementById("player");
		this.playerView.init();
	}
};


$(document).ready(function() {
	loadRootUrls();
	loadPlayer();
	getAlbums();
});