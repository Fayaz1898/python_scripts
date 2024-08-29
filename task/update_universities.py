import csv
import requests

# API endpoints
post_url = 'https://jsonplaceholder.typicode.com/posts'
patch_url = 'https://jsonplaceholder.typicode.com/posts/{id}'

# Function to check if a record exists
def record_exists(name):
    response = requests.get(f'{post_url}?title={name}')
    if response.status_code == 200:
        records = response.json()
        if records:
            return records[0]['id']  # Assuming the first record is the correct one
    return None

# Read data from CSV
csv_file = 'universities_canada.csv'
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        web_pages = row['web_pages']

        # Prepare payload
        payload = {
            'title': name,
            'body': web_pages,
            'userId': 1  # Placeholder userId, update as needed
        }

        # Check if record exists and update or create accordingly
        record_id = record_exists(name)
        if record_id:
            # Update record
            patch_response = requests.patch(patch_url.format(id=record_id), json=payload)
            if patch_response.status_code == 200:
                print(f'Updated record for name: {name}')
            else:
                print(f'Failed to update record for name: {name}')
        else:
            # Create record
            post_response = requests.post(post_url, json=payload)
            if post_response.status_code == 201:
                print(f'Created record for name: {name}')
            else:
                print(f'Failed to create record for name: {name}')

