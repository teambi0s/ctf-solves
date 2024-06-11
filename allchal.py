import os
import pickle
import csv

filenames = os.listdir('solves/')
filenames = ['solves/'+i for i in filenames]
    
row_set = set()    
for file in filenames:
    for line in open(file).readlines():
        row_set.add(line.strip())
with open('allchalls.csv','w') as f:
    for row in row_set:
        f.write(row+'\n')

csv_reader = csv.reader(open('allchalls.csv').readlines(), delimiter=',')
uname = input("Username: ").lower()
total = 0
solved = 0
for row in csv_reader:
    if uname in row[2].lower():
        # print(' | '.join(row))
        total += 1
        if row[-1].endswith('000'):
            solved += 1
print("Total solves:",solved,"/",total)