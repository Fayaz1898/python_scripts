import requests
import csv

# Fetch data from API
response = requests.get('http://universities.hipolabs.com/search?country=Canada')
data = response.json()

# Define CSV file
csv_file = 'universities_canada.csv'

# Extract relevant data
fields = ['name', 'alpha_two_code', 'country', 'web_pages']
rows = [[university['name'], university['alpha_two_code'], university['country'], ', '.join(university['web_pages'])] for university in data]

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)  # Write header
    writer.writerows(rows)  # Write data rows

print(f'Data has been written to {csv_file}')

