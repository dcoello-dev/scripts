import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import nltk
# Record Audio
r = sr.Recognizer()
"""
with sr.Microphone() as source:
    print "Say something!"
    audio = r.listen(source)
"""
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    #said = r.recognize_google(audio, language="es-ES")
    said = "sube el volumen en 10 puntos"
    print "You said: " + said
    
    
    translator = Translator()
    said = translator.translate(src="es", dest="en", text=said)
    tokens = nltk.word_tokenize(said.text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    print entities

    tts = gTTS(text=said.text, lang="en")#lang='es-es')
    tts.save("pr.mp3")

except sr.UnknownValueError:
    print "Google Speech Recognition could not understand audio"
except sr.RequestError as e:
    print "Could not request results from Google Speech Recognition service; {0}".format(e)
