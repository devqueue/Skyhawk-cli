#!venv/bin/python3.8
def view():
    ""
    with open("skyhawk/services/Attendance.csv", "r") as file:
        lines = file.readlines()
        #print(lines)
        for line in lines:
            #print(line)
            attributes = line.split(",")
            #print(attributes)
            for attribute in attributes:
                print(attribute, end = "")
