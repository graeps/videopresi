from flask import Flask, render_template, jsonify, request
from old_videoplayer_ctk import VideoPlayer
from multiprocessing import Process

app = Flask(__name__)


# Generic route
@app.route("/<presentation>")
def show_video_collection(presentation):
    presentations = {
        "kuefer": {
            "title": "keltermuseum Unterjesingen - Kuefer",
            "css": ["single-video.css"],
            "script": "kuefer.js",
            "videos": [
                {
                    "title": "Der Küfer",
                    "description": "Herstellung eines Holzfasses (8:12)",
                    "video_file": "kuefer.mp4",
                    "image_id": "img-kuefer",
                    "image": "kuefer/img01.png",
                }
            ]
        },
        "schmied": {
            "title": "keltermuseum Unterjesingen - Schmied",
            "css": ["single-video.css"],
            "script": "schmied.js",
            "videos": [
                {
                    "title": "Der Schmied",
                    "description": "Herstellung einer Hacke (5:52)",
                    "video_file": "schmied.mp4",
                    "image_id": "img-schmied",
                    "image": "schmied/img01.png",
                }
            ]
        },
        "wagner": {
            "title": "keltermuseum Unterjesingen - Wagner",
            "css": ["single-video.css"],
            "script": "wagner.js",
            "videos": [
                {
                    "title": "Der Wagner",
                    "description": "Herstellung eines Hackenstiels (5:10)",
                    "video_file": "wagner.mp4",
                    "image_id": "img-wagner",
                    "image": "wagner/img01.png",
                }
            ]
        },
        "einwecken": {
            "title": "keltermuseum Unterjesingen - Einwecken",
            "css": ["three-videos.css"],
            "script": "einwecken.js",
            "videos": [
                {
                    "title": "Kirschen, Zwetschken, Brombeeren",
                    "description": "Einkochen Einwecken Eindünsten (5:46)",
                    "video_file": "KiZweBro.mp4",
                    "image_id": "img-kizwebro",
                    "image": "kizwebro/img01.png",
                },
                {
                    "title": "Lebensmittel haltbar machen",
                    "description": "Erklärungen und Geschichten (6:48)",
                    "video_file": "haltbarmachen.mp4",
                    "image_id": "img-haltbarmachen",
                    "image": "haltbarmachen/img01.png",
                },
                {
                    "title": "Der Bäcker",
                    "description": "Ein Freitag in der Backstube (6:32)",
                    "video_file": "baecker.mp4",
                    "image_id": "img-baecker",
                    "image": "baecker/img01.png",
                },
            ]
        },
        "wengerter": {
            "title": "keltermuseum Unterjesingen - Wengerter",
            "css": ["five-videos-4k.css"],
            "script": "wengerter.js",
            "videos": [
                {
                    "title": "Die Obere Mühle",
                    "description": "Mehl aus Dinkel und Emmer (4:07)",
                    "video_file": "mueller.mp4",
                    "image_id": "img-mueller",
                    "image": "mueller/img01.png",
                },
                {
                    "title": "Der Imker",
                    "description": "Von Bienenwachs und Honig (4:05)",
                    "video_file": "imker.mp4",
                    "image_id": "img-imker",
                    "image": "imker/img01.png",
                },
                {
                    "title": "Mit der Sense mähen",
                    "description": "Was ist eigentlich ein Worb? (18:06)",
                    "video_file": "sense.mp4",
                    "image_id": "img-sense",
                    "image": "sense/img01.png",
                },
                {
                    "title": "Der Wengerter",
                    "description": "Weinbau in Unterjesingen (5:06)",
                    "video_file": "wengerter.mp4",
                    "image_id": "img-wengerter",
                    "image": "wengerter/img01.png",
                },
                {
                    "title": "Kleine Sackkunde",
                    "description": "Geschichten und Verzierungen (4:58)",
                    "video_file": "sackkunde.mp4",
                    "image_id": "img-sackkunde",
                    "image": "sackkunde/img01.png",
                },
            ]
        }
    }

    if presentation not in presentations:
        return "Collection not found", 404

    context = presentations[presentation]
    context["main_css"] = "main-styles.css"
    return render_template("multi_video_template.html", **context)


@app.route("/play_video")
def play_video():
    video_path = request.args.get("ID")
    process = Process(target=VideoPlayer.start, args=(video_path,))
    process.start()
    return jsonify(message="Video is playing")


if __name__ == "__main__":
    app.run(debug=True)
