
#N Mazzetti
#18.02.26
#Fuction challange

def printWord(w,t):
    for i in range(t):
        print(w)

printWord("Hello",15)
printWord("ISA",200)


def generateTable(num,times):
    for i in range(1,times+1):
        print(num,"X",i,"=",num*i)

generateTable(10,5) # 10 is the coin and travels to num, 5 travels to i which chnages each time
generateTable(7,12)



Firstname = input ("What is your first name")
Lastname = input ("What is your last name")

print(Firstname,Lastname) # create 2 inputs and ask the user for there first and last name and then print first and last name

n1 = input ("What number do you want to add")
n2 = input ("give me another number")
sym = input ("What symbol do you want me to calculate it in")


def calculate(n1, n2, sym):
    if(sym =="+"):
        print(n1, "+" ,n2, "=" ,n1+n2)
    if(sym =="-"):
        print(n1, "-" ,n2, "=" ,n1-n2)
    if(sym =="*"):
        print(n1, "*" ,n2, "=" ,n1*n2)
    if(sym =="/"):
        print(n1, "/" ,n2, "=" ,n1/n2)


calculate(n1,n2,sym)
