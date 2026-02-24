
#17.02.26 - N Mazzetti
#functions - 1
#print a line of stars

def starLine():
    print("********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************")


def anyline(c, l):
    for i in range(1):
        print(c, end = " ")
    print()

anyline("_",20)
print("Hello there")
anyline("@",30)

def greetingName(N):
    print("Hello", N)

N = input("Enter Name")

greetingName(N)

def greetingTime(name,time):
    if(time>=8 and time<=12):
        print("Good morning", name)
    elif(time>=1 and time<=3):
        print("Good afternoon",name )
    else:
        print("Good Morning",name)


anyline("-",20)
print("Hello There")
anyline("@",30)

greetingTime("Jhon",10)
greetingTime("Jane",4)
greetingTime("Adam",1)

