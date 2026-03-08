# Video presentation – Keltermuseum Unterjesingen

Interactive video presentations running on **Raspberry Pis** in the Keltermuseum Unterjesingen.

The system displays slideshow previews of [videos in which local craftsmen and women demonstrate traditional techniques](https://www.youtube.com/@keltermuseumunterjesingen3185). Visitors can start the videos by clicking on the preview images.  
Each Raspberry Pi runs the application locally and automatically launches the presentation in **fullscreen kiosk mode** after boot.

This repository contains the **presentation software only**.  
Videos and image assets are stored separately.

---

### Project Overview

The system was developed for permanent exhibition screens in the **Keltermuseum Unterjesingen**.

Each Raspberry Pi:

- runs a small **local Flask web application**
- shows slideshow previews for available videos
- allows visitors to start videos via touchscreen
- launches automatically in **kiosk mode**
- disables screensavers and power saving
- restarts the presentation automatically after reboot

---

### Tech Stack

Backend
- Python
- Flask

Frontend
- HTML
- CSS
- JavaScript slideshow logic

System
- Raspberry Pi OS (Debian Bookworm)
- Firefox kiosk mode
- Bash setup scripts

Legacy component (currently unused)
- VLC + Tkinter video player (`old_videoplayer_ctk/`)

---

### Raspberry Pi Installation

#### Requirements

- Raspberry Pi with **Raspberry Pi OS (Debian Bookworm)**
- Internet connection
- keyboard and mouse for setup

---

#### 1. Open a terminal

Press:

CTRL + ALT + T

---

#### 2. Download the presentation software

```bash
git clone https://github.com/graeps/videopresi.git
```

The project folder should be located at:

```
/home/pi/videopresi
```

---

#### 3. Download the image assets

Download the presentation images separately from the private asset repository.

Clone the asset repository:

```bash
git clone git@github.com:graeps/videopresi-assets.git
```

Then copy the images into the project:

```bash
cp -r videopresi-assets/src/static/images /home/pi/videopresi/src/static/
```

You can delete the temporary asset repository afterwards:

```bash
rm -rf videopresi-assets
```

After this step the following folder must exist:

```
/home/pi/videopresi/src/static/images/
```

---

#### 4. Copy the video files

Video files must be placed in:

```
/home/pi/videopresi/src/static/videos/
```

**Important:**  
The filenames must exactly match the names listed in Video Naming Convention below.

---

#### 5. Run the setup script

Execute:

```bash
/home/pi/videopresi/scripts/setup.sh
```

The setup script will:

- install required system packages
- create a Python environment
- disable screensavers and power saving
- configure kiosk mode
- ask which presentation should run on this device

---

#### 6. Restart the Raspberry Pi

After reboot the system should automatically start the presentation in fullscreen mode.

Expected behaviour:

- slideshow starts automatically after <1min
- no mouse cursor visible
- no screensaver interrupts the presentation

---

#### Cursor visibility

If the cursor should be visible, edit:

```
src/static/styles/main-styles.css
```

Remove or comment out the line:

```
cursor: none;
```

---

### Project Structure

```
videopresi
├── logs
├── scripts                   # setup and startup scripts
├── src
│   ├── old_videoplayer_ctk   # legacy VLC/Tkinter player (not currently used)
│   ├── static
│   │   ├── fonts
│   │   ├── images            # slideshow images (loaded from asset repo)
│   │   ├── scripts           # JavaScript slideshow logic
│   │   ├── styles            # CSS layout
│   │   └── videos            # video files (place them here, not included in repo)
│   ├── templates             # HTML templates
│   └── videopresi_browser.py
└── systemd                   # startup configuration
```

---

### Video Naming Convention

Videos must be placed in:

```
src/static/videos/
```

and named exactly as follows.

#### Einwecken / Haltbarmachen

- haltbarmachen.mp4
- KiZweBro.mp4
- baecker.mp4

#### Küfer

- kuefer.mp4

#### Schmied

- schmied.mp4

#### Wagner

- wagner.mp4

#### Großer Monitor

- mueller.mp4
- imker.mp4
- sense.mp4
- wengerter.mp4
- sackkunde.mp4

#### Schulprojekt

- lore_koehm.mp4
- elfriede_bergmeir.mp4
- heinz_eiting.mp4
- adolf_zeeb.mp4
- heimatfilm.mp4

