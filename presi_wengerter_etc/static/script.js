
//timerfunction
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}





//slideshow funktion. arrays und for schleifen, falls mehr Videos dazu kommen

var imageSources = [
    ["/static/bilder/mueller/img01.png", "/static/bilder/mueller/img02.png", "/static/bilder/mueller/img03.png","/static/bilder/mueller/img04.png","/static/bilder/mueller/img05.png"],
    ["/static/bilder/imker/img01.png", "/static/bilder/imker/img02.png", "/static/bilder/imker/img03.png","/static/bilder/imker/img04.png","/static/bilder/imker/img05.png"],
    ["/static/bilder/sense/img01.png", "/static/bilder/sense/img02.png", "/static/bilder/sense/img03.png","/static/bilder/sense/img04.png","/static/bilder/sense/img05.png"],
    ["/static/bilder/wengerter/img01.png", "/static/bilder/wengerter/img02.png", "/static/bilder/wengerter/img03.png","/static/bilder/wengerter/img04.png","/static/bilder/wengerter/img05.png"],
    ["/static/bilder/sackkunde/img01.png", "/static/bilder/sackkunde/img02.png", "/static/bilder/sackkunde/img03.png","/static/bilder/sackkunde/img04.png","/static/bilder/sackkunde/img05.png"]
];

var currentIndex = 1;

async function changeImage() {
  const img = document.getElementsByClassName("slide-img");
  const container = document.getElementsByClassName("video");

  for(let i = 1; i<img.length+1; i++){
    let x = ((7*i) + currentIndex) % 5;
    img[x].style.opacity=0;
    await sleep(3200);
    
    img[x].src = imageSources[x][currentIndex];
    img[x].style.opacity=1;
    container[x].style.filter="brightness(1.2)";
    container[x].style.boxShadow = "0 0 4vh rgba(0, 0, 0, 0.6)";
    await sleep(5000);
    container[x].style.filter="brightness(1)";
    container[x].style.boxShadow = "0 0 2vh rgba(0, 0, 0, 0.3)";
  }

  // await sleep(2000);

  // for(let i = 0; i<img.length; i++){
  //   img[i].src = imageSources[i][currentIndex];
  //   img[i].style.opacity=1;
  //   await sleep(400);
  // }

  currentIndex++;
  currentIndex = currentIndex % 5
}

setInterval(changeImage, 41000); 



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
