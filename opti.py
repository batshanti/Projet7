from itertools import combinations

import csv
import time


MAX = 500

def main():
    file_list = load_csv()
    invest_dynamique(file_list, MAX)


def load_csv():
    with open("invest.csv") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            file_list.append([line[0], float(line[1]), float(line[2])])

        return file_list


def invest_dynamique(file_list, inv_max):


    matrice = [[0 for x in range(inv_max + 1)] for x in range(len(file_list) + 1)]

    for i in range(1, len(file_list) + 1):
        for w in range(1, inv_max + 1):

            if file_list[i-1][1] <= w:
                a = file_list[i-1][1]
                matrice[i][w] = max(file_list[i-1][2] + matrice[i-1][w-int(file_list[i-1][1])], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    actions_selection = []
    nb_element = len(file_list)

    while inv_max >= 0 and nb_element >= 0:
        action = file_list[nb_element-1]

        if matrice[nb_element][inv_max] == matrice[nb_element-1][inv_max-int(action[1])] + int(action[2]):
            actions_selection.append(action)
            inv_max -= int(action[1])
        nb_element -= 1

      
    print(list(reversed(actions_selection)))


if __name__ == "__main__":
    main()

