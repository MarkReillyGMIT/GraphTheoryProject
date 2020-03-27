import thompsonConstruction

if __name__ == "__main__":
    # An array of test data
    tests = [
        ["a.b|b*", "bbbbb", True],
        ["a.b|b*", "bbx", False],
        
        ["a.b", "ab", True], 
        ["a.b", "c", False], 
        
        ["b*", "", True],
        ["b**", "bbbbbb", True],

        ["c|a", "c", True],
        ["c|a", "b", False],

        ["b+", "bbb", True],
        ["b+", "", False],

        ["a?", "a", True],
        ["a?", "aa", False]
    ]

    # test our data using match function
    for test in tests:
        assert thompsonConstruction.match(test[0], test[1]) == test[2], test[0] + " should match " if test[2] else " should not match " + test[1]

