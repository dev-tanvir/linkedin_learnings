import csv
from string import Template

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

# print(column_chart)
# print("---------------------------")
# print(table_data)

html_string = Template('''
<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
  var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.

    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);

}
</script>
</head>
<body>
    <div id="chart_div" style="width:1000; height:500"></div>
</body>
</html>
''')

chart_data_str = ''

for row in column_chart[1:]:
    chart_data_str += '%s,\n'%row

completed_html = html_string.substitute(labels=column_chart[0],data=chart_data_str)

with open('column_chart.html','w') as output_file:
    output_file.write(completed_html)