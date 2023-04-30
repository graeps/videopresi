Neuen Raspberry einrichten:

0. Graphik hochstellen: 
        Einstellungen>Raspberry Pi-Konfigurationen>Leistung>GPU-Speicher=256 und neustarten.
     Bildschirmschoner desactivieren:
        Einstellungen>Raspberry Pi-Konfigurationen>Display>Disable "Screen Blanking"  

Terminal öffnen mit CTRL+ALT+T

1. Folgendes im Terminal eingeben um die Präsentationen ohne Video Dateien herunterzuladen
            git clone -b v2 https://github.com/timtombobjohn/videopresi.git
2. in den Ordner /home/pi/videopresi gehen und den Ordner mit der gewünschten Präsentation nach ~/<presi_name>/ ablegen
3. Videos auf den Raspi kopieren/herunterladen. Anschließen Video(s) nach /home/pi/<presi_name>/static/filme/ verschieben 
    und umbennen wie in film_name.txt geschrieben.
4. benögtigte Python Module im Terminal hinzufügen:
            pip install python-vlc
            pip install flask
5. kleiner Test:
            python3 ~/<presi_name>/videopresi.py
    Browser öffnen und "localhost:5000" in der URL-Zeile eingeben. Klappt? 
    Es sollte eine Diashow zusehen sein, kein Ton, unsichtbarer Mauszeigen. Wenn auf "Film starten" geklickt wird, sollte in Film beginnen, 
    erkann leider nicht abgebrochen werden.  
8. Jetzt Anleitung unten zum #autostart befolgen.
9. Finaler Test nach Neustart:
            sudo reboot
    nach der Start sollte nach mindestens 1min und höchstens 2min die Präsentation im Randlosen fullscreen Modus angezeigt werden.
   (CRTL+F4 um herauszukommen)
10. Jetzt kann der restliche /home/pi/videopresi Ordner gelöscht werden. (Außer die readme.txt Datei  ;-))





##################autostart##################
       Datei erstellen und beschreiben:
            sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

        Inhalt reinkopieren 
        (Achtung, wieder keine Leerzeichen oder Tabs am Zeilenanfang und in der letzten 
        Zeile den wirlichen Namen im Dateipfad, z.B.  ~/<presi_schmied>/chrome.sh, angeben):

                    @lxpanel --profile LXDE-pi
                    @pcmanfm --desktop --profile LXDE-pi
                    @xscreensaver -no-splash
                    @xset s 0 0
                    @xset s noblank
                    @xset s noexpose
                    @xset dpms 0 0 0

                    ~/<presi_name>/chrome.sh
                    ~/<presi_name>/videopresi.sh
