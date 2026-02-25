
# N Mazzetti
# 25.02.26
# Movie ticket

def check(age):
    if ((age)<=12):
        return 8
    if ((age)>=12 and (age)<=18):
        return 10
    if ((age)>=18):
        return 15


age = int(input("Enter your age"))
print(check(age))

