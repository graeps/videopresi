from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from vlc import *
from time import *




class FSPlayer:
    def __init__(self, video_path):
        #initialize vlc player
        self.instance = Instance("--no-xlib")
        self.player = self.instance.media_player_new()
        self.video_path = video_path

        #initialize tk root window and frames
        self.root = Tk()
        self.root.attributes("-fullscreen",True)
        self.fullscreen = 1
        self.root.geometry("800x800")

        #frame for vlc player
        self.video_frame = Frame(self.root)
        self.video_frame.pack(fill=BOTH, expand=YES)
        self.video_frame.place(relwidth=1, relheight=1)

        #embed vlc player in the video_frame
        self.player.set_xwindow(self.video_frame.winfo_id())

        #the above frame is for the purpose of embedding the video in non-fullscreen
#        self.root.bind('<space>', self.toggle_playback)
        self.root.bind('<Escape>', self.toggle_fullscreen)


#        self.button_frame=Frame(self.root,bg='green')
#        self.button_frame.pack(side=BOTTOM)
#
#        self.play_button = Button(
#            self.button_frame, 
#            text="Weiter/Pause", 
#            borderwidth=5,
#            relief="groove",
#            command=self.toggle_playback)
#        self.play_button.pack(side='left', padx=10, pady=20)
#        #button to play the video


        self.home_button = Button(
            self.root, 
            text="Menü",
            borderwidth=5,
            relief="flat",
            command=self.del_player,
            bg="white",
            fg="black")

        self.home_button.place(x=1820, y=1020)
     #   self.home_button.pack(side=BOTTOM,padx=100, pady=20)



        media = self.instance.media_new(self.video_path)

        self.player.set_media(media)
        
#        self.update_button_text()

        self.player.event_manager().event_attach(EventType.MediaPlayerEndReached, self.del_player)


    def del_player(self, event=False):
        self.root.destroy()
        self.player.stop()
        self.player.release()
        del self




    def toggle_fullscreen(self, event=False):
        if self.fullscreen == 0:
            self.fullscreen = 1
            self.root.attributes("-fullscreen", True)
        elif event and self.fullscreen==1:
            self.fullscreen = 0
            self.root.attributes("-fullscreen", False)

#    def toggle_playback(self):
#        if self.player.is_playing():
#            self.player.pause()
#        else:
#            self.player.play()
#
#        self.update_button_text()

#    def update_button_text(self):
#        if self.player.is_playing():
#            self.play_button.config(text="Weiter")
#        else:
#            self.play_button.config(text="Pause")
