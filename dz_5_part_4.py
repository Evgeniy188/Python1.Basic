from translate import Translator


def file_split(write_f_name, read_f_name):
    with open(write_f_name, 'w', encoding='utf-8') as f_write:
        with open(read_f_name, 'r', encoding='utf-8') as f_read:
            translator = Translator(to_lang='Russian')
            for line in f_read:
                res = translator.translate(line.split(' - ')[0]) + ' - ' + line.split(' - ')[1]
                f_write.writelines(res)


write_f_name = 'my_test4.txt'
read_f_name = 'text_4.txt'
file_split(write_f_name, read_f_name)
