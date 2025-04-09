Neuen Raspberry einrichten:

Terminal öffnen mit CTRL+ALT+T

1. Folgendes im Terminal eingeben, um die Präsentationen ohne Video Dateien herunterzuladen,
   git clone -b v2 https://github.com/timtombobjohn/videopresi.git
2. Videos auf den Raspi kopieren/herunterladen und nach /home/pi/videopresi/src/static/videos/
   verschieben. Filmdateien unbedingt wie in /home/pi/videopresi/src/static/videos/film_name.txt benennen.
3. /home/pi/videopresi/scripts/setup.sh ausführen
4. Jetzt Anleitung unten zum #autostart befolgen.

##################autostart##################
Datei erstellen und beschreiben:
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

        Inhalt reinkopieren 
        (Achtung, wieder keine Leerzeichen oder Tabs am Zeilenanfang und in der letzten 
        Zeile den wirlichen Namen im Dateipfad, z.B.  ~/presi_schmied/chrome.sh, angeben):

                    @lxpanel --profile LXDE-pi
                    @pcmanfm --desktop --profile LXDE-pi
                    @xscreensaver -no-splash
                    @xset s 0 0
                    @xset s noblank
                    @xset s noexpose
                    @xset dpms 0 0 0

                    ~/<presi_name>/chrome.sh
                    ~/<presi_name>/videopresi.sh
