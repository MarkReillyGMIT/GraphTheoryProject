# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

import thompsonConstruction, MainMenu
"""
Prompts user for input of Regex and String, returns if the Regex matches the string or not.
"""
# Prints Main Menu .
MainMenu.mainMenu()

# User input for regex and string.
regexInput = input("Enter Regular Expression: ")
userString = input("Enter string: ")

result = (thompsonConstruction.match(regexInput, userString))
if result:
    print("\nThe regular expression " + regexInput + " matches the string " + userString)
else:
    print("\nThe regular expression" + regexInput + " does not match the string " + userString)
