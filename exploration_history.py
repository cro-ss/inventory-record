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

## We are creating our own tester, which track the increses in files

pre_last = None
diff = 0
for row in dict_data:
    actual = int(row['n_elements'])
    if pre_last is not None:
        diff= actual-pre_last
        print(row['date'],diff)
    pre_last = actual