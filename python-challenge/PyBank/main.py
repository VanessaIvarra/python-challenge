import os
import csv
budget_csv = os.path.join(r"C:\Users\vanes\python-challenge\PyBank\Resources\budget_data.csv")

total_months=[]
Profit_losses=[]
change_Profit=[]

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csvheader = next(csvreader)
    print(f"Header:{csvheader}")

    for row in csvreader:
        total_months.append(row[0])
        Profit_losses.append(int(row[1]))

    for i in range(len(Profit_losses)-1):
        change_Profit.append(Profit_losses[i+1]-Profit_losses[i])

    average_Changes = sum(change_Profit) / len(change_Profit)

    greatest_increase = max(change_Profit)
    greatest_increase_date = total_months[change_Profit.index(greatest_increase) + 1]
    greatest_decrease = min(change_Profit)
    greatest_decrease_date = total_months[change_Profit.index(greatest_decrease) + 1]

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(Profit_losses)}")
    print(f"Average Change: ${average_Changes:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    with open("output.txt", "w") as f:
        print("Financial Analysis", file=f)
        print("-------------------------", file=f)
        print(f"Total Months: {len(total_months)}", file=f)
        print(f"Total: ${sum(Profit_losses)}", file=f)
        print(f"Average Change: ${average_Changes:.2f}", file=f)
        print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=f)
        print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=f)










    



