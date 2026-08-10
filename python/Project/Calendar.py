import calendar

while True:
    year = int(input("Enter a Year:"))
    if 1800 <= year <= 2100:
        break
    print("Invalid Year. Please try again.")

while True:
    month = int(input("Enter a Month:"))
    if 1 <= month <= 12:
        break
    print("Invalid month. Please try again.")

print(calendar.month(year, month))