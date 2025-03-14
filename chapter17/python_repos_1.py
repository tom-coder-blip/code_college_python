import requests

# Set up the API URL
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Set headers to specify the API version and request JSON format
headers = {"Accept": "application/vnd.github.v3+json"}

# Make the API call
r = requests.get(url, headers=headers)

# Check if the request was successful
print(f"Status code: {r.status_code}")

# Convert the response to a dictionary
response_dict = r.json()

# Print the total repositories and check if results are complete
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Extract the list of repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]

# Print the number of keys and their names
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Print the keys from the response dictionary
print(response_dict.keys())

# Extract selected information from the first repository
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")   