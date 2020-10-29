from prettytable import PrettyTable
from prettytable import from_csv


def View():
    with open('skyhawk/services/Attendance.csv', 'r') as inf:
        table = from_csv(inf)
        print(table)

