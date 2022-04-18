from itertools import combinations

import csv
import time

start = time.time()

MAX = 500

def main():
    file_list = load_csv()
    best_invest_list = actions_combo(file_list)
    display(best_invest_list)

def load_csv():
    """Open csv file and return list
    
    Return
    ------
    list
        list of shares
        
    """
    with open("invest.csv") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            file_list.append([line[0], float(line[1]), float(line[2])])

        return file_list

def actions_combo(list):
    """Test all conbinations and find the best
    
    Parameters
    ----------
    list : list
    list of actions    
    
    Return
    ------
    list
        best invest list

    """
    best_invest_list = []
    total_gain = 0

    for line in range(len(list)):
        combination = combinations(list, line + 1)

        for combi in combination:
            total_price = calculate_invest(combi)
            
            if total_price <= MAX:
                gain = calculate_gain(combi)
            
                if gain > total_gain:
                    total_gain = gain
                    best_invest_list = combi

    return best_invest_list 

def calculate_invest(combi):
    """Calculate invest total price with list of shares
    
    Parameters
    ----------
    list : list
    list of shares
    
    Return
    ------
    float
        total invest
        
    """
    cost_actions = []
    
    for price in combi:
        cost_actions.append(price[1])

    total_cost = sum(cost_actions)    
    return total_cost


def calculate_gain(combi):
    """Calculate gain with list of shares
    
    Parameters
    ----------
    list : list
    list of shares
    
    Return
    ------
    float
        gain
        
    """
    gain = []

    for line in combi:
        gain.append(line[1] * line[2] / 100)

    total_gain = sum(gain)
    return total_gain


def display(invest_list):
    """Display best invest liste, total cost, total profit and running time.
    
    parameters
    ----------
    invest_list : list

    """
    actions_name = []
    cost = []
    
    for action in invest_list:
        actions_name.append(action[0])
        cost.append(action[1])

    print("List actions boughts : " + str(actions_name))
    print("Cost : " + str(sum(cost)) + " Euros")
    print("Profit : " + str(calculate_gain(invest_list)) + " Euros")
    print("Script Time : " + str(time.time() - start))

if __name__ == "__main__":
    main()
