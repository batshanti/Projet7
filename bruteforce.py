import csv
import time





def load_csv():
    with open("invest.csv") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            file_list.append(line[0], float.(line[1]), float.(line[2]))

        return file_list
       