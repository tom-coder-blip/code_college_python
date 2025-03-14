import requests
import plotly.express as px

# Ask the user for a programming language
language = input("Enter a programming language: ")

# Make an API call to GitHub
url = f"https://api.github.com/search/repositories?q=language:{language}+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Check if API call was successful
if r.status_code != 200:
    print(f"Failed to retrieve data: {r.status_code}")
else:
    response_dict = r.json()
    
    # Extract repository names and star counts
    repo_dicts = response_dict.get("items", [])
    repo_names, stars = [], []

    for repo_dict in repo_dicts:
        repo_names.append(repo_dict["name"])
        stars.append(repo_dict["stargazers_count"])

    # Check if repositories were found
    if repo_names and stars:
        # Create a styled bar chart
        title = f"Most-Starred {language.capitalize()} Projects on GitHub"
        labels = {'x': 'Repository', 'y': 'Stars'}

        fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

        # Customize font sizes for readability
        fig.update_layout(
            title_font_size=28,  
            xaxis_title_font_size=20,  
            yaxis_title_font_size=20   
        )

        fig.show()
    else:
        print(f"No repositories found for {language}.")