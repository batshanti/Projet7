import csv
import time


MAX = 500

def main():
    file_list = load_csv()
    invest_list = invest_dynamique(file_list, MAX)
    display(invest_list)

def load_csv():
    with open("dataset1.csv") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            if float(line[1]) <= 0 or float(line[2]) <= 0:
                pass
            else :
                file_list.append([line[0],
                float(line[1]),
                (float(line[1])*float(line[2])/100)])

        return file_list


def invest_dynamique(file_list, inv_max):

    actions_selection = []
    nb_actions = len(file_list)
    cost = []
    gain = []

    for action in file_list:
        cost.append(int(action[1]))
        gain.append(int(action[2]))


    matrice = [[0 for x in range(inv_max + 1)] for x in range(nb_actions + 1)]

    for i in range(1, nb_actions + 1):
        for w in range(1, inv_max + 1):

            if cost[i-1] <= w:
                matrice[i][w] = max(gain[i-1] + matrice[i-1][w-int(cost[i-1])], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]


    while inv_max >= 0 and nb_actions >= 0:
        
        if matrice[nb_actions][inv_max] == matrice[nb_actions-1][inv_max-int(cost[nb_actions-1])] + int(gain[nb_actions-1]):
            actions_selection.append(file_list[nb_actions-1])
            inv_max -= cost[nb_actions-1]
        nb_actions -= 1
 
    return list(reversed(actions_selection))

def display(invest_list):
    actions_name = []
    cost = []
    gain = []

    for action in invest_list:
        actions_name.append(action[0])
        cost.append(action[1])
        gain.append(action[2])

    print("List actions boughts : " + str(actions_name))
    print("Cost : " + str(sum(cost)) + " Euros")
    print("Profit : " + str(sum(gain)) + " Euros\n")


if __name__ == "__main__":
    main()
