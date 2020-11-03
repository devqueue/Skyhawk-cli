import cv2
import os
import string
import random

class Capture:
    def __init__(self):
        pass

    def color():
        def get_random_string(length):
            # Random string with the combination of lower and upper case
            letters = string.ascii_letters
            result_str = ''.join(random.choice(letters) for i in range(length))
            return result_str

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        name = input("Name: ")
        pics = int(input("No. of images: "))
        count = 0
        cap = cv2.VideoCapture(0)
        k = cv2.waitKey(100) & 0xff
        suffix = random.randint(1, 10)

        print("\n[INFO] Initializing face capture. Look the camera and wait ...")

        def face_ext(img):
            gray = frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            if faces is():
                return None

            for(x, y, w, h) in faces:
                cropped_face = img[y:y+h, x:x+w]

            return cropped_face

        while True:
            re, frame = cap.read()
            if face_ext(frame) is not None:
                count += 1
                face = cv2.resize(face_ext(frame), (200, 200))
                #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                #path = os.path.abspath(os.path.join(os.path.dirname(__file__), "services/captured/"))
                path = os.path.join(os.getcwd(),'skyhawk/facedata/', f'{name}')
                file_path = os.path.join(path, str(count) + get_random_string(suffix) + '.jpg')
                print(file_path)
                if os.path.exists(path):
                    cv2.imwrite(file_path, face)

                elif not os.path.exists(path):
                    os.makedirs(path)
                    cv2.imwrite(file_path, face)
                cv2.putText(face, str(count), (50, 50),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
                cv2.imshow('Data Collector', face)

            else:
                pass

            if k == 27 or count == pics:
                break
        print("\n[INFO] Exiting Program and cleanup stuff")
        cap.release()
        cv2.destroyAllWindows()
        print("INFO] Dataset Collection Completed")
        


    def black():
        def get_random_string(length):
            # Random string with the combination of lower and upper case
            letters = string.ascii_letters
            result_str = ''.join(random.choice(letters) for i in range(length))
            return result_str
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        name = input("Name: ")
        pics = int(input("No. of images: "))
        count = 0
        cap = cv2.VideoCapture(0)
        k = cv2.waitKey(100) & 0xff
        suffix = random.randint(1,10)

        print("[INFO] Initializing face capture. Look the camera and wait ...")


        def face_ext(img):
            gray = frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            if faces is():
                return None

            for(x, y, w, h) in faces:
                cropped_face = img[y:y+h, x:x+w]

            return cropped_face


        while True:
            re, frame = cap.read()
            if face_ext(frame) is not None:
                count += 1
                face = cv2.resize(face_ext(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                path = os.path.join(os.getcwd(),'skyhawk/facedata', f'{name}')
                file_path = os.path.join(path, str(count) + get_random_string(suffix) + '.jpg')
                print(file_path)
                if os.path.exists(path):
                    cv2.imwrite(file_path, face)
                elif not os.path.exists(path):
                    os.makedirs(path)
                    cv2.imwrite(file_path, face)
                cv2.putText(face, str(count), (50, 50),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
                cv2.imshow('Data Collector', face)

            else:
                pass

            if k == 27 or count == pics:
                break
        print("[INFO] Exiting Program and cleanup stuff")
        cap.release()
        cv2.destroyAllWindows()
        print("Dataset Collection Completed")
