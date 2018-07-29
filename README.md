# pythonExample-1
This is a simplae python example to show for loop and if statement
This function takes a sentence, position and start parameter and returns the position word from the start or end depending on the parameter
Sample input 1:  findNthWord("My name is xyz", 2, true) returns "name"
Sample input 2:  findNthWord("My name is xyz", 2, false) returns "is"

Some more examples below
findNthWord("My name is xyz", 4, False)    returns My
findNthWord("My name is xyz", 2, True)    returns name
findNthWord("My name is xyz", 2, False)    returns is
findNthWord("My name is xyz", 4, True)    returns xyz
findNthWord("My name is xyz", 0, True)    returns NULL
findNthWord("My name is xyz", 5, True)    returns NULL
