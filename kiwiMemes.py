import json
from moviepy.editor import *
import os
import random
import time

# Path to the config.json file
config_file_path = "config.json"

# Read the JSON data from the file
with open(config_file_path, "r") as file:
    config_data = json.load(file)

# Access specific values from the config_data dictionary
remove_background_audio = config_data.get("removeBackgroundAudio", False)
h = config_data.get("height", 0)
w = config_data.get("width", 0)


background_folder = "backgrounds/"
memes_folder = "memes/"
output_folder = "output/"

print(
    f"""
      ================KiwiMemes================
              Create meme videos faster
      =========================================
      Settings: width: {w}, height: {h},
                remove background audio: {remove_background_audio}
      \n\n\n
    """
)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("->Output folder created!")
background_videos = os.listdir(background_folder)
memes = os.listdir(memes_folder)

for meme in memes:
    background_video_path = os.path.join(
        background_folder, random.choice(background_videos)
    )
    background_clip = VideoFileClip(background_video_path)

    if remove_background_audio:
        background_clip = background_clip.set_audio(None)
        print("-> Audio removed")

    meme_path = os.path.join(memes_folder, meme)
    meme_clip = ImageClip(meme_path)

    meme_width = int(w * 0.8)
    meme_height = int(meme_clip.h * meme_width / meme_clip.w)
    x = int((w - meme_width) / 2)
    y = int((h - meme_height) / 2)

    # Resize and position the meme on the background
    meme_clip = meme_clip.set_duration(background_clip.duration).resize(
        width=meme_width
    )
    final_clip = CompositeVideoClip([background_clip, meme_clip.set_pos((x, y))])

    # Write the final video with the meme to the output folder
    final_video_path = os.path.join(output_folder, f"output_{meme}.mp4")

    final_clip.write_videofile(final_video_path, codec="libx264", fps=24)

print(
    """
    =========================================
                    FINISHED 
    =========================================
    Programm will close in 4 seconds
    """
)

time.sleep(4)
