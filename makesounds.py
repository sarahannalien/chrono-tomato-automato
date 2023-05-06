from gtts import gTTS
import os

def text_to_wav(text, output_file):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(output_file)

    # Convert mp3 to wav using ffmpeg (if available)
    if os.system("ffmpeg -version") == 0:
        os.system(f"ffmpeg -i {output_file} -acodec pcm_s16le -ac 1 -ar 16000 {output_file.replace('.mp3', '.wav')}")
        os.remove(output_file)

text_to_wav("It's time to work!", "sounds/work_sound.mp3")
text_to_wav("Enjoy your break!", "sounds/break_sound.mp3")

