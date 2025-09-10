# Opening the File For the storage purpose
with open('Storage.txt', 'w') as f:
    # Taking The Salary of User of a Month as an Input
    salary = int(input("\n Enter Your Monthly Salary = "))
    f.write("Salary = " + str(salary) + "\n")

    # Taking The Input of the Date of Entered Data
    date = int(input("\n Enter The date of Salary = "))
    f.write("Date = " + str(date) + "\n")

    # Taking The Month of The Year of Entered Data
    month = input("\n Enter The Month (In Complete Words and First Letter Capital) = ")
    f.write("Month = " + month + "\n")

    # Taking The Year as Input of Entered Data
    year = int(input("\n Enter The Year = "))
    f.write("Year = " + str(year) + "\n")

    # Setting Days of Month
    date_month = {}
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # If the Entered Year is a Leap Year
        date_month = {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
                      "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    else:  # If the Entered Year is not a Leap Year
        date_month = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
                      "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

    for key, value in date_month.items():
        f.write(f"{key} = {value}\n")
