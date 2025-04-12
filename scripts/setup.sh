#!/bin/bash

log() {
  echo "[INFO] $1"
}

# 1. Präsentation auswählen
log "Welche Präsentation soll auf diesem RasPi laufen?"
echo "1) Der Schmied"
echo "2) Der Küfer"
echo "3) Der Wagner"
echo "4) Einwecken, Haltbarmachen, der Bäcker"
echo "5) Der Wengerter, Sensenkurs, Mühle, Imker und Sackkunde"
read -r -p "Wähle mit Taste (1/2/3/4/5): " choice

case "$choice" in
  1) PRESENTATION_URL="http://localhost:5000/schmied" ;;
  2) PRESENTATION_URL="http://localhost:5000/kuefer" ;;
  3) PRESENTATION_URL="http://localhost:5000/wagner" ;;
  4) PRESENTATION_URL="http://localhost:5000/einwecken" ;;
  5) PRESENTATION_URL="http://localhost:5000/wengerter" ;;
  *) PRESENTATION_URL="http://localhost:5000" ;;
esac

echo "PRESENTATION_URL=\"$PRESENTATION_URL\"" > ${HOME}/videopsresi/presentation.conf

# 2. Abhängigkeiten
log "Systemaktualisierungen & Python-Abhängigkeiten..."
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv

cd ${HOME}/videopresi || exit 1
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. systemd-Service
log "Systemd-Service wird konfiguriert..."
mkdir ${HOME}/.config/systemd/user/
sudo cp systemd/keltermuseum.service ${HOME}/.config/systemd/user/
sudo systemctl --user enable keltermuseum.service
sudo systemctl --user start keltermuseum.service


# 4. Bildschirm-Schoner & Energiesparen deaktivieren (Wayland)
log "Bildschirm-Schoner und Energiesparen werden deaktiviert (Wayland)..."

# Disable power-saving using gsettings (works with Wayland+GNOME schema)
gsettings set org.gnome.desktop.session idle-delay 0
gsettings set org.gnome.desktop.screensaver lock-enabled false
gsettings set org.gnome.desktop.screensaver idle-activation-enabled false

# Mask suspend/hibernate
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

# Disable console blanking
sudo sed -i '/^consoleblank=/d' /boot/config.txt
echo 'consoleblank=0' | sudo tee -a /boot/config.txt > /dev/null

# 5. Neustart
log "Setup abgeschlossen!"
echo "Präsentations-URL: $PRESENTATION_URL"
read -r -p "MÖCHTEN SIE JETZT NEUSTARTEN? [y/n] " reboot_choice
if [[ "$reboot_choice" =~ ^[Yy]$ ]]; then
  sudo reboot
fi
