#IMPORTS
import csv
from operator import itemgetter
from datetime import datetime as dt



def read_file(fp):
    '''Returns a list containing information from the covid csv file'''
    
    output_list = [[], [], [], [], []]
    reader = csv.reader(fp)
    for line in reader:
        if "Michigan" in line:
            output_list[0].append(line)
        elif "New York" in line:
            output_list[1].append(line)
        elif "Arizona" in line:
            output_list[2].append(line)
        elif "Texas" in line:
            output_list[3].append(line)
        else:
            if "California" in line:
                output_list[4].append(line)

    return output_list, 

def get_totals(states, data):
    '''Finds the current total covid case number in the specified states'''
    case_list = [[], [], [], [], []]
    for i in range(5):
        current_total = 0
        current_date = "01/01/00"
        for j in data[0][i]:
            if dt.strptime(j[0], "%m/%d/%y") > dt.strptime(current_date, "%m/%d/%y"):
                current_date = j[0]
                current_total = j[3]
        case_list[i].append(states[i])
        case_list[i].append(current_total)

    return case_list

def get_spike_dates(states,data):
    '''Finds the highest difference in covid cases by consecutive date'''
    spike_list = [[], [], [], [], []]
    for i in range(5):
        current_spike = 0
        spike_date = ""
        previous_value = 0
        for j in data[0][i]:
            if int(j[3]) - previous_value > current_spike:
                current_spike = int(j[3]) - previous_value
                spike_date = j[0]
            previous_value = int(j[3])
        spike_list[i].append(states[i])
        spike_list[i].append(spike_date)
        spike_list[i].append(current_spike)
    return spike_list


def main():    

    states = ['Michigan','New York','Arizona','Texas','California']

    fp = open("covid-19-us-states.csv")
    file_data = read_file(fp)
    
    
    state_totals = get_totals(states, file_data)
    if state_totals:  # if their values are not None
        print("\nTotal Coronavius cases by state\n")
        print("{:24s} {:10s}".format("State","#Cases"))
        for tup in state_totals:
            print("{:24s} {:2s}".format(tup[0],tup[1]))

    state_spikes = get_spike_dates(states, file_data)
    if state_spikes:  # if their values are not None
        print("\nDate of Coronavius spike by State \n")
        print("{:24s} {:10s} {:>8s}".format("State","Date","#Cases"))
        for tup in state_spikes:
            print("{:24s} {:10s} {:8d}".format(tup[0],tup[1],tup[2]))

if __name__ == "__main__":
    main()
