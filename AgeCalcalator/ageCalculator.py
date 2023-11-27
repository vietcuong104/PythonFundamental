import datetime


def ageCalculator(y, m, d):
    now = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((now - dob).days / 365.25)

    return age


day = int(input("Enter your day of birth: "))
month = int(input("Enter your month of birth: "))
year = int(input("Enter your year of birth: "))

my_age = ageCalculator(year, month, day)
print("Your age is: ", my_age)
