import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Initialize the mixer
mixer.init()

# Create the main window
root = Tk()
root.title("Python Music Player")
root.geometry("400x300")

# Define functions
def play_music():
    song = filedialog.askopenfilename(title="Select a Song", filetypes=[("Audio Files", "*.mp3")])
    if song:
        mixer.music.load(song)
        mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

# Add buttons
play_button = Button(root, text="Play", command=play_music)
pause_button = Button(root, text="Pause", command=pause_music)
resume_button = Button(root, text="Resume", command=resume_music)
stop_button = Button(root, text="Stop", command=stop_music)

play_button.pack(pady=10)
pause_button.pack(pady=10)
resume_button.pack(pady=10)
stop_button.pack(pady=10)

# Run the main loop
root.mainloop()