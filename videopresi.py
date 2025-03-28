from flask import Flask, render_template, jsonify, request
from videoplayer import VideoPlayer
from multiprocessing import Process

app = Flask(__name__)


# Define a route for the HTML page
@app.route("/einwecken")
def presi_einwecken():
    return render_template("einwecken.html")


@app.route("/kuefer")
def presi_kuefer():
    return render_template("kuefer.html")


@app.route("/schmied")
def presi_schmied():
    return render_template("schmied.html")


@app.route("/wagner")
def presi_wagner():
    return render_template("wagner.html")


@app.route("/wengerter")
def presi_wengerter():
    return render_template("wengerter.html")


@app.route("/play_video")
def play_video():
    video_path = request.args.get("ID")

    process = Process(target=VideoPlayer.start, args=(video_path,))
    process.start()

    return jsonify(message="Video is playing")


if __name__ == "__main__":
    app.run(debug=True)
