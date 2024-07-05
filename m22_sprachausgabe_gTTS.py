import os
from gtts import gTTS

text = "Hello, how are you today?"
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")

# Play the audio file
os.system("hello.mp3")
