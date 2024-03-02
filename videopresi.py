from flask import Flask, render_template, jsonify, request
import vlc
import time
from pynput import mouse
from tk_player import FSPlayer
import threading
import tkinter as tk
import sys

app = Flask(__name__)




# Define a route for the HTML page
@app.route("/")
def index():
    return render_template("index.html")

# Define a route to start playing the video
@app.route("/play_video")
def play_video():

    video_path = request.args.get("ID")
    def start_video():
        video_player = FSPlayer(video_path)
        video_player.player.play()
        video_player.root.mainloop()
        del video_player
        return

    video_thread = threading.Thread(target=start_video)
    video_thread.start()
    return jsonify(message="Video is playing")

if __name__ == "__main__":
    app.run(debug=1)
