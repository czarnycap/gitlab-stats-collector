import os
import requests

# Get the GitLab API URL from an environment variable
api_url = os.environ['GITLAB_API_URL']
print(api_url)

# Set up the API endpoint URL and headers
# commits_url = f'{api_url}/projects/:id/repository/commits'
commits_url = f'{api_url}'
headers = {'PRIVATE-TOKEN': os.environ['GITLAB_ACCESS_TOKEN']}

# Call the API endpoint and get the response
response = requests.get(commits_url, headers=headers)

print("reponse code",response.status_code)
# # Check if the request was successful
# if response.status_code == 200:
#     # Get the number of commits from the response headers
#     num_commits = int(response.headers['X-Total'])
#     print(f'Total number of commits: {num_commits}')
# else:
#     print(f'Request failed with status code {response.status_code}')
