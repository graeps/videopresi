from flask import Flask, render_template, jsonify, request
from video_player import VideoPlayer
from multiprocessing import Process

app = Flask(__name__)


# Define a route for the HTML page
@app.route("/")
def index():
    return render_template("index.html")


# Define a route to start playing the video
@app.route("/play_video")
def play_video():
    video_path = request.args.get("ID")

    process = Process(target=VideoPlayer.start, args=(video_path,))
    process.start()

    return jsonify(message="Video is playing")


if __name__ == "__main__":
    app.run(debug=True)
