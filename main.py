# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

import thompsonConstruction, MainMenu

# Print program header.
MainMenu.mainMenu()

# User input for regex and string.
regexInput = input("Enter Regular Expression: ")
userString = input("Enter string: ")

# Calls match from regex script on users regex and string.
result = (thompsonConstruction.match(regexInput, userString))
if result:
    print("\nThe regular expression " + regexInput + " matches the string " + userString)
else:
    print("\nThe regular expression" + regexInput + " does not match the string " + userString)
