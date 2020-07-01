#from operator import itemgetter

def build_map(in_file1, in_file2):
    '''Takes two files containing cities and continents as well as related countries
    and organizes them into a dictionary'''

    data_map = {
        "Continents" : {},
        "Cities": {}
    }

    #Read from file 1    
    file_list = in_file1.readlines()

    continent_list = []
    for line in file_list:
        temp_line = line.strip().split()
        continent_list.append(temp_line)
    
    continent_list.pop(0)
    #Sorts items into keys with list values in continents
    for i in range(len(continent_list)):
        if continent_list[i][0] not in data_map["Continents"].keys():
            data_map["Continents"][continent_list[i][0]] = {continent_list[i][1]}
        else:
            if continent_list[i][1] not in data_map["Continents"][continent_list[i][0]]:
                data_map["Continents"][continent_list[i][0]].add(continent_list[i][1])


    #Read from file 2
    file_list = in_file2.readlines()

    city_list = []
    for line in file_list:
        temp_line = line.strip().split()
        city_list.append(temp_line)
    
    city_list.pop(0)
    #Sorts items into keys with list values in continents
    for i in range(len(city_list)):
        if city_list[i][0] not in data_map["Cities"].keys():
            data_map["Cities"][city_list[i][0]] = {city_list[i][1]}
        else:
            if city_list[i][1] not in data_map["Cities"][city_list[i][0]]:
                data_map["Cities"][city_list[i][0]].add(city_list[i][1])

    return data_map


def display_map(data_map):
    '''Prints out cities in a country in its respective continent'''
    #For each continent
    for continent in data_map["Continents"]:
        [print(continent)]
        #For each country
        for country in data_map["Continents"][continent]:
            print("{:>10s} --> {}".format(country, str(data_map["Cities"][country])[1:-1]))


def open_file():
    '''Opens file with user input'''
    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


def main():

    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map(in_file1, in_file2) # data_map is a dictionary
        display_map(data_map)
        in_file1.close()
        in_file2.close()
        



if __name__ == "__main__":
    main()

