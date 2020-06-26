#IMPORTS
import statistics

#PART A: Processing the data
def process_data():
    data_file = open("data.txt", "r")

    data_list = [[], [], []]
    for i in data_file:
        if i[12:16].isalpha() == False:
            temp_list = []
            temp_list.append(i[:12].strip())
            temp_list.append(float(i[12:16]))
            temp_list.append(float(i[24:28]))
            temp_list.append(round(temp_list[2] / (temp_list[1] ** 2), 2))
            print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(temp_list[0], temp_list[1], temp_list[2], temp_list[3]))
            data_list[0].append(temp_list[1])
            data_list[1].append(temp_list[2])
            data_list[2].append(temp_list[3])
        else:
            print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"))
    print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", statistics.mean(data_list[0]), statistics.mean(data_list[1]), statistics.mean(data_list[2])))        
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", max(data_list[0]), max(data_list[1]), max(data_list[2])))
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", min(data_list[0]), min(data_list[1]), min(data_list[2])))
    data_file.close()


#PART B: Processing data and writing to a new file
def write_to_file():
    #Open Text Files
    data_file = open("data.txt", "r")
    write_file = open("exported_data.txt", "w")
    #Data Process
    data_list = [[], [], []]
    for i in data_file:
        if i[12:16].isalpha() == False:
            temp_list = []
            temp_list.append(i[:12].strip())
            temp_list.append(float(i[12:16]))
            temp_list.append(float(i[24:28]))
            temp_list.append(round(temp_list[2] / (temp_list[1] ** 2), 2))
            write_file.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}\n".format(temp_list[0], temp_list[1], temp_list[2], temp_list[3]))
            data_list[0].append(temp_list[1])
            data_list[1].append(temp_list[2])
            data_list[2].append(temp_list[3])
        else:
            write_file.write("{:<12s}{:<12s}{:<12s}{:<12s}\n".format("Name", "Height(m)", "Weight(kg)", "BMI"))
    write_file.write("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}\n".format("Average", statistics.mean(data_list[0]), statistics.mean(data_list[1]), statistics.mean(data_list[2])))        
    write_file.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}\n".format("Max", max(data_list[0]), max(data_list[1]), max(data_list[2])))
    write_file.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", min(data_list[0]), min(data_list[1]), min(data_list[2])))
    #Close Text Files
    write_file.close()
    data_file.close()


#Start
if __name__ == "__main__":
    process_data()
    write_to_file()