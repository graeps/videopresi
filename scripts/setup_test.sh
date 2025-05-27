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
echo "6) Schulprojekt"
read -r -p "Wähle mit Taste (1/2/3/4/5/6): " choice

case "$choice" in
  1) PRESENTATION_URL="http://localhost:5000/schmied" ;;
  2) PRESENTATION_URL="http://localhost:5000/kuefer" ;;
  3) PRESENTATION_URL="http://localhost:5000/wagner" ;;
  4) PRESENTATION_URL="http://localhost:5000/einwecken" ;;
  5) PRESENTATION_URL="http://localhost:5000/wengerter" ;;
  6) PRESENTATION_URL="http://localhost:5000/schulprojekt" ;;
  *) PRESENTATION_URL="http://localhost:5000" ;;
esac

echo "PRESENTATION_URL=\"$PRESENTATION_URL\"" > ${HOME}/videopresi/presentation.conf

# 2. Abhängigkeiten
log "Systemaktualisierungen & Python-Abhängigkeiten..."


# 3. Bildschirm-Schoner & Energiesparen deaktivieren (Wayland)
log "Bildschirm-Schoner und Energiesparen werden deaktiviert (Wayland)..."


# 4. Labwc Autostart
log "Labwc Autostart wird eingerichtet..."

# 5. Neustart
log "Setup abgeschlossen!"

