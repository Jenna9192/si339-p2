import csv
import io
import sys
import unittest
import os
import csv


# #connect path
# filename = "Vera Naines18895017.csv"
# base_path = os.path.abspath(os.path.dirname(__file__))
# full_path = os.path.join(base_path, filename)

# #connect path2
# filename2 = "Violet Olley26328683.csv"
# base_path2 = os.path.abspath(os.path.dirname(__file__))
# full_path2 = os.path.join(base_path, filename)

html_template_file = 'athlete_results_template.html'
output_html_file = 'athlete_results.html'
folder = 'athletes/womens_team'
files = os.listdir(folder)

html_content = f"""
<!DOCTYPE html>
<html lang = en>
<meta charset="UTF-8">
<head>
    <title>Athlete Results</title>
</head>
<body>
    <header>
        <title>Athlete Results</title>
    </header>
        <title>Women's Team Athletes</title>"""

for filename in files:
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        file_path = os.path.join(folder, filename)

        with open(file_path) as csv_file:
            csv_reader =  csv.reader(csv_file)
            name = next(csv_reader)[0]
            id = next(csv_reader)[0]
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

            # Create the HTML content
            # Create the HTML content with f-string substitution
            html_content += f"""
            <h1><strong>Name:</strong> {name} ({id})</h1>
            <table>
                <tr>
                    <th>Overall Place</th>
                    <th>Grade</th>
                    <th>Time</th>
                    <th>Date</th>
                    <th>Meet</th>
                </tr>
            """

            # Add rows to the HTML table from the CSV data
            for result in data:
                html_content += f"""
                    <tr>
                        <td>{result['overall_place']}</td>
                        <td>{result['grade']}</td>
                        <td>{result['time']}</td>
                        <td>{result['date']}</td>
                        <td>{result['meet']}</td>
                    </tr>
                """

            # Close the table and HTML tags
            html_content += """
            </table>"""

html_content += """
                </body>
                </html>
                """

# Write the HTML content to the output file
output_html_file = "athlete_results.html"
with open(output_html_file, "w") as html_file:
    html_file.write(html_content)