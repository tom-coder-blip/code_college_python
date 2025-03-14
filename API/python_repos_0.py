import requests

# Step 1: Set up the API URL
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Step 2: Set headers to specify the API version and request JSON format
headers = {"Accept": "application/vnd.github.v3+json"}

# Step 3: Make the API call
r = requests.get(url, headers=headers)

# Step 4: Check if the request was successful
print(f"Status code: {r.status_code}")

# Step 5: Convert the response to a dictionary
response_dict = r.json()

# Step 6: Print the keys from the response dictionary
print(response_dict.keys())