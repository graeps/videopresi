#!/bin/bash

# Konfiguration laden
source /home/pi/videopresi/presentation.conf

# Logverzeichnis erstellen
mkdir -p ~/videopresi/logs

# Virtuelle Umgebung aktivieren
source /home/pi/videopresi/venv/bin/activate

while true; do
  # Starte Flask-Server
  python3 ~/videopresi/src/videopresi_browser.py >> ~/videopresi/logs/run.log 2>> ~/videopresi/logs/error.log &
  FLASK_PID=$!

  # Warten bis Flask erreichbar ist (max. 30s)
  for i in {1..30}; do
    if curl -s http://localhost:5000 > /dev/null; then
        break
    fi
    sleep 1
  done

  # Starte Chromium im Kiosk-Modus
  echo "==== Starting Chromium ($PRESENTATION_URL) at $(date) ====" >> ~/videopresi/logs/run.log
  chromium-browser "$PRESENTATION_URL" --kiosk --noerrdialogs --disable-infobars --no-first-run --ozone-platform=wayland --enable-features=OverlayScrollbar --start-maximized >> ~/videopresi/logs/run.log 2>> ~/videopresi/logs/error.log &
  CHROMIUM_PID=$!

  # Überwache Prozesse
  wait -n $FLASK_PID $CHROMIUM_PID
  echo "==== Process crashed at $(date) ====" >> ~/videopresi/logs/error.log
  kill -9 $FLASK_PID $CHROMIUM_PID 2>/dev/null
  sleep 10
done
