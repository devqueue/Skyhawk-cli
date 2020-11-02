import shutil
import os

class Clear:
    def __init__(self):
        pass
    

    def attandance():
        try:
            with open('skyhawk/bin/Attendance.csv', 'w') as file:
                HEADER = "Name, Date, Time, Day "
                file.write(HEADER)
        except FileNotFoundError as e:
            print("Error: %s : %s" % (path, e.strerror))
            print("Make sure to run 'skyhawk init' before clearing a file")

    
    def images(name):
        IMAGE_DIR = r"skyhawk/facedata/"
        path = IMAGE_DIR+name

        try:
            shutil.rmtree(path)
            print(f"{name} user data deleted")
            print("Make sure to run 'skyhawk train' to permanently remove user data")
        except OSError as e:
            print("Error: %s : %s" % (path, e.strerror))
            
