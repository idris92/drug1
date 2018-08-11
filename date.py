'''from datetime import datetime,timedelta

mft=datetime(2018,02,15)
cft=datetime(2017,10,15)
exp=datetime(2018,04,15)

diff=exp-mft
diff2= exp-cft
if diff<=diff2:
    print ("Low")
else:
    print ("High")
print diff
print diff2
'''
import sqlite3
conn=sqlite3.connect('drug.db')
query=conn.execute("SELECT * FROM drugs")
for row in query:
    for data in row[1]:
        a=str[data]
    for data in row[2]:
        b=str[data]
    print a
    print b
    for number in a:
        for numbers in b:
            diff=number-numbers
            print (diff)

'''diff2=mft-timedelta()

if diff <= diff2:
    print ("Low")
else:
    print ("High")'''
