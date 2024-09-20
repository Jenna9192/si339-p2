import csv
import os

# Define the path to your folder containing CSV files
athletes_folder = 'athletes'  # Replace with your folder name
base_path = os.path.abspath(os.path.dirname(__file__))
folder_path = os.path.join(base_path, athletes_folder)

# List all CSV files in the directory
def list_csv_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

# Process CSV file and extract data
def process_csv(file_path):
    data = []
    with open(file_path, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row_data = {
                'name': row.get('Name'),
                'grade': row.get('Grade'),
                'overall_place': row.get('Overall Place'),
                'time': row.get('Time'),
                'date': row.get('Date'),
                'meet': row.get('meet')  # Updated to 'meet'
            }
            data.append(row_data)
    return data

# Get all CSV files
csv_files = list_csv_files(folder_path)

# Check if we have at least two files
if len(csv_files) < 1:
    print("No CSV files found in the 'athletes' folder.")
    exit()

# Process the first CSV file (change index if needed)
csv_file_path = os.path.join(folder_path, csv_files[0])
data = process_csv(csv_file_path)

# Check if we have at least two rows of data
if len(data) < 2:
    print("Not enough data in the CSV file.")
    exit()

# Prepare HTML content
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Athlete Results</title>
</head>
<body>
    <!-- Main content with headers and table for details -->
    <main>
        <!-- Athlete 1 -->
        <header>
            <h1>{athlete1_name}</h1> <!-- Placeholder for first athlete's name -->
        </header>
        <section>
            <h2>Race Details</h2>
            <table border="1">
                <thead>
                    <tr>
                        <th>Grade</th>
                        <th>Overall Place</th>
                        <th>Athlete's Time</th>
                        <th>Meet</th> <!-- Updated placeholder to 'Meet' -->
                        <th>Race Date</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{athlete1_grade}</td> <!-- Placeholder for first athlete's grade -->
                        <td>{athlete1_overall_place}</td> <!-- Placeholder for first athlete's overall place -->
                        <td>{athlete1_race_time}</td> <!-- Placeholder for first athlete's race time -->
                        <td>{meet_name}</td> <!-- Placeholder for meet -->
                        <td>{race_date}</td> <!-- Placeholder for race date -->
                    </tr>
                </tbody>
            </table>
        </section>

        <!-- Athlete 2 -->
        <header>
            <h1>{athlete2_name}</h1> <!-- Placeholder for second athlete's name -->
        </header>
        <section>
            <h2>Race Details</h2>
            <table border="1">
                <thead>
                    <tr>
                        <th>Grade</th>
                        <th>Overall Place</th>
                        <th>Athlete's Time</th>
                        <th>Meet</th> <!-- Updated placeholder to 'Meet' -->
                        <th>Race Date</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{athlete2_grade}</td> <!-- Placeholder for second athlete's grade -->
                        <td>{athlete2_overall_place}</td> <!-- Placeholder for second athlete's overall place -->
                        <td>{athlete2_race_time}</td> <!-- Placeholder for second athlete's race time -->
                        <td>{meet_name}</td> <!-- Placeholder for meet -->
                        <td>{race_date}</td> <!-- Placeholder for race date -->
                    </tr>
                </tbody>
            </table>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Athletics Meet</p>
    </footer>
</body>
</html>
'''

# Prepare placeholders with data from the CSV file
html_content = html_template.format(
    athlete1_name=data[0]['name'],
    athlete1_grade=data[0]['grade'],
    athlete1_overall_place=data[0]['overall_place'],
    athlete1_race_time=data[0]['time'],
    athlete2_name=data[1]['name'],
    athlete2_grade=data[1]['grade'],
    athlete2_overall_place=data[1]['overall_place'],
    athlete2_race_time=data[1]['time'],
    meet_name=data[0]['meet'],  # Assuming meet name is the same for both athletes
    race_date=data[0]['date']   # Assuming race date is the same for both athletes
)

# Output HTML file path
output_html_file = 'athlete_results.html'

# Write the generated HTML to a file
with open(output_html_file, 'w') as output_file:
    output_file.write(html_content)

print("HTML file generated successfully.")



# import csv
# import io
# import sys
# import unittest
# import os


# #connect path
# filename = "Vera Naines18895017.csv"
# base_path = os.path.abspath(os.path.dirname(__file__))
# full_path = os.path.join(base_path, filename)

# #connect path2
# filename2 = "Violet Olley26328683.csv"
# base_path2 = os.path.abspath(os.path.dirname(__file__))
# full_path2 = os.path.join(base_path, filename)

# csv_file = '/athletes/mens_team'
# html_template_file = 'athlete_results_template.html'
# output_html_file = 'athlete_results.html'

# with open(full_path) as csv_file:
#    csv_reader =  csv.reader(csv_file)
#    name = next(csv_reader)
#    id = next(csv_reader)
#    for i in range(3):
#          headers = next(csv_reader)

#    data = []
#    rows = list(csv_reader)
#    for row in rows[:-2]:
#         row_data = {}
#         row_data['overall_place'] = row[1]
#         row_data['grade'] = row[2]
#         row_data['time'] = row[3]
#         row_data['date'] = row[4]
#         row_data['meet'] = row[5]
#         data.append(row_data)

#    print(data)
      
             

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