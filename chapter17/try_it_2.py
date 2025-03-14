import requests
import matplotlib.pyplot as plt
from operator import itemgetter

# Make an API call to get the top stories.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    try:
        # Make a new API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        response_dict = r.json()

        # Check if 'descendants' (comment count) exists, otherwise skip.
        if 'descendants' not in response_dict:
            continue

        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)

    except KeyError:
        continue  # Skip any entries with missing keys

# Sort submissions by comment count
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Extract titles, comment counts, and links
titles = [submission['title'] for submission in submission_dicts]
comment_counts = [submission['comments'] for submission in submission_dicts]
links = [submission['hn_link'] for submission in submission_dicts]

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(titles, comment_counts, color='skyblue')

# Invert y-axis to have the most commented post on top
plt.gca().invert_yaxis()

# Add labels
plt.xlabel("Number of Comments")
plt.ylabel("Hacker News Discussions")
plt.title("Most Active Discussions on Hacker News")

# Show the chart
plt.show()