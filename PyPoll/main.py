# The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#                                             row[0]   row[1]      row[3]

import os
<<<<<<< HEAD
=======

>>>>>>> e2cef246cdab6884a8e6ea0892fd9b1d194faf79

# The total number of votes cast

from csv import reader 
with open("Resources/electron_data.csv") as read_obj: 
    csv_reader = reader(read_obj) 
    csv_reader = list(csv_reader)
    totalvotes = len(csv_reader[1:])

# A complete list of candidates who received votes
vforkhan = 0
vforcorrey = 0
vforli = 0
vfortooly = 0
candidates = []

from csv import reader 
with open("Resources/electron_data.csv") as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)
    for row in csv_reader:
        if str(row[2]) == "Khan":
            vforkhan += 1
        elif str(row[2]) == "Correy":
            vforcorrey += 1
        elif str(row[2]) == "Li":
            vforli += 1
        else:
            vfortooly += 1
    candidates.append(vforkhan)
    candidates.append(vforcorrey)
    candidates.append(vforli)
    candidates.append(vfortooly)
    winner = max(candidates)
    if vforcorrey == winner:
        thewinner = "Khan"
    elif vforli == winner:
        thewinner = "Li"
    elif vfortooly == winner:
        thewinner = "O'Tooley"
    elif vforkhan == winner:
        thewinner = "Khan"
kpercent = "{:.3f}".format(vforkhan / totalvotes * 100)
cpercent = "{:.3f}".format(vforcorrey / totalvotes * 100)
lpercent = "{:.3f}".format(vforli / totalvotes * 100)
opercent = "{:.3f}".format(vfortooly / totalvotes * 100)

print(f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
Khan: {kpercent}% ({vforkhan})
Correy: {cpercent}% ({vforcorrey})
Li: {lpercent}% ({vforli})
O'Tooley: {opercent}% ({vfortooly})
-------------------------
Winner: {thewinner}
-------------------------
""")

os.chdir('C:\\Users\\mahoy\\Documents\\GitHub\\Python-Challenge\\PyPoll\\analysis')
Result_txt = open("Result.txt", "w", encoding='utf-8')

print(f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
Khan: {kpercent}% ({vforkhan})
Correy: {cpercent}% ({vforcorrey})
Li: {lpercent}% ({vforli})
O'Tooley: {opercent}% ({vfortooly})
-------------------------
Winner: {thewinner}
-------------------------
""", file=Result_txt)

Result_txt.close()
