#import pyttsx3
#from decouple import config

#USERNAME = config('USER')
#BOTNAME = config('BOTNAME')

#engine = pyttsx3.init('sapi5')

#set rate
#engine.setProperty('rate',150)

#set volume
#engine.setProperty('volume',1.0)

#set voice
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()