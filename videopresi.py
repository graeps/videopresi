from flask import Flask, render_template, jsonify, request
import vlc
import time
from pynput import mouse
app = Flask(__name__)

# Initialize VLC media player instance
vlc_instance = vlc.Instance("--no-xlib")
media_player = vlc_instance.media_player_new()

# Define a route for the HTML page
@app.route("/")
def index():
    return render_template("index.html")

# Define a route to start playing the video
@app.route("/play_video")
def play_video():
    #der Dateipfad zum Video wird in "ID" übergeben
    videoURL = request.args.get("ID")
    # Load the video file into the media player
    media = vlc_instance.media_new(videoURL)
    media_player.set_media(media)



    # Set up fullscreen mode
    media_player.set_fullscreen(True)

    def on_click(x,y,button,pressed):
        if pressed and x>1500 and y<250:
#            media_player.set_fullscreen(False)
            media_player.stop()
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Play the video
    media_player.play()

    while True:
#        media_player.set_fullscreen(True)
        if media_player.get_state() == vlc.State.Ended or media_player.get_state() == vlc.State.Stopped:
            break
        time.sleep(0.1)
    
    media_player.stop()
    listener.stop()
    return jsonify(success=True)


if __name__ == "__main__":
    app.run()
