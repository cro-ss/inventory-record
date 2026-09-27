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

##writing csv files
history_file = open('history.csv','a', newline = '', encoding='UTF-8')
history_writer= csv.writer(history_file)
history_writer.writerow(['pepe','ociosa','ola','carebola','pelo_corto','pepudo',])
history_file.close() 