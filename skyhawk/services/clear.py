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
            print("Error: %s : %s" % (e.strerror))
            print("Make sure to run 'skyhawk init' before clearing a file")

    
    def images(name):
        IMAGE_DIR = r"skyhawk/facedata/"
        path = IMAGE_DIR

        try:
            shutil.rmtree(path)
            print(f"User data deleted")
        except OSError as e:
            print("Error: %s : %s" % (path, e.strerror))
            print("Enter the name of the user to clear data")
            
