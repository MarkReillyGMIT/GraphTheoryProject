# Author: Mark Reilly
# Graph Theory Project Thompsons Construction
# Reference Dr.Ian McLoughlin https://web.microsoftstream.com/video/f4bc3634-b94f-4c15-b2c1-70cccd874c54
from Compile import compile

#Add a state to a set and follow all of the e arrows
def followes(state, current):
    if state not in current:
       # Put the state into current
        current.add(state)
       #See whether state is labeled by e
        if state.label is None:
            # Loop through the states pointed to by this one.
            for x in state.edges:
                # Follow all of their e(psilon)s too.
                followes(x, current)

def match(regex, s):
    """This function will return true if and only if the regular expression 
         regex (fully) matches the string s,it returns False otherwise"""    # Returns true if regex (fully) matches the string s. It returns false otherwise.

    # Compile the regular expression into an NFA.
    nfa = compile(regex)

    # Try to match the regular expression to the string s
    # The Current set of states
    current = set()
    followes(nfa.start, current)
    # The previous set of states
    previous = set()

    # Loop through characters in s.
    for c in s:
        # Keep track of where we were.
        previous = current
        # Create a new empty set for states we're about to be in.
        current = set()
        # Loop through the previous state
        for state in previous:
            # Only follow arrows not labelled by e(psilon).
            if state.label is not None:
                # If the label of the state is equal to the character we've read.
                if state.label == c:
                # Add the state at the end of the arrow to current.
                    followes(state.edges[0], current)


    # Ask the NFA if it matches the string s.
    return nfa.accept in current


