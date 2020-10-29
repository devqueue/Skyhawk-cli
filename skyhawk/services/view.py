from prettytable import PrettyTable
from prettytable import from_csv
import os

class Viewer:
    def __init__(self):
        pass


    def view():
        with open('skyhawk/services/Attendance.csv', 'r') as inf:
            table = from_csv(inf)
            print(table)

    def users():
        path = "skyhawk/services/captured"
        dir_content = os.listdir('skyhawk/services/captured')
        users = []
        for filename in dir_content:
            if filename.endswith(".py"):
                pass
            else:
                users.append(filename)
        table = PrettyTable(['users'])
        for x in range(len(users)):
            table.add_row([users[x]])
        print(table)

