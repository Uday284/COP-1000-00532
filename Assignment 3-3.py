import calendar  

year = int(input("Enter a year: "))  
month = int(input("Enter a month (1-12): "))  
day = int(input("Enter a day: "))  

if year > 0 and 1 <= month <= 12:
    max_days = calendar.monthrange(year, month)[1]
    
    if 1 <= day <= max_days:
        print(f"{month}/{day}/{year} is a valid date")
    else:
        print(f"{month}/{day}/{year} is an invalid date")
else:
    print(f"{month}/{day}/{year} is an invalid date")
