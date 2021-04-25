import json


def create_list_firm(f_name: str):
    with open(f_name, 'r', encoding='utf-8') as file:
        firm_dict = dict()
        average_profit = 0
        n = 0
        for line in file:
            profit = float(line.split()[2]) - float(line.split()[3])
            firm_dict[line.split()[0]] = profit
            if profit > 0:
                n += 1
                average_profit = average_profit + profit
        list_firm = [firm_dict, {'average_profit': average_profit / n}]
    return list_firm


def create_json_obj(my_list):
    with open('my_list7.json', 'w', encoding='utf-8') as file:
        json.dump(my_list, file)


file_name = 'text_7.txt'
create_json_obj(create_list_firm(file_name))
