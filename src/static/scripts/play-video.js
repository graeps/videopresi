export async function playVideo(videoURL) {
    try {
        const response = await fetch(`/play_video?ID=${videoURL}`);
        if (response.ok) {
            const text = await response.text();
            console.log("Received response:", text);
        }
    } catch (err) {
        console.error("Request failed:", err);
    }
}