import speech_recognition as sr
AF = ("10_OCTOBER/billo.wav")
r = sr.Recognizer()

with sr.AudioFile(AF) as source:
    audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Sorry, I did not get that.")