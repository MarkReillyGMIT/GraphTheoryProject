# Mark Reilly - G00357230

# Graph Theory Report

# Introduction
Welcome everyone to my Graph Theory Project's overview, inside this document I will have a brief introduction on my project and how the code works, then I will discuss how to download and run my code from GitHub in detail and also how download and setup python on your machine. After this I will discuss how testing is incorporated into my code, and the relevance and importance of testing in any software project. Finally I will give an overview and explanation of the main algorithms in my code.

To start of I'd like to say the project is written in python, which the majority of you as second year students would have heard about but from experience would not have coded with as of yet.

The project required us to build a non-deterministic finite automaton (NFA) from a regular expression,and can use the NFA to check if the regular expression matches any given string of text.

My repository contains the following:

* [Lab](https://github.com/MarkReillyGMIT/GraphTheoryProject/tree/master/Lab "Lab Folder") folder keeps previous labs from each week of the module.
* [Project](https://github.com/MarkReillyGMIT/GraphTheoryProject/tree/master/Project "Project Folder") folder, this is where all the necessary files for my project are kept.
* [Image](https://github.com/MarkReillyGMIT/GraphTheoryProject/tree/master/Image "Image Folder") folder, keeps all images for README and Overview markdown documents.

The project folder contains the following:
* [Compile.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/Compile.py "Compile.py") this returns an NFA fragment representing the infix regular expression.
* [MainMenu.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/MainMenu.py "MainMenu.py") shows the main menu when the program is run.
* [Result.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/Result.py "Result.py") prompts the user to enter the Regular Expression and String.
* [State_Fragment.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/State_Fragment.py "State_Fragment.py") creates a fragment with a start and accept state.
* [main.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/main.py "Main.py") is where I call Result.py and MainMenu.py, which prompts user for input of Regex and String, returns if the Regex matches the string or not.
* [shunt.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/shunt.py "Shunt.py") is short for the shunting yard algorithm which is a method for parsing mathematical expressions specified in infix notation to postfix.
* [testing.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/testing.py "testing.py") is used for testing the program.
* [thompsonConstruction.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/thompsonConstruction.py "thompsonConstruction.py") is a method of transforming a regular expression into a NFA.[2] This NFA can be used to match strings against the regular expression.

# Run 
Firstly, I am going to discuss how to download and run my code from my GitHub repository.

* Start by opening a command prompt and enter the following `git clone https://github.com/MarkReillyGMIT/GraphTheoryProject`
* `cd GraphTheoryProject`
* `cd Project`
* `python main.py --Run`
* The program will prompt the user to input a regular expression, e.g "a.b|b*"
* Next, the program will prompt the user to enter a string, e.g "bbb"
* The program will return if the string matches or does not match the regular expression.

Secondly, I am going to discuss how to download python to your machine.

* Firstly go to the following link to download [Python](https://www.python.org/downloads/ "Python")
* Select which OS you want download it for, for this example I am going to use windows.
* Choose which python version and then select Windows x86-64 executable installer.
* Run the download file, when you reach a page with "Install Python 'version'" at the bottom of the page select "Add Python to path" and then select "Install Now".
* Click Next and then Install.
* Finally check if it is installed correctly by opening a command prompt and typing `python`, if the next writable line begins with ">>>" type `print('Hello World')` and enter. If "Hello World" is printed out, congratulations python is installed on your machine.

# Testing
In this section I am going to discuss how to run the tests incorporated in the code. My project testing is done in the [testing.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/testing.py "testing.py") file, I am testing to see if the postfix regular expression matches using the match function created in [thompsonConstruction.py](https://github.com/MarkReillyGMIT/GraphTheoryProject/blob/master/Project/thompsonConstruction.py "thompsonConstruction.py"). The match function allows us to test any input and return an answer of true or false.

The following will show you how to run testing for my project:
* Once in the Project directory within the GraphTheoryProject folder e.g `GraphTheoryProject/Project`.
* Enter `python testing.py`, this will run the testing.py file.
* Nothing will return if all the test's are correct.
* If a test is incorrect the following will return: "regular expression should not match string" or "regular expression should match string".

If a test is incorrect the following will return: "regular expression should not match string" or "regular expression should match string".

# Algorithm
The main algorithm in my project would be the
Shunting yard Algorithm which convert's an infix expression into a postfix expression.It uses a stack which is used to hold the operators.The purpose of the stack is to reverse the order of the operators in the expression.

The operator precedence needs to be set so the method knows which operator has higher precedence over the other operators.If the operator on the top of the stack has higher precedence than the one being read, pop and print the one on top and then push the new operator on.

Once the end of the expression has been reached, pop the operators on the stack one at a time and convert the output list to a string.

# References

Shunt Yard Algorithm Explanation - http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/

The following helped me to understand regular expressions to NFA's: https://www.youtube.com/watch?v=RYNN-tb9WxI

The following helped me to understand '+' One or more and '?' Zero or one and how to implement them: https://swtch.com/~rsc/regexp/regexp1.html

The folowing helped me with user input: https://www.geeksforgeeks.org/taking-input-in-python/

The following helped with adding command line arguements: https://www.geeksforgeeks.org/command-line-arguments-in-python/
