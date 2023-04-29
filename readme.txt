browser in borderless fullscree:
	$ chromium-browser --kiosk http://localhost:5000
	crtl+F4 um zu beenden

graphic hochstellen

direkt bei start öffnen

dateipfade bilder, videos

mouse und keyboard module brauche sudo rechte

pulseaudio hat probleme mit sudo evlt vor python star
	$ sudo pulseaudion --start 


#vlc player python modul
pip install python-vlc

#keyboard module
pip install keyboard (?)

pip install mouse (?)

graphik speicher hochstellen

#autostart datei
sudo nano /etc/xdg/autostart/display.desktop

#path
wenn programm von ~/ aus ausgeführt wird,
muss in html videodateipfad mit 'presi_wagner/static/...' beginnen

#kein bildschirmschoner
sudo apt install x11-xserver-utils
und dann --noblank option

#noch eine autostart version FUNKTIONIERT
zwei bash dateien, eine für chrome mit 60sec timer. eine für python.
dann datein anlegen 
/home/pi/.config/lxsession/LXDE-pi/autostart
siehe seite 83 pipresents anleitung!https://raw.githubusercontent.com/KenT2/pipresents-beep/master/manual.pdf


#pulseaudio-hack
            Solution run PulseAudio for all your users
            Add bellow lines into /etc/systemd/system/pulseaudio.service file and save

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


#autostartdatei einrichten
            datei erstellen:
            /home/pi/.config/lxsession/LXDE-pi/autostart

            inhalt:

                    @lxpanel --profile LXDE-pi
                    @pcmanfm --desktop --profile LXDE-pi
                    @xscreensaver -no-splash
            
                    #kein screen blanking
                    @xset s noblank
                    @xset s off
                    @xset s -dpms

                    /home/pi//chrome.sh
                    /home/pi/<presi_name>/videopresi.sh
