import numpy as np
import cv2
import pickle
import os
from datetime import datetime


def run():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read("skyhawk/bin/face-trainner.yml")

    def markattendance(name):
        with open('skyhawk/bin/Attendance.csv', 'r+') as f:
            dataList = f.readlines()
            nameList = []
            for line in dataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                date = now.strftime('%b %d %Y')
                day = now.strftime('%a')
                time = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name}, {date}, {time}, {day}')

    labels = {"person_name": 1}
    with open("skyhawk/bin/face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        _ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
            _roi_color = frame[y:y+h, x:x+w]
            #print(w, h)

            # recognize
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 4 and conf <= 85:
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                colortext = (255, 255, 255)
                colorframe = (255, 0, 0)
                stroke = 2
                cv2.rectangle(frame, (x, y), (x + w, y + h),
                              colorframe, stroke)
                cv2.rectangle(frame, (x, y+h), (x+w, y+h+20),
                              colorframe, stroke)
                cv2.rectangle(frame, (x, y+h), (x+w, y+h+20),
                              colorframe, cv2.FILLED)
                cv2.putText(frame, name, (x, y+h+20),
                            font, 0.70, colortext, stroke)
                markattendance(name)

                #img_item = "7.png"
                #cv2.imwrite(img_item, _roi_color)

        # Display the resulting frame
        cv2.imshow('Face-detector', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


