import time
import playsound
import os
import random
from gtts import gTTS

audio_str = "mohit"


class TextToSpeech(object):

    def text2speech(self, audio_str=None):
        text=gTTS(text=audio_str, lang='en')
        gg=random.randint(1, 1000009)
        audio_file='audio'+str(gg)+'.mp3'
        text.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_str)
        # os.remove(audio_file)

text_to_speech = TextToSpeech()
text_to_speech.text2speech("hello")