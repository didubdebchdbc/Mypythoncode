
#while1
#N mazzetti
#2 sep

print("Enter your age[18-50 only]:")
Age=int(input())

while(Age <18 or Age>50):
    print("Invalid age. 18-50 only allowed.")
    Age = int(input())

print(Age, "is a valid entry!")





print("Enter your choice [y/n ONLY]:")
choice = input()

while (choice.lower()!="y" or choice.lower()!="n"):
    print("Only y/n allowed. Re-enter:")
    choice = input()

print("Succesful entry")