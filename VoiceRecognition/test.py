import speech_recognition as sr
import cv2
import numpy as np
text = ""
r = sr.Recognizer()
with sr.Microphone(device_index=1, sample_rate=48000,
                   chunk_size=2048) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said: " + text)
        pass
    except sr.UnknownValueError:
        print("Can't understand")

    except sr.RequestError as e:
        print("Connect to internet")
for i in text.rstrip():
    img = cv2.imread('./Data/'+str(i).upper()+'/001.jpg')
    img = cv2.resize(img, (640,480), interpolation=cv2.INTER_AREA)
    cv2.imshow('image', img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()





