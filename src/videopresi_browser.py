from flask import Flask, render_template, request

app = Flask(__name__)


# Generic route
@app.route("/<presentation>")
def show_video_collection(presentation):
    presentations = {
        "kuefer": {
            "title": "Keltermuseum Unterjesingen - Kuefer",
            "css": ["single-video.css"],
            "script": "kuefer.js",
            "videos": [
                {
                    "title": "Der Küfer",
                    "description": "Herstellung eines Holzfasses (8:12)",
                    "video_file": "kuefer.mp4",
                    "image_id": "img-kuefer",
                    "image": "kuefer/img01.png",
                    "button_text": "Film starten"
                }
            ]
        },
        "schmied": {
            "title": "Keltermuseum Unterjesingen - Schmied",
            "css": ["single-video.css"],
            "script": "schmied.js",
            "videos": [
                {
                    "title": "Der Schmied",
                    "description": "Herstellung einer Hacke (5:52)",
                    "video_file": "schmied.mp4",
                    "image_id": "img-schmied",
                    "image": "schmied/img01.png",
                    "button_text": "Film starten"
                }
            ]
        },
        "wagner": {
            "title": "Keltermuseum Unterjesingen - Wagner",
            "css": ["single-video.css"],
            "script": "wagner.js",
            "videos": [
                {
                    "title": "Der Wagner",
                    "description": "Herstellung eines Hackenstiels (5:10)",
                    "video_file": "wagner.mp4",
                    "image_id": "img-wagner",
                    "image": "wagner/img01.png",
                    "button_text": "Film starten"
                }
            ]
        },
        "einwecken": {
            "title": "Keltermuseum Unterjesingen - Einwecken",
            "css": ["three-videos.css"],
            "script": "einwecken.js",
            "videos": [
                {
                    "title": "Kirschen, Zwetschken, Brombeeren",
                    "description": "Einkochen Einwecken Eindünsten (5:46)",
                    "video_file": "KiZweBro.mp4",
                    "image_id": "img-kizwebro",
                    "image": "kizwebro/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Lebensmittel haltbar machen",
                    "description": "Erklärungen und Geschichten (6:48)",
                    "video_file": "haltbarmachen.mp4",
                    "image_id": "img-haltbarmachen",
                    "image": "haltbarmachen/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Der Bäcker",
                    "description": "Ein Freitag in der Backstube (6:32)",
                    "video_file": "baecker.mp4",
                    "image_id": "img-baecker",
                    "image": "baecker/img01.png",
                    "button_text": "Film starten"
                },
            ]
        },
        "wengerter": {
            "title": "Keltermuseum Unterjesingen - Wengerter",
            "css": ["five-videos-4k.css"],
            "script": "wengerter.js",
            "videos": [
                {
                    "title": "Die Obere Mühle",
                    "description": "Mehl aus Dinkel und Emmer (4:07)",
                    "video_file": "mueller.mp4",
                    "image_id": "img-mueller",
                    "image": "mueller/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Der Imker",
                    "description": "Von Bienenwachs und Honig (4:05)",
                    "video_file": "imker.mp4",
                    "image_id": "img-imker",
                    "image": "imker/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Mit der Sense mähen",
                    "description": "Was ist eigentlich ein Worb? (18:06)",
                    "video_file": "sense.mp4",
                    "image_id": "img-sense",
                    "image": "sense/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Der Wengerter",
                    "description": "Weinbau in Unterjesingen (5:06)",
                    "video_file": "wengerter.mp4",
                    "image_id": "img-wengerter",
                    "image": "wengerter/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Kleine Sackkunde",
                    "description": "Geschichten und Verzierungen (4:58)",
                    "video_file": "sackkunde.mp4",
                    "image_id": "img-sackkunde",
                    "image": "sackkunde/img01.png",
                    "button_text": "Film starten"
                },
            ]
        },
        "schulprojekt": {
            "title": "Keltermuseum Unterjesingen - Schulprojekt",
            "css": ["five-videos.css"],
            "script": "schulprojekt.js",
            "videos": [
                {
                    "title": "Lore Köhm erzählt...",
                    "description": "Jahrgang 1927 (5:01)",
                    "video_file": "lore_koehm.mp4",
                    "image_id": "img-lore",
                    "image": "lore_koehm/img01.jpg",
                    "button_text": "Audio starten"
                },
                {
                    "title": "Die neue Schule",
                    "description": "Heimatfilm (3:32)",
                    "video_file": "heimatfilm.mp4",
                    "image_id": "img-heimatfilm",
                    "image": "heimatfilm/img01.png",
                    "button_text": "Film starten"
                },
                {
                    "title": "Elfriede Bergmeier erzählt...",
                    "description": "Jahrgang 1930 (5:36)",
                    "video_file": "elfriede_bergmeir.mp4",
                    "image_id": "img-name3",
                    "image": "elfriede_bergmeir/img01.jpg",
                    "button_text": "Audio starten"
                },
                {
                    "title": "Heinz Eiting erzählt...",
                    "description": "Jahrgang 1939 (3:05)",
                    "video_file": "heinz_eiting.mp4",
                    "image_id": "img-name4",
                    "image": "heinz_eiting/img01.jpg",
                    "button_text": "Audio starten"
                },
                {
                    "title": "Adolf Zeeb erzählt...",
                    "description": "Jahrgang 1950 (5:27)",
                    "video_file": "adolf_zeeb.mp4",
                    "image_id": "img-name5",
                    "image": "adolf_zeeb/img01.jpg",
                    "button_text": "Audio starten"
                },
            ]
        }
    }

    if presentation not in presentations:
        return "Collection not found", 404

    context = presentations[presentation]
    context["main_css"] = "main-styles.css"
    return render_template("ff-template.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
