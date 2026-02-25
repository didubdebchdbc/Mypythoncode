
# nickname
# 25.02.26
# N Mazzetti


def make_nickname(first, last):
    ft = first[0:3] # this takes the first 3 letters for the first name 
    st = last[0:3] # this takes the first 3 letters for the last name 
    print("Your nickname is", ft + st, "!") 

first = input("Enter your first name please") # asks user for first name
last = input("Enter your last name please") # asks user for last name

make_nickname(first, last) # crates user nickname