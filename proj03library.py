#HEADING
#IMPORTS
#CONSTANTS
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz "
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
DECIMAL_DIGITS = "0123456789"
#VARIABLES


#FUNCTIONS

#0. (my own thing) find_index(str, str)
def find_index(str_compare, str_input):
    loop_active = True
    temp_index = 0
    for i in range(len(str_compare)):
        if loop_active:
            if str_input != str_compare[i]:
                temp_index += 1
            else:
                loop_active = False
    return temp_index

#1. is_alpha(str)
def is_alpha(str):
    function_result = True
    for i in str:
        if (i not in ASCII_LOWERCASE) and (i not in ASCII_UPPERCASE):
            function_result = False
    if function_result:
        return True
    else:
        return False


#2. is_digit(str)
def is_digit(str):
    function_result = True
    for i in str:
        if i not in DECIMAL_DIGITS:
            function_result = False
    if function_result:
        return True
    else:
        return False


#3. to_lower(str)
def to_lower(str):
    str_temp = str
    str_index = 0
    for i in str:
        if i in ASCII_UPPERCASE:
            temp_index = find_index(ASCII_UPPERCASE, i)
            str_temp = str_temp[:str_index] + ASCII_LOWERCASE[temp_index] + str_temp[str_index + 1:]
        str_index += 1
    return str_temp


#4 to_upper(str)
def to_upper(str):
    str_temp = str
    str_index = 0
    for i in str:
        if i in ASCII_LOWERCASE:
            temp_index = find_index(ASCII_LOWERCASE, i)
            str_temp = str_temp[:str_index] + ASCII_UPPERCASE[temp_index] + str_temp[str_index + 1:]
        str_index += 1
    return str_temp


#5 find_chr(str, str)
def find_chr(str1, str2):
    loop_active = True
    temp_index = 0
    for i in str1:
        if loop_active:
            if str2 == i:
                loop_active = False
            else:
                temp_index += 1
    if temp_index == len(str1):
        return -1
    else:
        return temp_index

#6 find_str(str, str)
def find_str(str1, str2):
    loop_active = True
    temp_index = 0
    for i in str1:
        if loop_active:
            if i == str2[0]:
                test_num = 0
                for j in range(len(str2)):
                    if str1[temp_index + j] == str2[j]:
                        test_num += 1
                if test_num == len(str2):
                    loop_active = False
                else:
                    temp_index += 1   
            else:
                temp_index += 1
    if temp_index == len(str1):
        return -1
    else:
        return temp_index               
                

#7. replace_chr(str, str, str)
def replace_chr(original_string, to_replace, will_replace):
    temp_index = 0
    tempString = original_string
    if len(to_replace) == 1 and len(will_replace) ==1:
        for i in original_string:
            if i == to_replace:
                tempString = tempString[:temp_index] + will_replace + tempString[temp_index + 1:]
            temp_index += 1
        return tempString 
    else:
        return ""


#8. replace_str(str, str, str)
def replace_str(original_string, to_replace, will_replace):
    temp_string = original_string
    working_string = original_string
    if to_replace != "":
        while find_str(temp_string, to_replace) != -1:
            temp_index = find_str(temp_string, to_replace)
            print(temp_index)
            working_string = working_string[:temp_index] + will_replace + working_string[temp_index + len(to_replace):]
            temp_string = temp_string[len(temp_string) - temp_index + 1:]

        return working_string
    else:
        return will_replace + original_string + will_replace

"""
Me when code not work:
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀⠀⠀
"""