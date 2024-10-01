import os
import pickle
import csv
from usermap import users

README = """# team bi0s
## CTF Solves

Use `run.py` to see your solve stats. 
- Select option 1 and provide your exact username
- If you've had multiple usernames in the past, try all of them separately. 

## Team Statistics
| Username | Solves |
| --- | --- |
"""

filenames = os.listdir('solves/')
filenames = ['solves/'+i for i in filenames]
    

row_set = set()    
for file in filenames:
    for line in open(file).readlines():
        row_set.add(line.strip())
with open('allsolves.csv','w') as f:
    for row in row_set:
        if row.endswith('000'):
            f.write(row+'\n')


counts = dict()
solves_set = set()
for file in filenames:
    x = open(file).readlines()
    csv_reader = csv.reader(x, delimiter=',')
    for row in csv_reader:
        if row[-1].endswith('000'):
            solves_set.add(','.join(row))
            for username in [i.strip() for i in row[2].split(',')]:
                for k,v in users.items():
                    if username in v:
                        username = k
                        break
                if username not in counts:
                    counts[username] = 0
                counts[username] += 1


solves = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))


while True:
    ch = input("1. User solves\n2. All solves\n3. Exit\nEnter choice: ")


    if ch == '1':
        inp = input("Save to file? (y/n): ")
        if inp.lower() == 'y':
            csv_writer = csv.writer(open('usersolves.csv','w'), delimiter=',')
        csv_reader = csv.reader(open('allsolves.csv').readlines(), delimiter=',')
        name = input("Enter name: ")
        count = 0

        if name in users.keys():
            usernames = users[name]
        else:
            usernames = [name]

        for row in csv_reader:
            if len(set([r for r in row[2].split(', ')]).intersection(usernames)):
                if inp.lower() == 'y':
                    csv_writer.writerow(row)
                row_ = [i for i in row]

                for username in usernames:
                    row_[2] = row_[2].replace(username, f"\033[1;31;40m{username}\033[0m")

                print(' | '.join(row_))
                count+=1
        print("Total solves:",count)


    elif ch == '2':
        readme = open('README.md', 'w')
        readme.write(README)
        for i,j in solves.items():
            readme.write(f"| {i} | {j} |\n")
        print("README.md updated")


    elif ch == '3':
        break
    else:
        print("Invalid choice")