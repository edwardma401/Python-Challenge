import os

from csv import reader 
with open("Resources/budget_data.csv") as read_obj: 
    csv_reader = reader(read_obj) 
    total = 0
    next(csv_reader)
    for row in csv_reader:
        total += int(row[1])
print(total)

from csv import reader    
with open("Resources/budget_data.csv") as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    totalmonths = len(list_of_rows[1:])
print(totalmonths)


totaldifference = 0
difference = 0

from csv import reader    
with open("Resources/budget_data.csv") as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)
    for i in csv_reader:
        index = i[1]

    with open("Resources/budget_data.csv") as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row[1] != "Profit/Losses":
                difference = int(row[1]) - int(i[1])  
                totaldifference += difference
                differnece = 0

averagechange = totaldifference / (totalmonths - 1)
averagechange = round(averagechange, 2)
print(averagechange)

from csv import reader    
with open("Resources/budget_data.csv") as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)
    greatestincrease = max(csv_reader, key=lambda row: int(row[1]))
print(greatestincrease)

from csv import reader    
with open("Resources/budget_data.csv") as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)
    greatestdecrease = min(csv_reader, key=lambda row: int(row[1]))
print(greatestdecrease)


print(f"""
Financial Analysis
-------------------------------
Total Monts: {totalmonths}
total: {total}
Average Change : {averagechange}
Greatest Increase in Profits : {greatestincrease}
Greatest Decrease in Profits : {greatestdecrease}
""", end="")

os.getcwd()
os.chdir('C:\\Users\\mahoy\\Documents\\GitHub\\Python-Challenge\\PyBank\\analysis')

result_txt = open("Result.txt", "w", encoding='utf-8')
print(f"""
Financial Analysis
-------------------------------
Total Monts: {totalmonths}
total: {total}
Average Change : {averagechange}
Greatest Increase in Profits : {greatestincrease}
Greatest Decrease in Profits : {greatestdecrease}
""", file=result_txt)
result_txt.close()

