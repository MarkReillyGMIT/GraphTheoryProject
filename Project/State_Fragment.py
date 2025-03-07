# Author: Mark Reilly
# Graph Theory Project Thompsons Construction
#Reference Dr.Ian McLoughlin https://web.microsoftstream.com/video/3be78704-8cc5-43f1-9be5-68b2e92c8d56

"""A Nonedeterministic finite automaton (NFA) is represented as a fragement with a start state and an accept state """

class State:
    """ A state with one or two arrows, all edges labeled by label. """
        # Every state has 0, 1, or 2 edges from it.
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        #Label for the arrows, None means epsilon.
        self.label = label


class Fragment:
    """ An NFA fragment with a start state and an accept state"""
    #Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

