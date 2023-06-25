import requests
import base64
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access the variables using os.environ
username = os.environ.get('wp_user')
password = os.environ.get('wp_password')
wordpress_url = os.environ.get('wordpress_url')

# Combine the username and password with a colon
credentials = f"{username}:{password}"

# Encode the credentials as base64
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')


auth_header = {
    'Authorization': 'Basic '+encoded_credentials
}

class Post:
    def __init__(self):
        self.api_endpoint = f'{wordpress_url}/wp-json/wp/v2/posts'
    
    def create_post(self, post_data):
        # Send the HTTP POST request to create the new post
        response = requests.post(self.api_endpoint, headers=auth_header, json=post_data)

        # Check the response status code
        # Check the response status code
        if response.status_code == 201:
            return 'New blog post created successfully!'
        else:
            return f'Failed to create new blog post with error {response.status_code}: {response.text}'
    
    @staticmethod
    def get_posts(self):
        response = requests.get(self.api_endpoint)
        response.raise_for_status()
        return response.json()
    
    def delete_post(self, post_id):
        url = f"{self.api_endpoint}/{post_id}"
        print(url)
        response = requests.delete(url, headers=auth_header)
        # response.raise_for_status()
        return response.json()
    
    def update_post(self, post_id, post_data):
        url = f"{self.api_endpoint}/{post_id}"
        response = requests.post(url, headers=auth_header, json=post_data)
        # response.raise_for_status()
        return response.json()