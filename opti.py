from itertools import combinations

import csv
import time


MAX = 500

def main():
    file_list = load_csv()
    invest_dynamique(file_list)


def load_csv():
    with open("invest.csv") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            file_list.append([line[0], float(line[1]), float(line[2])])

        return file_list


def invest_dynamique(file_list):
    


    matrice = [[0 for x in range(MAX + 1)] for x in range(len(file_list) + 1)]

    for i in range(1, len(file_list) + 1):
        for w in range(1, MAX + 1):

            if file_list[i-1][1] <= w:
                a = file_list[i-1][1]
                print(type(a))
                matrice[i][w] = max(file_list[i-1][2] + matrice[i-1][w-a], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
    print(matrice)










if __name__ == "__main__":
    main()

