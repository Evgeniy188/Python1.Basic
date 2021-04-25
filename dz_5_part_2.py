def count_str_words(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        n_str = 0
        count_list_word = []
        for line in file:
            n_str += 1
            n_words = 0
            for words in line.split():
                n_words += 1
            count_list_word.append(n_words)
        return n_str, count_list_word


file_name = 'my_test1.txt'
count_str, word_list = count_str_words(file_name)
print('Количество строк в файле:', count_str)
[print(f'В {i + 1}-й строке количество слов = {word_list[i]}') for i in range(len(word_list))]
