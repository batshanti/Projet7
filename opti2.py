import csv
import time


MAX = 500
DATASET = [

    "1 : invest.csv",
    "2 : dataset1.csv",
    "3 : dataset2.csv"
]


def main():
    dataset = choose_dataset()
    global start
    start = time.time()
    file_list = load_csv(dataset)
    sort_list = sorted_actions(file_list)
    invest_list = find_invest(sort_list, MAX)
    display(invest_list)

def choose_dataset():
    choices = {
        "1" : "invest.csv",
        "2" : "dataset1.csv",
        "3" : "dataset2.csv"
    }

    for line in DATASET:
        print(line)
    choice = input("Choose dataset : ")
    return choices[choice]

def load_csv(dataset):
    with open(dataset) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            if float(line[1]) <= 0 or float(line[2]) <= 0:
                pass
            else :
                file_list.append([line[0], float(line[1]), float(line[2])])

        return file_list

def sorted_actions(invest_list):
    return sorted(invest_list, key=lambda action: action[2], reverse=True)


def find_invest(invest_list, max):
    best_invest = []
    total_cost = 0
    i = 0

    while i < len(invest_list) and total_cost <= max:
        action = invest_list[i]
        action_cost = action[1]
        if total_cost + action_cost <= max:
            best_invest.append(action)
            total_cost += action_cost
        i += 1  

    return best_invest

def display(invest_list):
    actions_name = []
    cost = []
    gain = []

    for action in invest_list:
        actions_name.append(action[0])
        cost.append(action[1])
        gain.append(action[1] * action[2] / 100)

    print("List actions boughts : ")

    for action in actions_name:
        print(action)

    print("Total Cost : " + str(sum(cost)) + " Euros")
    print("Profit : " + str(sum(gain)) + " Euros")
    print("Script Time : " + str(time.time() - start))


if __name__ == "__main__":
    main()