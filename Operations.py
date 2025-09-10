# Importing All The Inputs
from Inputs import salary, date, month, year, date_month

# Open Storage.txt in write mode
with open('Storage.txt', 'w') as f:
    # Here you can write the header or any initial content to the file if needed.

    # Calculating Individual Expenses of the day
    def expense_inputs(n):
        total_expenditure = 0
        for i in range(n):
            detail = input("\n Your Expense Detail = ")
            f.write("Detail = " + detail + "\n")

            units_bought = int(input("\n Enter Input of Product = "))
            f.write("N = " + str(units_bought) + "\n")

            expense = int(input("\n Expense Done (in Rupees) = "))
            f.write("Expense = " + str(expense) + "\n")

            total_expenditure += units_bought * expense

        return total_expenditure

    # Taking Days in a month of Year
    days_of_month = date_month[month]

    while date in range(date_month[month]) or salary >= 0:
        
        if (salary == 0):#If salary is finished or not given
            date_month[month] = 0
            print("\n You don't have balance to have expenses. Sorry!!!!")
            break
        
        else:
            f.write(f"\n Today's Date = {date} {month} {year}")
            remaining_days = days_of_month - date - 1

            n = int(input("\n Times Expenditure is done = "))
            result = expense_inputs(n)

            f.write(f"\n Your's Today Expenditure = {result}")
            salary -= result

            f.write(f"\n Alert!!!!! \n Your Salary Left = {salary} \n Days in Month Left = {remaining_days}")

            date += 1
        
