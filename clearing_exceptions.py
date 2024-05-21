import csv
import re
import os

directories = os.listdir()
list_dirs = []
for director in directories:
    if '.csv' in director:
        list_dirs += [director]

num=0
for list_dir in list_dirs:
    num+=1
    print(f'[{num}] {list_dir}')

enter_list = int(input('Введите число: '))
enter_list-=1
try:
    document = (list_dirs[enter_list])
    print(document)
except:
    print('Некорректный выбор')

with open('exceptions.txt', 'r') as file_txt:
    txt_domains = {row.strip() for row in file_txt}

with open(f'{document}', 'r') as file_csv:
    reader = csv.DictReader(file_csv)
    
    if 'Domain' not in reader.fieldnames:
        print("Столбец 'Domain' не найден в CSV файле.")
        exit(1)

    for row in reader:
        email = row['Domain']

        if email in txt_domains:
            print("Найдено точное совпадение:", email)
            with open('result.txt', 'a+') as result_file:
                result_file.write(f'{email}\n')
        else:
            match = re.search(r'@(.+)', email)
            if match:
                domain = match.group(1)

                if domain in txt_domains:
                    print("Найдено совпадение по домену:", email)
                    with open('result.txt', 'a+') as result_file:
                        result_file.write(f'{email}\n')
