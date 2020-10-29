import shutil
import os

class Clear:
    def __init__(self):
        pass
    

    def attandance():
        with open('skyhawk/services/Attendance.csv', 'w') as file:
            HEADER = "Name, Date, Time, Day "
            file.write(HEADER)

    
    def images(name):
        IMAGE_DIR = r"skyhawk/services/captured/"
        path = IMAGE_DIR+name

        try:
            shutil.rmtree(path)
            print(f"{name} user data deleted")
            print("Make sure to run 'skyhawk train' to permanently remove user data")
        except OSError as e:
            print("Error: %s : %s" % (path, e.strerror))
            
