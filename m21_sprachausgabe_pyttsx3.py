"""
_summary_
"""
import pyttsx3

text = "Hello, how are you today?"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for v in voices:
    print(v)
# engine.say(text)
# engine.runAndWait()
