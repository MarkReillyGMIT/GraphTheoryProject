# Author: Mark Reilly
# Graph Theory Project Thompsons Construction
# Test cases for NFA

import thompsonConstruction

if __name__ == "__main__":
    tests = [
        ["a.b|b*", "bbbbb", True],
        ["a.b|b*", "bbx", False],
        ["a.b*", "abbbb", True],
        ["b**", "b", True],
        ["b*", "", True],
        ["b+", "bbbb", True],
        ["a.b", "ab", True],
        ["a?", "a", True],
        ["a?", "aaa", False]
    ]

    for test in tests:
        assert thompsonConstruction.match(test[0], test[1]) == test[2], test[0] + \
        (" should not match " if test[2] else " should match ") + test[1]
