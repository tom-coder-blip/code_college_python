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
repo_names, stars, hover_texts = [], [], []


for repo in repo_dicts:
    repo_names.append(repo["name"])
    stars.append(repo["stargazers_count"])

    # Step 4: Build hover text with owner and description
    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_text = f"{owner}<br />{description}"  # Adding line break in tooltip
    hover_texts.append(hover_text)

# Create a styled bar chart
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

# Step 5: Create and display the bar chart
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Customize font sizes for readability
fig.update_layout(
    title_font_size=28,  # Increase title font size
    xaxis_title_font_size=20,  # Increase X-axis label size
    yaxis_title_font_size=20   # Increase Y-axis label size
)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show() 
