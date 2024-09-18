import csv

csv_file = 'athletes'
html_template_file = 'athlete_results_template.html'
output_html_file = 'athlete_results.html'

# Read CSV data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

meet_name = "Athletics Meet"
meet_date = "2024" 


with open(html_template_file, 'r', encoding='utf-8') as template_file:
    template = template_file.read()

athlete_entries = ''
for athlete in data[:2]: 
    athlete_name = athlete['Name']
    athlete_date = athlete['Date']
    athlete_place = athlete['Overall Place']
    athlete_time = athlete['Grade Time']
    athlete_meet = athlete['Meet']

    athlete_entries += f'''
        <li>
            <strong>{athlete_name}</strong><br>
            Date: {athlete_date}<br>
            Place: {athlete_place}<br>
            Time: {athlete_time}<br>
            Meet: {athlete_meet}<br>
        </li>
    '''

html_content = template.format(
    meet_name=meet_name,
    meet_date=meet_date,
    athlete_entries=athlete_entries
)

with open(output_html_file, 'w', encoding='utf-8') as output_file:
    output_file.write(html_content)

print("HTML file generated successfully.")