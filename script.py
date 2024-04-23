import requests

# Confluence credentials and page information
username = 'your_username'
password = 'your_password' <you can also add your api token here>
base_url = 'https://your-confluence-instance.atlassian.net/wiki'
page_id = '123456789'  # Replace with the ID of the page you want to update or you can retrieve it by adding the command

# New content for the page
new_content = """
<h2>New Content</h2>
<p>This is the updated content of the Confluence page.</p>
"""

# API endpoint for updating a page
url = f'{base_url}/rest/api/content/{page_id}'

# Request headers
headers = {
    'Content-Type': 'application/json',
}

# Request data
data = {
    'type': 'page',
    'title': 'Updated Page Title',
    'version': {
        'number': 2  # Increment the version number to update the page
    },
    'body': {
        'storage': {
            'value': new_content,
            'representation': 'storage',
        },
    },
}

# Send the request to update the page
response = requests.put(url, json=data, auth=(username, password), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print('Page updated successfully!')
else:
    print(f'Error updating page: {response.text}')

