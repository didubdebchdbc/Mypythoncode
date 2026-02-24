
#M Nico driver / R Sebastian Navigator
#27.08.2025
# Challenge 1

name = input (" What is you name")


print("Welcome to the c-f - f-c converter,",name)

print("select 1 if you want c-f or select 2 if you want f-c") #
ch = int(input())

if (ch <2 or ch >1):
    print("Error! cannot function, list choices 1 or 2 only")

if(ch==1):
    c = float(input ("State your value in celsius"))
    f = (c * 9/5) + 32
    print(c, "Celsius is ", f, "Fahrenheit")

print("select 1 if you want c-f or select 2 if you want f-c")
ch = int(input())

if (ch <2 or ch >1):
    print("Error! cannot function, list choices 1 or 2 only")

if(ch==2):
    f = float(input ("State your value in fahrenheit"))
    c = (f - 32) * 5/9.
    print(f, "Fahrenheit is ", c, "Celsius")


