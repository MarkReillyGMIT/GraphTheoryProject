# GraphTheoryProject
  A Python program to execute regular expressions on strings using an algorithm known as Thompson’s construction.
## Mark Reilly 

## Running Program
`git clone https://github.com/MarkReillyGMIT/GraphTheoryProject`

`cd GraphTheoryProject`

`cd Project`

`python main.py --Run`

The program will promt the user to input a regular expression, e.g "a.b|b*"

Next, the program will prompt the user to enter a string, e.g "bbb"

The program will return if the string matches or does not match the regular expression.

## How the program works:
* Once the user has entered the Regular Expression and the input string, the match function is called from the file "thompsonConstruction.py" and passed the regular expression and input string as parameters.

* The first thing the match() function will do is call compile() and take the regex as a parameter.

* Next, the method will take the infix regex and return the postfix, using the shunt() class.

* Next, the postfix will be converted to a stack of characters.

* Next, the stack of characters are put through a series of if/elif statements, characters from the postfix and the Fragment and State classes are used to create the new NFA.

* Next, in match() the followes() method is called which takes in the current state and the state to be checked. The followes method ensures all the epsilons edges are followed.Edges labelled with epsilon are represented with None in thompsonConstruction.py

* The match method will then loop through all the characters in the string. Depending on if the last state is the accept state , the match function will ask the NFA if it matches the string.

## Running the tests
![alt text](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Image/GraphTheory.PNG "True")

![alt text](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Image/GraphTheoryFalse.PNG "False")

## Research
The following helped me to understand regular expressions to NFA's:
https://www.youtube.com/watch?v=RYNN-tb9WxI

The following helped me to understand '+' One or more and '?' Zero or one and how to implement them:
https://swtch.com/~rsc/regexp/regexp1.html

The folowing helped me with user input:
https://www.geeksforgeeks.org/taking-input-in-python/

The following helped with adding command line arguements:
https://www.geeksforgeeks.org/command-line-arguments-in-python/
