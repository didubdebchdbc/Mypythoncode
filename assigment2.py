
#N Mazzetti
#1.09.2025
#assingment


adult_price = 10
student_price = 5
child_price = 3
senior_price = 8


adults = int(input("Adults? "))
students = int(input("Students? "))
children = int(input("Children? "))
seniors = int(input("Seniors? "))
rating = input("Rating? ")


total = (adults * adult_price) + (students * student_price) + (children * child_price) + (seniors * senior_price)


if rating == "12":
    total += 2
elif rating == "15":
    total += 3
elif rating == "18":
    total += 5


print("Total bill :£", total)



