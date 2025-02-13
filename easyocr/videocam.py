import cv2
from imagetotext import imagetotext
import easyocr
import pyttsx3

# cap = cv2.VideoCapture(1)

# while(cap.isOpened()):  
#     ret,frame = cap.read()

#     if not ret:
#         print("Exit")
#         break  
#     cv2.imwrite('frame.png',frame)
    
#     break

frame = 'pic.png'

def imagetotext():
    reader=easyocr.Reader(['en'])
    results= reader.readtext(frame)
    data=''
    for (bbox,text,conf) in results:
        data+=(text+' ')

    return data


engine = pyttsx3.init()


engine.setProperty('rate', 100)  
engine.setProperty('volume', 1)


text = imagetotext()


engine.say(text)


engine.runAndWait()









