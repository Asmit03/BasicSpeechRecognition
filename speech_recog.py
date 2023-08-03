import speech_recognition as sr

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
keyword = "alpha"

r = sr.Recognizer()
r.energy_threshold = 300

with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Speak Now: ")
    audio = r.listen(source)

try:
    txt = r.recognize_google(audio, language="en-US")
    print("Keyword Present" if keyword in txt else "Keyword Absent")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
