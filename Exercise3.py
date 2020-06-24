#HEADER
#Imports
#Constants
#Variables


#Part A
def leap_year(year):
    return (int(year) % 400 == 0 or int(year) % 4 ==0) and (int(year) % 100 != 0)
#Part B
def rotate(s,n):
    if n <= len(s) and n >= 1:
        tempString = s[-1 * n:] + s[:len(s) - n]
        return tempString
    else:
        return "Error: Int (n) too large"
#Part C
def digit_count(num):
    even_digits = 0
    odd_digits = 0
    zero_digits = 0
    for i in str(num):
        if i != ".":
            if int(i) != 0 and int(i) % 2 == 0:
                even_digits += 1
            elif int(i) % 2 == 1:
                odd_digits += 1
            else:
                zero_digits += 1
    return f"({even_digits}, {odd_digits}, {zero_digits})"
#Part D
def float_check(num_string):
    return num_string.isdigit()


#Code Start
if __name__ == "__main__":
    print(leap_year("1896"))
    print(rotate("abcdefgh", 3))
    print(digit_count(0.123))
    print(float_check("12e34"))