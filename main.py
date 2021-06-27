from moviepy.editor import VideoFileClip

clip = VideoFileClip("game.mp4")
clip.write_gif("mygif.gif", fps=10)