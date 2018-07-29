#Simple program to find the nth element from a sentence based on start as true or false

def reverseString(sentence):
    reversed=[] #create empty list
    for i in range(len(sentence),0,-1): #starting from end, push each character of sentence into list as a character
        reversed.append(sentence[i-1])
    return "".join(reversed)  #join the individual character elements of a list into a string

print(reverseString("My name is xyz")) #returns zyx si eman yM
print(reverseString("Banana")) #returns  ananaB
print(reverseString("BeE")) #returns  EeB