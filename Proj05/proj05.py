#IMPORTS
import matplotlib.pyplot as plt
#VARIABLES



def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    plt.xlabel('Income')
    plt.ylabel('Cumulative Percent')
    plt.title("Cumulative Percent for Income in "+str(year))
    plt.plot(x_vals,y_vals)
    plt.show()

def get_error(err_val):
    '''Reads the error doc returns an error based on the inputed error value'''

    error_file = open("print_error_strings.txt", "r")
    return error_file.readlines()[err_val + 1]


def open_file():
    '''Prompts user for a year to examine and returns the file pointer, also it error checks for invalid year'''
    
    input_valid = False
    while not input_valid:
        try:
            year_str = input("Enter a year where 1990 <= year <= 2015: ")
            if year_str.isdigit() and int(year_str) >= 1990 and int(year_str) <= 2015:
                fp = open(f"year{year_str}.txt")
                input_valid = True
                return fp
            else:
                print(get_error(0))
        except:
            print(get_error(1))


def read_file(fp):
    '''Reads and digests file pointer into a list'''
    year_list = []
    for line in fp:
        temp = line.split()
        temp.pop(1)
        year_list.append(temp)
    year_list.pop(0)
    year_list.pop(0)

    return year_list

        
def find_average(data_lst):
    '''finds the average income for the given year'''
    denom_num = float(data_lst[len(data_lst) - 1][3].replace(",", ""))
    numer_num = 0
    for i in data_lst:
        numer_num += float(i[5].replace(",", ""))

    return round((numer_num / denom_num), 2)


def find_median(data_lst):
    '''Finds the median salary of that given year'''
    temp_lst = [[], []]
    for i in data_lst:
        temp_lst[0].append(float(i[4]))
        temp_lst[1].append(float(i[6].replace(",", "")))
    index = temp_lst[0].index(temp_lst[0][min(range(len(temp_lst[0])), key = lambda i: abs(temp_lst[0][i] - 50))])

    return temp_lst[1][index]

def get_range(data_lst, percent):
    '''Uses a percent and returns salary range, the cumulative percentage, and average income in relation to the percentage parameter'''
    percent_index = 0
    index_found = False
    for i in data_lst:
        if not index_found and float(i[4]) < percent:
            percent_index += 1
        else:
            index_found = True
    return (data_lst[percent_index][0], data_lst[percent_index][1]), data_lst[percent_index][4], data_lst[percent_index][6]


def get_percent(data_lst,salary):
    '''Takes a list of data and an income and returns cumulative percentage and income range in relation to that salary'''
    salary_index = 0
    index_found = False
    for i in data_lst:
        if not index_found and not (float(i[0].replace(",", "")) <= salary and float(i[1].replace(",", "")) >= salary):
            salary_index += 1
        else:
            index_found = True
    return (data_lst[salary_index][0], data_lst[salary_index][1]), data_lst[salary_index][4]

def main():
    fp_list = read_file(open_file())
    year = "2014"
    avg = find_average(fp_list)
    median = find_median(fp_list)
    print("For the year {:4s}:".format(year))
    print("The average income was ${:<13,.2f}".format(avg))
    print("The median income was ${:<13,.2f}".format(median))
    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        x_list = []
        y_list = []
        for i in fp_list:
            x_list.append(float(i[6].replace(",", "")))
        for i in fp_list:
            y_list.append(float(i[4]))


        do_plot(x_list, y_list,year)
    
    choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    
    while choice:
        try:
            if choice.lower() == "r":
                perc_30 = input("Enter a percent: ")
                try:
                    val = get_range(fp_list, float(perc_30))
                    print(f"Range: {val[0][0]} - {val[0][1]}\n")
                    print(f"Closest Percent : {val[1]}\n")
                    print(f"Average Salary : {val[2]}\n")
                except:
                    print(get_error(4))
            if choice.lower() == "p":
                income_brh = input("Enter an income salary: ")
                try:
                    val = get_percent(fp_list, float(income_brh))
                    print(f"Range: {val[0][0]} - {val[0][1]}\n")
                    print(f"Closest Percent : {val[1]}\n")
                except:
                    print(get_error(5))
        except:
            print(get_error(6))
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")

if __name__ == "__main__":
    main()