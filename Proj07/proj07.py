#CONSTANTS
PROMPT = "What would you like to do?\n 1. Search for documents\n 2. Read document\n 3. Quit program\n"
DIVIDER = "-------------------------------------------"


def open_file():
    '''Opnes a document with a name given with user input and returns a file pointer'''
    success = False
    #Error check
    while not success:
        fp = input("Enter name of file: ")
        try:
            try_file = open(fp, "r")
            return try_file
        except:
            print("Invalid file name, try again")


def prompt_message():
    '''Prompts and checks for valid user input and returns the input'''
    user_input = input(PROMPT)
    #Error check
    while user_input:
        if user_input in "123" and len(user_input) == 1:
            return user_input
        else:
            user_input = input("Invalid response, try again\n" + PROMPT)


def process_doc(fp_doc):
    '''Organizes the contents of a document into a dictionary and returns the dictionary'''
    process_doc = fp_doc.readlines()
    doc_num = 0
    doc_dict = {}


    for line in process_doc:
        if "<NEW DOCUMENT>" in line:
            doc_num += 1
            doc_dict[doc_num] = ""
        else:
            doc_dict[doc_num] += line
    return doc_dict


def search_input(doc_dict):
    '''Searches for terms within every element of the sorted dictionary and returns
    the documnet indecies in which the words were found'''
    user_input = input("Enter search terms: ")
    doc_results = []

    for i in range(len(doc_dict)):
        if user_input.casefold() in doc_dict[i + 1].casefold():
            doc_results.append(i + 1)
    if not doc_results:
        return "No Result"
    else:
        return str(doc_results).strip("[]")


def read_doc(doc_dict):
    '''Reads and prints a document based on its index in the dictionary'''
    user_input = input("Enter document number: ")

    print("Document #{}".format(user_input))
    print(DIVIDER)
    print(doc_dict[int(user_input)])
    print(DIVIDER)






def main():
    '''Main function'''
    fp = open_file()
    doc_file = process_doc(fp)
    Active = True
    while Active:
        user_input = prompt_message()

        if user_input == "1":
            print(search_input(doc_file))
        elif user_input == "2":
            read_doc(doc_file)
        else:
            Active = False
    fp.close()


if __name__ == "__main__":
    main()