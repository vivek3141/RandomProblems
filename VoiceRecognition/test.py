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
    if i == " ":
        continue
    img = cv2.imread('./Data/'+str(i).upper()+'/001.jpg')
    height, width = img.shape[:2]
    img = cv2.resize(img, (int(width/3),int(height/3)), interpolation=cv2.INTER_AREA)
    cv2.imshow('image', img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
