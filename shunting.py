#Mark Reilly
#The shunting yard algorithm for regular expressions.

#THe input -  let user type own input in future
infix = "(a|b).c*"
print("Input is:" , infix)
# Expected output:" ab|c*."
print("Expected: ab|c*.")
#Operator
opers = []

#Convert the input to a stack list.
infix = list(infix)[::-1]

#Output list.
postfix = []

#Operator precedence
prec = {'*': 100, '|': 80, '.': 60, ')': 40, '(': 20}
#Loop through one character at a time.
while infix:
    #pop a character from the list
    c = infix.pop()
#Decide what to do based on the character.
    if c == '(':
        #Push and open brcket to opers stack
        opers.append(c)
    elif c == ')':
        #Pop the operators stack until u find an opening bracket
        while opers[-1] != '(':
            postfix.append(opers.pop())
        #Get rid of the "("
        opers.pop()
    elif c in prec:
        #Push any operators on the opers stack with higher prec to the output.
        while opers and prec[c] < prec[opers[-1]]:
            postfix.append(opers.push())
        #Push c to the opers stack.
        opers.append(c)
    else:
        #Typically we just push the character to the output
        postfix.append(c)

#Pop all cahracters to the output
while opers:
    postfix.append(opers.pop())

#Convert output list to string.
postfix = ''.join(postfix)

#Print the result
print("Output is: ", postfix)

