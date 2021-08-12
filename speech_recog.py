# pip install SpeechRecognition
import speech_recognition as sr

#use lsusb to see microphone device id
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"  

#chunk_size determines the audio input length from the source
sample_rate = 48000
chunk_size = 4096

r = sr.Recognizer()
r.energy_threshold = 300
  
#speech input and recognition
with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
    
    r.adjust_for_ambient_noise(source)
    print ("Speak Now: ")
    print ()
    
    audio = r.listen(source)
          
    try:
        txt = r.recognize_google(audio, language="en-US")
      
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
      
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#split output into a list and display each element
#remove the split function to look for keyword in the string directly
try:
    look = txt.split()
    for i in look:
        print(i)
except:
    print ()

#parsing the text for keyword detection
print()
try:
    if any("point" in word for word in look):
        print('Keyword Present')
        print()
    else:
        print('Keyword Absent')
        print()
except:
    print()