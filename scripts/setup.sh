#!/bin/bash

IS_TEST=${IS_TEST:-false}
LOG_PREFIX=">>>"

log() {
  echo "$LOG_PREFIX $1"
}

# 1. GPU-Speicher
log "GPU-Speicher wird auf 256MB eingestellt..."
if [ "$IS_TEST" = false ] && command -v raspi-config &> /dev/null; then
  sudo raspi-config nonint do_memory_split 256
fi

# 2. Bildschirmschoner deaktivieren
log "Bildschirmschoner wird deaktiviert..."
if [ "$IS_TEST" = false ]; then
  sudo raspi-config nonint do_blanking 1
  xset s off
  xset -dpms
  xset s noblank
fi

# 3. Präsentation auswählen
log "Welche Präsentation soll auf diesem RasPi laufen?"
echo "1) Der Schmied"
echo "2) Der Küfer"
echo "3) Der Wagner"
echo "4) Einwecken, Haltbarmachen, der Bäcker"
echo "5) Der Wengerter, Sensenkurs, Mühle, Imker und Sackkunde"
read -r -p "Wähle mit Taste (1/2/3/4/5): " choice

case $choice in
  1) PRESENTATION_URL="http://localhost:5000/schmied" ;;
  2) PRESENTATION_URL="http://localhost:5000/kuefer" ;;
  3) PRESENTATION_URL="http://localhost:5000/wagner" ;;
  4) PRESENTATION_URL="http://localhost:5000/einwecken" ;;
  5) PRESENTATION_URL="http://localhost:5000/wengerter" ;;
  *) PRESENTATION_URL="http://localhost:5000" ;;
esac

echo "PRESENTATION_URL=\"$PRESENTATION_URL\"" > ~/videopresi/presentation.conf

# 4. Abhängigkeiten
log "Systemaktualisierungen & Python-Abhängigkeiten..."
if [ "$IS_TEST" = false ]; then
  sudo apt-get update
  sudo apt-get install -y python3-pip python3-venv
fi

cd ~/videopresi || exit 1
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 5. systemd-Service
log "Systemd-Service wird konfiguriert..."
if [ "$IS_TEST" = false ]; then
  sudo cp systemd/keltermuseum.service /etc/systemd/system/
  sudo systemctl enable keltermuseum.service
  sudo systemctl start keltermuseum.service
fi

# 6. Neustart
log "Setup abgeschlossen!"
echo "Präsentations-URL: $PRESENTATION_URL"
read -r -p "MÖCHTEN SIE JETZT NEUSTARTEN? [y/n] " reboot_choice
if [[ "$reboot_choice" =~ ^[Yy]$ ]] && [ "$IS_TEST" = false ]; then
  sudo reboot
fi
