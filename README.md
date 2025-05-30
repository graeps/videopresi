# Videopräsentationen für das Keltermuseum Unterjesingen.

## Beschreibung

Die Präsentationen laufen als lokale Website auf einem RaspberryPi. Es laufen Slideshow-Vorschauen für Videos, die
durch Anklicken gestartet werden können.
In der aktuellen Version werden die Videos in Firefox abgespielt. Alternativ können die Videos auch über einen Custom
Player (Nutzt vlc-player und tkinter) abgespielt werden, siehe `old_videoplayer_ctk/`.

Durch Ausführen von `scripts/setup.sh` kann ein RaspberryPi erstmals in Betrieb genommen werden. Danach wird nach dem
Hochfahren automatisch die gewünschte Präsentation im Kiosk-Modus gestartet.

___

## RaspberryPi einrichten:

Der RaspberryPi benötigt das neuste OS Debian Bookworm.

1. Terminal öffnen mit CTRL+ALT+T
2. Die Präsentationen **ohne** Video Dateien herunterzuladen:
   `git clone https://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@github.com/graeps/videopresi.git`. Darauf achten, dass der Ordner
   unter `/home/pi/videopresi` abgelegt ist.
3. Videos auf den Raspi kopieren/herunterladen und in `/home/pi/videopresi/src/static/videos/`
   ablegen. Filmdateien unbedingt wie in unten beschrieben benennen!
4. Im Terminal `/home/pi/videopresi/scripts/setup.sh` ausführen und die weiteren Schritte befolgen. Es kann aus einer der aktuell fünf Präsentationen (Wengerter, Schmied, Wagner, Küfer, Einmachen&Einwecken) ausgewählt werden.
5. Zur Überprüfung den Raspi neu starten. Er sollte einige Sekunden nach dem Start die Slideshow im Vollbildmodus
   öffnen. Es sollte kein Cursor zusehen sein und kein Bildschirmschoner o.A. die Präsentation unterbrechen.

Falls doch ein Cursor sichtbar sein soll, muss die Zeile `cursor: none` in der Datei `/src/static/styles/main-styles.css/` auskommentiert oder gelöscht werden. 

___

## Übersicht Dateien

```videopresi
├── logs                      
├── scripts                   # Bash-Scripts für Setup und Start
├── src             
│   ├── old_videoplayer_ctk   # Aktuell nicht genutzt                    
│   ├── static                   
│   │   ├── fonts             
│   │   ├── images  <--------- Hier Bilder ablegen
│   │   ├── scripts           # Javascript für Slideshows und Videoplayerfunktion
│   │   ├── styles            # CSS für Slideshows
│   │   └── videos  <--------- Hier Videos ablegen (Namen beachten!)
│   ├── templates             # HTML Templates
└── systemd                   # Dateien für Autostart-Setup auf RasperryPi
```

___

## Benennung der  Videodateien

Die Videos für die jeweiligen Präsentationen müssen unter folgenden Namen in diesem Ordner abgelegt werden:

**Videos zum Einwecken etc.**

* `haltbarmachen.mp4`
* `KiZweBro.mp4`
* `baecker.mp4`

**Küfer**

* `kuefer.mp4`

**Schmied**

* `schmied.mp4`

**Wagner**

* `wagner.mp4`

**Großer Monitor**

* `mueller.mp4`
* `imker.mp4`
* `sense.mp4`
* `wengerter.mp4`
* `sackkunde.mp4`

**Schulprojekt**
* `lore_koehm.mp4`
* `elfriede_bergmeir.mp4`
* `heinz_eiting.mp4`
* `adolf_zeeb.mp4`
* `heimatfilm.mp4` 