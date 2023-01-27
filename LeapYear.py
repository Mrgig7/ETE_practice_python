from datetime import date

def leap_years(start_date, end_date):
    leap_years = []
    non_leap_years = []
    for year in range(start_date.year, end_date.year+1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_years.append(year)
        else:
            non_leap_years.append(year)
    return leap_years, non_leap_years

day_1 = int(input("Enter the start date: "))
month_1 = int(input("Enter the start month: "))
year_1 = int(input("Enter the start year: "))

day_2 = int(input("Enter the end date: "))
month_2 = int(input("Enter the end month: "))
year_2 = int(input("Enter the end year: "))

start_date = date(year_1, month_1, day_1)
end_date = date(year_2, month_2, day_2)
leap_years, non_leap_years = leap_years(start_date, end_date)
print("Leap years:", leap_years)
print("Non-leap years:", non_leap_years)
