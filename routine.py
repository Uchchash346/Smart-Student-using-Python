'''import pandas as pd

a = pd.read_excel("G:\8th semester\Last project\ourroutine.xlsx", sheetname="Sheet1")
a
'''
from prettytable import PrettyTable
list1 = ['Day','Time','C.Code','C.Title','Teacher']
list2 = [["Monday","1.00PM-2.30PM","CSE322","Computer Architecture & Organization","AKMM"],
           ["Monday","2.30PM-4PM","CSE321","System Analysis and Design","NIS"],
           ["Monday","4PM-5.30PM","ECO314","Economics","SM"],
           ["Tuesday","8.30AM-10AM","CSE322","Computer Architecture & Organization","AKMM"],
           ["Tuesday","10.00AM-11.30AM","CSE321","System Analysis and Design","NIS"],
           ["Tuesday","11.30AM-1.00AM","CSE323","Operating Systems","HH"],
           ["Wednesday","10-11.30AM","ECO314","Economics","SM"],
           ["Wednesday","11.30AM-1.00PM","CSE323","Operating Systems","HH"],
           ["Thursday","8.30AM-10.00AM","CSE324","Operating Systems Lab","HH"],
           ["Thursday","10.00AM-11.30AM","CSE324","Operating Systems Lab","HH"]]

table = PrettyTable(['list1','list2'])
for x in range(0,5):
    table.add_row([list1[x],list2[x]])
print(table)

'''# Heading must be placed into string variables
Date = "Date"
Time = "Time"
Code = "C.Code"
Title = "C.Title"
Teacher ="Teacher Initial"

# Data can be placed under headings
m1 = "Monday"
m2 = "Monday"
m3 = "Monday"
t1 = "Tuesday"
t2 = "Tuesday"
t3 = "Tuesday"
w1 = "Wednesday"
w2 = "Wednesday"
th1 = "Thursday"
th2 = "Thursday"'''
