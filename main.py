import operator
dict = {}
with open('1.txt', encoding='utf-8') as file1:
    first_file = len(file1.readlines())

dict[file1.name] = first_file

with open('2.txt', encoding='utf-8') as file2:
    second_file = len(file2.readlines())

dict[file2.name] = second_file

with open('3.txt', encoding='utf-8') as file3:
    third_file = len(file3.readlines())

dict[file3.name] = third_file

sorted_tuples = sorted(dict.items(), key=operator.itemgetter(1))
sorted_dict = {k: v for k,v in sorted_tuples}

result = 'result.txt'

for key, value in sorted_dict.items():
    with open(f'{key}', encoding='utf-8') as file:
        read_file = file.read()
        with open(result, 'a') as file:
            file.write(f'{key}\n')
            file.write(f'{value}\n')
            file.write(f'{read_file}\n')

