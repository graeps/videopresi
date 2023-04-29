Neuen Raspberry einrichten:

0. Graphik hochstellen: 
    Einstellungen>Raspberry Pi-Konfigurationen>Leistung>GPU-Speicher=256 und neustarten.

Terminal öffnen mit CTRL+ALT+T

1. Folgendes im Terminal eingeben um die Präsentationen ohne Video Dateien herunterzuladen
            git clone -b v1 https://github.com/timtombobjohn/videopresi.py
2. in den Ordner /home/pi/videopresi gehen und den Ordner mit der gewünschten Präsentation nach /home/pi/<presi_name>/ ablegen
3. Videos auf den Raspi kopieren/herunterladen. Anschließen Video(s) nach /home/pi/<presi_name>/static/filme/ verschieben 
    und umbennen wie in film_name.txt geschrieben.
4. Damit es später Ton gibt, jetzt die Anleitung #pulseaudio unten befolgen
5. benögtigte Python Module im Terminal hinzufügen:
            sudo pip install python-vlc
            sudo pip install keyboard
            sudo pip install mouse
            sudo pip install flask
6. kleiner Test:
            sudo python3 ~/<presi_name>/videopresi.py
    Browser öffnen und "localhost:5000" in der URL-Zeile eingeben. Klappt? 
    Es sollte eine Diashow zusehen sein, kein Ton, unsichtbarer Mauszeigen. Wenn auf "Film starten" geklickt wird, sollte in Film beginnen, 
    mit Ton, der durch erneuten Links-Klick, oder "q" abgebrochen werden kann. Dann sollte man zurück zur Diashow geleitet werden. 
7. Jetzt Anleitung unten zum #autostart befolgen.
8. Finaler Test nach Neustart:
            sudo reboot
    nach der Start sollte nach mindestens 1min und höchstens 2min die Präsentation im Randlosen fullscreen Modus angezeigt werden.
   (CRTL+F4 um herauszukommen)
9. Bei Bedarf kann der restliche /home/pi/videopresi Ordner gelöscht werden. (Außer die readme.txt Datei, die du gerade ließt ;-))




##############pulseaudio####################
            Solution run PulseAudio for all your users
            Add bellow lines into /etc/systemd/system/pulseaudio.service file and save. Datei als admin öffnen mit zB sudo nano/etc/systemd/system/pulseaudio.service
             Achtung keine Leerzeichen am Zeilenanfang. 

                    [Unit]
                    Description=PulseAudio system server

                    [Service]
                    Type=notify
                    ExecStart=pulseaudio --daemonize=no --system --realtime --log-target=journal

                    [Install]
                    WantedBy=multi-user.target

            Enable service

                    sudo systemctl --system enable pulseaudio.service
                    sudo systemctl --system start pulseaudio.service
                    sudo systemctl --system status pulseaudio.service

            Edit Client conf /etc/pulse/client.conf and replace ass bellow

                    default-server = /var/run/pulse/native
                    autospawn = no

            Add root to pulse group

                    sudo adduser root pulse-access

            And finally reboot the system




###############autostart##################
            Datei erstellen und beschreiben:
            sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

            Inhalt reinkopieren (Achtung, wieder keine Leerzeichen oder Tabs am Zeilenanfang und in der letzten Zeile den wirlichen Namen im Dateipfad angeben):

                    @lxpanel --profile LXDE-pi
                    @pcmanfm --desktop --profile LXDE-pi
                    @xscreensaver -no-splash
            
                    #kein screen blanking
                    @xset s noblank
                    @xset s off
                    @xset s -dpms

                    /home/pi//<presi_name>/chrome.sh
                    /home/pi/<presi_name>/videopresi.sh
