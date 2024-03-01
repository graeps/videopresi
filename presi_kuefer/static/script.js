
//timerfunction
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}





//slideshow funktion. arrays und for schleifen, falls mehr Videos dazu kommen

var imageSources = [
    ["/static/bilder/img01.png", "/static/bilder/img02.png", "/static/bilder/img03.png","/static/bilder/img04.png","/static/bilder/img05.png"]
];

var currentIndex = 1;

async function changeImage() {
  const img = document.getElementsByClassName("slide-img");

  for(let i = 0; i<img.length; i++){
    img[i].style.opacity=0.1;
    await sleep(400);
    
  }
  await sleep(1600);

  for(let i = 0; i<img.length; i++){
    img[i].src = imageSources[i][currentIndex];
    img[i].style.opacity=1;
    await sleep(400);
  }

  currentIndex++;
  currentIndex = currentIndex % 5
}

setInterval(changeImage, 10000); 



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
