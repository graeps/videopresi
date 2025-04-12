export function playVideo(filename) {
    const overlay = document.getElementById("video-overlay");
    const player = document.getElementById("video-player");
    const close = document.getElementById("close-video");

    player.src = "/static/videos/" + filename;
    overlay.style.display = "block";
    player.play();

    close.onclick = () => {
        player.pause();
        player.src = "";
        overlay.style.display = "none";
    };
}