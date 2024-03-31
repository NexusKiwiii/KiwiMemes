
# KiwiMemes

Create simple meme-videos

For each meme (in the `memes` folder) it will take a random background video (from the `backgrounds` folder).
Based on your `config.json` it will remove the background audio.

## Installation

You only need moviepy and the script

![App Screenshot](https://raw.githubusercontent.com/NexusKiwiii/KiwiMemes/main/preview.png)

```bash
    pip install moviepy
```
    
after downloading you have to create a `config.js` in the same directory:

```json
{
    "removeBackgroundAudio": false,
    "height": 1920,
    "width": 1080
}
```

You should only set `removeBackgroundAudio` to true if your backgrounds have audio (or atleast 1). Don't enable it if you want the background audio or your backgrounds don't have audio.

Create a `memes` and `backgrounds` folder where you put all the backgrounds and memes. They dont need any specific name or smth.

After running the script it will automatically create a output folder with the meme-videos.

**Examples** can be found **on my TikTok**: https://www.tiktok.com/@nexus.kiwi
