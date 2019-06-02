import csv

timing_data = []    # we want list of lists 
                    # column_chart = [['Test Name','Diff from Avg']]
                    # table_data = [['Test Name','Run Time (s)']] 

with open('TestTimingData.csv') as csv_data:
    csv_read = csv.reader(csv_data)

    for row in csv_read:
        timing_data.append(row)

column_chart = [['Test Name','Diff from Avg']]
table_data = [['Test Name','Run Time (s)']]

for row in timing_data[1:]:
    test_name = row[0]

    if not row[1] or not row[2]: # avoiding blank row datas
        continue
        
    current_run_time = float(row[1])    
    average_run_time = float(row[2])
    diff_from_avg = average_run_time - current_run_time
    column_chart.append([test_name,diff_from_avg])
    table_data.append([test_name,float(current_run_time)])

print(column_chart)
print("---------------------------")
print(table_data)

