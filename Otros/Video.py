import tkinter as tk
import tkinter.ttk as ttk
from moviepy.editor import VideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoPlayer(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.video_frame = ttk.Frame(self)
        self.video_frame.grid(row=0, column=0)
        
        # Cargar el archivo de video
        self.video = VideoFileClip("video.mp4")
        
        # Crear un clip de video
        self.video_clip = VideoClip(self.video.duration, self.draw_frame)
        self.video_clip.fps = self.video.fps
        
        # Crear un reproductor de video
        self.video_player = self.video_clip.preview(fps=self.video.fps, fullscreen=False, 
                                                     winpos=(self.winfo_x() + self.winfo_width(), self.winfo_y()))

    def draw_frame(self, t):
        frame = self.video.get_frame(t)
        return frame

ventana = tk.Tk()
app = VideoPlayer(master=ventana)
app.mainloop()