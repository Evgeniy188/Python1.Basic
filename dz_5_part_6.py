def lesson_dict(f_name: str):
    lesson_dict = dict()
    with open(f_name, 'r', encoding='utf-8') as file:
        for line in file:
            line_list = line.split()
            sum_num = 0
            for i in range(1, len(line_list)):
                num = ''
                for j in range(0, len(line_list[i])):
                    if line_list[i][j].isdigit():
                        num = num + line_list[i][j]
                try:
                    sum_num += int(num)
                except:
                    continue
            lesson_dict[line_list[0][0:-1]] = sum_num
    return lesson_dict


file_name = 'text_6.txt'
print(lesson_dict(file_name))
