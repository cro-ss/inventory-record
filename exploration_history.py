import csv
from datetime import datetime
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
pre_day = None
diff = 0
delta_date = None
mean_delta=0
difference = None
for row in dict_data:
    ## current date in date format
    current_str_format = row['date']
    current_date_format = datetime.strptime(current_str_format,f'%Y-%m-%d').date()
    ## actual number of elements
    actual = int(row['n_elements'])
    if pre_last is not None:
        ## diff is the difference between files
        diff= actual-pre_last
        delta_date = current_date_format - pre_day
        mean_delta = diff/delta_date.days
        difference= delta_date.days  
    

    print(row['date'], f'{diff}  ' ,f'   delta between two dates {difference}',f'   Mean files per day {round(mean_delta,0)}')
    pre_last = actual
    pre_day = current_date_format





## Now we create a feature that gives us the difference among days, maybe the tracker is applied 1 week up next, therefore it should have more files but in more days

### step 0 install libraries
from datetime import datetime

### step 1 get a date time form str
#str_time = dict_data[-1]['date']
#print(str_time)
#print(type(str_time))
#date_time_values = datetime.strptime(str_time, f'%Y-%m-%d')

## look that when converted to date time it returns the hours as well even when we write just year, month and day.
#print(date_time_values)
## step 2 solution
#date_time_values = datetime.strptime(str_time, f'%Y-%m-%d').date()
#print(date_time_values)
## check that effectively the str turns into date time object
#print(type(date_time_values))

## step 3 proofs
#today = datetime.now().date()
#diff_days= today - date_time_values
#print(diff_days)
#print(diff_days.days)




#date.from(f'%Y-%m-%d')
