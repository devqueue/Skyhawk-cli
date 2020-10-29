from prettytable import PrettyTable
from prettytable import from_csv


def view():
    with open('skyhawk/services/Attendance.csv', 'r') as inf:
        table = from_csv(inf)
        print(table)





















    # with open("skyhawk/services/Attendance.csv", "r") as file:
    #     lines = file.readlines()
    #     #print(lines)
    #     for line in lines:
    #         #print(line)
    #         attributes = line.split(",")
    #         #print(attributes)
    #         for attribute in attributes:
    #             print(attribute, end = "")
    #     print('\n')
