
# N Mazzetti
#24.02.26
#checking word length

# function body
def countWordLen(wordArray,num):
    counter = 0

    for i in range(0,len(wordArray)):
        if(len(wordArray[i])>=num):
            counter = counter + 1
    #end of for loop
    return counter
#end of function body

#function call
print(countWordLen(["Rondaldo","Messi","Neymar","pele"],5))
print(countWordLen(["Maradona","Buffon","Muller","Lewandoski","Cabal"],6))
print(countWordLen(["Pedri","Vithina","gavi","Neves","Locatelli"],7))

def displayContacts(contactList, letter):
    newList = []
    for i in range(len(contactList)):
        if (contactList[i][0].lower() == letter.lower()):
            newList.append(contactList[i])
    #end of loop
    return newList

print(displayContacts(["Nile","Neymar","James","Adam"], "N"))