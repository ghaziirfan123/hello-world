#Name is Mohammad Irfan and peoplesoft number is 1626488
from datetime import date
def calculateAge(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
p = 1981
q = 9
r = 21
print("Birthday Calculator")
print('Current Day')
m1 = int(input('Month: '))
d1 = int(input('Day: '))
y1 = int(input('Year: '))
print('Birthday')
m2 = int(input('Month: '))
d2 = int(input('Day: '))
y2 = int(input('Year: '))
print("you are ", calculateAge(date(y1, m1, d1), date(y2, m2, d2)), "years old.")
if d1 == d2:
    print("Happy Birthday!")