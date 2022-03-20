import csv
import time



def main():
    file_list = load_csv()
    # print(file_list)
    print(file_list[0])
    print(file_list[1])



def load_csv():
    with open("invest.csv") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        file_list = []
        for line in file:
            file_list.append([line[0], float(line[1]), float(line[2])])

        return file_list


if __name__ == "__main__":
    main()