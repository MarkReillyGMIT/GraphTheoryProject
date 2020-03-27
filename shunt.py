# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

def shunt(infix):
    """Return the infix regular expression in postfix """
    #Convert the input to a stack list.
    infix = list(infix)[::-1]

    #Operators Stack
    opers = []
 
    #Output lists.
    postfix = []

    #Operator precedence
    prec = {'*': 100,'?': 95, '+': 85, '|': 80, '.': 60, ')': 40, '(': 20}
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
                postfix.append(opers.pop())
            #Push c to the opers stack.
            opers.append(c)
        else:
            #Typically we just push the character to the output
            postfix.append(c)

    #Pop all cahracters to the output
    while opers:
        postfix.append(opers.pop())

    #Convert output list to string.
    return ''.join(postfix)

