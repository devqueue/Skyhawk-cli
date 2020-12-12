import os
from skyhawk.misc.colors import COLORS,colorText


def run():
    current_dir = os.getcwd()
    faces_dir = "skyhawk/facedata"
    bin_dir = "skyhawk/bin"
    face_path = os.path.join(current_dir,faces_dir)
    bin_path = os.path.join(current_dir,bin_dir)
    os.makedirs(face_path, exist_ok=True)
    os.makedirs(bin_path, exist_ok=True)
    with open('skyhawk/bin/Attendance.csv', 'w') as file:
        HEADER = "Name, Date, Time, Day "
        file.write(HEADER)
    with open('skyhawk/bin/trainer.py','w') as py:
      code = '''
import cv2
import os
import numpy as np
from PIL import Image
import pickle

def Facetrainer():
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  direc = "../facedata"
  image_dir = os.path.join(BASE_DIR, direc)
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  current_id = 0
  label_ids = {}
  y_labels = []
  x_train = []

  for root, dirs, files in os.walk(image_dir):
    for file in files:
      if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
        path = os.path.join(root, file)
        label = os.path.basename(root).replace(" ", "-").lower()
        #print(label, path)
        if not label in label_ids:
          label_ids[label] = current_id
          current_id += 1
        id_ = label_ids[label]
        #print(label_ids)
        pil_image = Image.open(path).convert("L")  # grayscale
        size = (200, 200)
        final_image = pil_image.resize(size, Image.ANTIALIAS)
        image_array = np.array(final_image, "uint8")
        #print(image_array)
        faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
          roi = image_array[y:y+h, x:x+w]
          x_train.append(roi)
          y_labels.append(id_)

  #print(y_labels)
  #print(x_train)

  with open("skyhawk/bin/face-labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

  recognizer.train(x_train, np.array(y_labels))
  recognizer.save("skyhawk/bin/face-trainner.yml")
  print("Training completed")


if __name__ == "__main__":
    Facetrainer()
'''
      py.write(code)

    header = "[[green]]            Welcome to skyhawk! Auto-attandance cli tool      "
    footer = "[[white]]Data directories initialized sucessfully"
    Logo = '''[[cyan]]
                                                                                                        
                                   -://-`                                               
                                 /dNMMMNmo`                                             
                                +MMMy+sNMMy                                             
                                hMMm`  yMMN`                                            
                      .--.`     :NMMmhdMMNo      .-:-`                                  
                    :hNNNNd/     -sdMMMmy:     :hNNNNd+                                 
                   -NMd::yMM:     .sNMMh-     .NMd:-yMM/                                
                   -NMd::hMM:    :mMMMMMN+    .NMm::yMM/                                
            `.`     :hNNNMm/     :MMMMMMMo     :dMMNNd+     `..                         
          -ymdmh:    `.:mMNho.   `mMMMMMM-   `+ymMN+.`    .yddmh/                       
         `mMo-+MN.     yMMMMMy    sMMMMMd    +MMMMMd`     dMs-/NN-                      
          yMdohMd`     +NMMMMm    -MMMMM+    yMMMMMs`    `yMdoyMd`                      
          `:oysNmdh/    /NMMMM.    dMMMN.   `mMMMMs`   :hdmMyys/`                       
              .NMMMN/    /NMMM/    +MMMy    -MMMMo    -mMMMM/                           
              `/dMMMN/    :mMMy    .NMM:    +MMN+    -mMMMmo`                           
                `/dMMN:    -mMm`    hMm`    yMN/    .mMMm+.                             
                  `/hNm-    -mM.    /Ms    `mN/    .dMd+`                               
                     :hd-    .d/    `m-    .m:    `hd/`                                 
                      `:o`    ./     :     :-    `+d`                                    
                                                                                                     
    '''
    print('\n')
    print(colorText(header))
    print(colorText(Logo))
    print(colorText(footer))
    print('\n')
