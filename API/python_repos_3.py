import requests
import plotly.express as px

# Step 1: Make an API call to GitHub
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Step 2: Check if API call was successful
print(f"Status code: {r.status_code}")

# Step 3: Process the response data
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}") 

# Step 4: Extract repository names and star counts
repo_dicts = response_dict["items"]
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# Create a styled bar chart
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

# Step 5: Create and display the bar chart
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

# Customize font sizes for readability
fig.update_layout(
    title_font_size=28,  # Increase title font size
    xaxis_title_font_size=20,  # Increase X-axis label size
    yaxis_title_font_size=20   # Increase Y-axis label size
)

fig.show() 
