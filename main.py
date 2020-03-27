# Author: Mark Reilly

import thompsonConstruction, MainMenu

MainMenu.mainMenu()

userRegex = input("Enter Regular Expression: ")
userString = input("Enter string: ")

result = (regex.match(userRegex, userString))
if result:
    print("\nThe regex " + userRegex + " mathces the string " + userString)
else:
    print("\nThe regex " + userRegex + " does not match the string " + userString)
