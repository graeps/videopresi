import customtkinter as ctk
import sys
import vlc
from PIL import Image


class VideoFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, border_width=0)
        self.grid(row=0, column=0, sticky="nesw")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.canvas = ctk.CTkCanvas(self, bg="black", highlightthickness=0, borderwidth=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")


class ProgressFrame(ctk.CTkFrame):
    def __init__(self, parent, set_video_position):
        super().__init__(parent)
        self.grid(row=1, column=0, sticky="ew", pady=15)
        self.grid_columnconfigure(1, weight=1)

        self.time_label = ctk.CTkLabel(self, text="00:00 / 00:00")
        self.time_label.grid(row=0, column=0, padx=(320, 20))

        self.progress_var = ctk.DoubleVar()
        self.progress_bar = ctk.CTkSlider(self, from_=0, to=100, variable=self.progress_var, command=set_video_position)
        self.progress_bar.grid(row=0, column=1, sticky="ew", padx=(0, 320))


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, parent, play_video, pause_video, quit_program, set_volume):
        super().__init__(parent)
        self.grid(row=0, column=1, sticky="e", padx=(0, 10))

        load_img_play = Image.open("./videoplayer/icons/play_white.png")
        load_img_pause = Image.open("./videoplayer/icons/pause_white.png")
        load_img_quit = Image.open("./videoplayer/icons/logout_white.png")
        img_play = ctk.CTkImage(dark_image=load_img_play, light_image=load_img_play, size=(30, 30))
        img_pause = ctk.CTkImage(dark_image=load_img_pause, light_image=load_img_pause, size=(30, 30))
        img_quit = ctk.CTkImage(dark_image=load_img_quit, light_image=load_img_quit, size=(30, 30))

        self.btn_play = ctk.CTkButton(self, text="", image=img_play, command=play_video, width=10)
        self.btn_pause = ctk.CTkButton(self, text="", image=img_pause, command=pause_video, width=10)
        self.btn_quit = ctk.CTkButton(self, text="", image=img_quit, command=quit_program, width=10)

        self.btn_play.grid(row=0, column=0, pady=(150, 15))
        self.btn_pause.grid(row=1, column=0, pady=15)

        load_volume_down = Image.open("./videoplayer/icons/volume_down.png")
        load_volume_up = Image.open("./videoplayer/icons/volume_up.png")
        img_volume_up = ctk.CTkImage(dark_image=load_volume_up, light_image=load_volume_up, size=(30, 30))
        img_volume_down = ctk.CTkImage(dark_image=load_volume_down, light_image=load_volume_down, size=(30, 30))

        self.volume_up_icon = ctk.CTkLabel(self, text="", image=img_volume_up)
        self.volume_up_icon.grid(row=2, column=0, pady=(100, 0))

        self.volume_var = ctk.DoubleVar(value=70)
        self.volume_slider = ctk.CTkSlider(self, from_=0, to=100, variable=self.volume_var, command=set_volume,
                                           orientation='vertical')
        self.volume_slider.grid(row=3, column=0, pady=10)
        self.volume_slider.set(70)

        volume_down_icon = ctk.CTkLabel(self, text="", image=img_volume_down)
        volume_down_icon.grid(row=4, column=0)

        self.btn_quit.grid(row=5, column=0, pady=(190, 0))


class VideoPlayer(ctk.CTk):
    def __init__(self, video):
        super().__init__()
        self.video = video
        self.attributes('-fullscreen', True)
        self.config(cursor="none")
        self._initialize_ui()
        self._initialize_vlc()
        self.update_video_progress()

    def _initialize_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.video_frame = VideoFrame(self)
        self.control_frame = ProgressFrame(self, self.set_video_position)
        self.button_frame = ButtonFrame(self, self.play_video, self.pause_video, self.quit_program, self.set_volume)
        self.canvas = self.video_frame.canvas

        self.progress_var = self.control_frame.progress_var
        self.progress_bar = self.control_frame.progress_bar
        self.time_label = self.control_frame.time_label

        self.control_frame.grid_remove()
        self.button_frame.grid_remove()
        self.controls_visible = False
        self.hide_controls_after = None

        self.canvas.bind("<Button-1>", self.toggle_controls)
        self.bind_all("<Motion>", self.show_controls_on_motion)
        self.bind("<Escape>", lambda e: self.quit_program())

    def _initialize_vlc(self):
        args = ['--no-xlib', '--vout=mmal_vout'] if sys.platform.startswith('linux') else []
        self.instance = vlc.Instance(args)
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.video)
        self.player.set_media(self.media)
        self.player.audio_set_volume(70)
        window_id = self.canvas.winfo_id()
        if sys.platform.startswith('win'):
            self.player.set_hwnd(window_id)
        elif sys.platform.startswith('linux'):
            self.player.set_xwindow(window_id)
        self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self._on_video_end)

    def play_video_buffered(self):
        if not self.player.is_playing():
            self.player.set_time(0)
            self.player.play()
            self.after(200, self.pause_video)
            self.after(300, self.player.play)

    def play_video(self):
        if self.player.get_state() == vlc.State.Paused:
            self.player.play()
        elif self.player.get_state() in (vlc.State.Stopped, vlc.State.Ended):
            self.player.set_time(0)
            self.player.play()

    def pause_video(self):
        if self.player.is_playing():
            self.player.pause()

    def quit_program(self):
        self.player.stop()
        self.quit()

    def set_video_position(self, value):
        if self.player.is_playing():
            total_duration = self.player.get_length()
            new_time = int((float(value) / 100) * total_duration)
            self.player.set_time(new_time)

    def set_volume(self, value):
        self.player.audio_set_volume(int(value))

    def update_video_progress(self):
        if self.player.is_playing():
            total_duration = self.player.get_length()
            current_time = self.player.get_time()
            if total_duration > 0:
                self.progress_var.set((current_time / total_duration) * 100)
                self.time_label.configure(
                    text=f"{self._format_time(current_time)} / {self._format_time(total_duration)}")
        self.after(1000, self.update_video_progress)

    def toggle_controls(self, event=None):
        if self.controls_visible:
            self.control_frame.grid_remove()
            self.button_frame.grid_remove()
            self.controls_visible = False
        else:
            self.control_frame.grid()
            self.button_frame.grid()
            self.controls_visible = True
            self.reset_hide_timer()

    def show_controls_on_motion(self, event=None):
        if not self.controls_visible:
            self.control_frame.grid()
            self.button_frame.grid()
            self.controls_visible = True
        self.reset_hide_timer()

    def reset_hide_timer(self, event=None):
        if self.controls_visible:
            if self.hide_controls_after:
                self.after_cancel(self.hide_controls_after)
            self.hide_controls_after = self.after(5000, self._hide_controls)

    def _hide_controls(self):
        self.control_frame.grid_remove()
        self.button_frame.grid_remove()
        self.controls_visible = False

    @staticmethod
    def _format_time(milliseconds):
        seconds = (milliseconds // 1000) % 60
        minutes = (milliseconds // 1000) // 60
        return f"{minutes:02}:{seconds:02}"

    def _on_video_end(self, event):
        self.destroy()

    @classmethod
    def start(cls, video):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("./videoplayer/color_theme.json")
        player = cls(video)
        player.after(1000, player.play_video_buffered)
        player.mainloop()