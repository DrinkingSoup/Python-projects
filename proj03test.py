#HEADING
#IMPORTS
import proj03library


def main():
    test1 = "Hello World"
    test2 = "H3ll0 W0r1d"
    test3 = "12345"
    #Test 1
    print("---TEST 1: is_alpha---")
    print(test1 + "\n Result: " + str(proj03library.is_alpha(test1)))
    print(test2 + "\n Result: " + str(proj03library.is_alpha(test2)))

    #Test 2
    print("---TEST 2: is_digit---")
    print(test1 + "\n Result: " + str(proj03library.is_digit(test1)))
    print(test2 + "\n Result: " + str(proj03library.is_digit(test2)))
    print(test3 + "\n Result: " + str(proj03library.is_digit(test3)))

    #Test 3
    print("---TEST 3: to_lower---")
    print(test1 + "\n Result: " + str(proj03library.to_lower(test1)))
    print(test2 + "\n Result: " + str(proj03library.to_lower(test2)))

    #Test 4
    print("---TEST 4: to_upper---")
    print(test1 + "\n Result: " + str(proj03library.to_upper(test1)))
    print(test2 + "\n Result: " + str(proj03library.to_upper(test2)))

    #Test 5
    print("---TEST 5: find_chr---")
    print("Find index of \'W\'in " + test1 + "\n Result: " + str(proj03library.find_chr(test1, "W")))
    print("Find index of \'l\' in " + test2 + "\n Result: " + str(proj03library.find_chr(test2, "l")))

    #Test 6
    print("---TEST 6: find_str---")
    print("Find index of \'orl\'in " + test1 + "\n Result: " + str(proj03library.find_str(test1, "orl")))
    print("Find index of \'3l\' in " + test2 + "\n Result: " + str(proj03library.find_str(test2, "3l")))

    #Test 7
    print("---TEST 7: replace_chr---")
    print("Replace \'e\' with \'3\' in " + test1 + "\n Result: " + str(proj03library.replace_chr(test1, "e", "3")))
    print("Replace \'3\' with \'e\' in " + test2 + "\n Result: " + str(proj03library.replace_chr(test2, "3", "e")))

    #Test 8
    print("---TEST 8: replace_str---")
    print("Replace \'Hello\' with \'Goodbye\' in " + test1 + "\n Result: " + str(proj03library.replace_str(test1, "Hello", "Goodbye")))
    print("Replace \'H3ll0\' with \'G00dby3\' in " + test2 + "\n Result: " + str(proj03library.replace_str(test2, "H3ll0", "G00dby3")))


#Run    
if __name__ == "__main__":
    main()
