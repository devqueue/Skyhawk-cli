import os

def run():
    current_dir = os.getcwd()
    faces_dir = "skyhawk/facedata"
    bin_dir = "skyhawk/bin"
    face_path = os.path.join(current_dir,faces_dir)
    bin_path = os.path.join(current_dir,bin_dir)
    os.makedirs(face_path, exist_ok=True)
    os.makedirs(bin_path, exist_ok=True)
    print("Data directories initialized")
    with open('skyhawk/bin/Attendance.csv', 'w') as file:
        HEADER = "Name, Date, Time, Day "
        file.write(HEADER)
