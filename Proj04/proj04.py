#CONSTANTS
CONST_YEAR_RANGE = 47
CONST_PERCENT_LINE_RANGE = 7
CONST_GDP_LINE_RANGE = 42

def open_file():
    '''Repeatedly prompt until a valid file name allows the file to be opened.'''
    valid = False
    
    while not valid:
        try:
            data_file = open(input("Enter file name: "), "r")
            valid = True
            return data_file
        except:
            print("Error: Invalid file name")

       
    
def find_min_percent(data_file, line):
    '''Find the min percent change in the line; return the value and the index.'''

    lines = data_file
    min_value = 100000000.0
    min_index = 0
    for i in range(CONST_YEAR_RANGE):
        current_val = float(lines[line + CONST_PERCENT_LINE_RANGE][76 + (12 * i):76 + (12 * (i + 1))].strip())
        if current_val < min_value:
            min_value = current_val
            min_index = i
    return min_value, min_index


def find_max_percent(data_file, line):
    '''Find the max percent change in the line; return the value and the index.'''

    lines = data_file
    min_value = -100000000.0
    min_index = 0
    for i in range(CONST_YEAR_RANGE):
        current_val = float(lines[line + CONST_PERCENT_LINE_RANGE][76 + (12 * i):76 + (12 * (i + 1))].strip())
        if current_val > min_value:
            min_value = current_val
            min_index = i
    return min_value, min_index

def find_gdp(data_file, line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    lines = data_file
    return lines[42 + line][76 + (12 * index):76 + (12 * (index + 1))].strip()


def find_year(data_file, index):
    '''Use the index to find the year'''
    lines = data_file
    return lines[42][76 + (12 * index):76 + (12 * (index + 1))].strip()

        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''
    print("Gross Domestic Product\n")    
    print("{:<10s}{:>8.6s}{:>6s}{:>18.3s}\n".format("min/max", "change", "year", "GDP"))
    print("{:<10s}{:>8.2f}{:>6}{:>18.2f}\n".format("max", max_val, max_year, float(max_val_gdp) * 0.001))
    print("{:<10s}{:>8.2f}{:>6}{:>18.2f}\n".format("min", min_val, min_year, float(min_val_gdp) * 0.001))

def main():                    
    df = open_file().readlines()
    minval = find_min_percent(df, 1)[0]
    maxval = find_max_percent(df, 1)[0]
    minyear = find_year(df, find_min_percent(df, 1)[1])
    maxyear = find_year(df, find_max_percent(df, 1)[1])
    mingdp = find_gdp(df, 1, find_min_percent(df, 1)[1])
    maxgdp = find_gdp(df, 1, find_max_percent(df, 1)[1])
    display(minval, minyear, mingdp, maxval, maxyear, maxgdp)

    


# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
    
