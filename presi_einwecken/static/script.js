
//timerfunction
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}





//slideshow funktion. arrays und for schleifen, falls mehr Videos dazu kommen

var imageSources = [
    ["/static/bilder/film1/img01.png", "/static/bilder/film1/img02.png", "/static/bilder/film1/img03.png","/static/bilder/film1/img04.png","/static/bilder/film1/img05.png","/static/bilder/film1/img06.png"],
    ["/static/bilder/film2/img01.png", "/static/bilder/film2/img02.png", "/static/bilder/film2/img03.png","/static/bilder/film2/img04.png","/static/bilder/film2/img05.png","/static/bilder/film2/img06.png"]
];

var currentIndex = 1;

async function changeImage() {
  const img = document.getElementsByClassName("slide-img");

  for(let i = 0; i<img.length; i++){
    img[i].style.opacity=0;
    await sleep(3000);
    img[i].src = imageSources[i][currentIndex];
    img[i].style.opacity=1;
    await sleep(7000);
  }

  // await sleep(2000);

  // for(let i = 0; i<img.length; i++){
  //   img[i].src = imageSources[i][currentIndex];
  //   img[i].style.opacity=1;
  //   await sleep(400);
  // }

  currentIndex++;
  currentIndex = currentIndex % 6
}

setInterval(changeImage, 20000); 



//video play funktion, schickt request mit URL
		function playVideo(videoURL) {
			var xhttp = new XMLHttpRequest();
			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
					console.log("Received response: " + this.responseText);
				}
			};
			xhttp.open("GET", `/play_video?ID=${videoURL}`, true);
			xhttp.send();
		}
