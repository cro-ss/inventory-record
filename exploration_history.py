import csv
file = open('history.csv', encoding = 'UTF-8')
reader = csv.reader(file)
data = list(reader)
print(data[0])
print(data[:])
print(len(data))
second_data=list(reader)
print(len(second_data))

file_dict = open('history.csv', encoding = 'UTF-8')
dict_reader = csv.DictReader(file_dict)
dict_data = list(dict_reader)
print(dict_data)
