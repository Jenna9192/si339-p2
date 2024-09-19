import csv
import io
import sys
import unittest
import os


#connect path
filename = "Vera Naines18895017.csv"
base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, filename)

#connect path2
filename2 = "Violet Olley26328683.csv"
base_path2 = os.path.abspath(os.path.dirname(__file__))
full_path2 = os.path.join(base_path, filename)

csv_file = '/athletes/mens_team'
html_template_file = 'athlete_results_template.html'
output_html_file = 'athlete_results.html'

with open(full_path) as csv_file:
   csv_reader =  csv.reader(csv_file)
   name = next(csv_reader)
   id = next(csv_reader)
   for i in range(3):
         headers = next(csv_reader)

   data = []
   rows = list(csv_reader)
   for row in rows[:-2]:
        row_data = {}
        row_data['overall_place'] = row[1]
        row_data['grade'] = row[2]
        row_data['time'] = row[3]
        row_data['date'] = row[4]
        row_data['meet'] = row[5]
        data.append(row_data)

   print(data)
      
             

# # Read CSV data
# with open(csv_file, newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     data = list(reader)

# meet_name = "Athletics Meet"
# meet_date = "2024" 


# with open(html_template_file, 'r', encoding='utf-8') as template_file:
#     template = template_file.read()

# athlete_entries = ''
# for athlete in data[:2]: 
#     athlete_name = athlete['Name']
#     athlete_date = athlete['Date']
#     athlete_place = athlete['Overall Place']
#     athlete_time = athlete['Grade Time']
#     athlete_meet = athlete['Meet']

#     athlete_entries += f'''
#         <li>
#             <strong>{athlete_name}</strong><br>
#             Date: {athlete_date}<br>
#             Place: {athlete_place}<br>
#             Time: {athlete_time}<br>
#             Meet: {athlete_meet}<br>
#         </li>
#     '''

# html_content = template.format(
#     meet_name=meet_name,
#     meet_date=meet_date,
#     athlete_entries=athlete_entries
# )

# with open(output_html_file, 'w', encoding='utf-8') as output_file:
#     output_file.write(html_content)

# print("HTML file generated successfully.")