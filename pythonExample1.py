#import sys
#Simple program to find the nth element from a sentence in forward or reverse direction


#import sys
#Simple program to find the nth element from a sentence

#This function takes a sentence, position and start parameter and returns the position word from the 
# start or end depending on the parameter
#Sample input 1:  findNthWord("My name is xyz", 2, true) returns "name"
#Sample input 2:  findNthWord("My name is xyz", 2, false) returns "is"
def findNthWord(sentence, position, start):
	words = sentence.split(' ')
	if(position < 1 or position > len(words)):
		return "NULL"		
	elif(start == True):
		return words[position-1]
	else:
		return words[len(words)-position]		

print(findNthWord("My name is xyz", 4, False)) #returns My
print(findNthWord("My name is xyz", 2, True)) #returns name
print(findNthWord("My name is xyz", 2, False)) #returns is
print(findNthWord("My name is xyz", 4, True)) #returns xyz
print(findNthWord("My name is xyz", 0, True)) #returns NULL
print(findNthWord("My name is xyz", 5, True)) #returns NULL
