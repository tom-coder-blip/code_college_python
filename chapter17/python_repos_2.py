import requests
import time

# Step 1: Make an API call to check rate limits
url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Step 2: Convert response to dictionary
rate_limit_data = r.json()

# Step 3: Extract search API rate limit information
search_limit = rate_limit_data["rate"]["limit"]
search_remaining = rate_limit_data["rate"]["remaining"]
reset_time = rate_limit_data["rate"]["reset"]  # Unix timestamp

# Step 4: Convert Unix time to readable format
reset_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_time))

# Step 5: Print the results
print(f"Search API Limit: {search_limit} requests per minute")
print(f"Requests remaining: {search_remaining}")
print(f"Limit resets at: {reset_time_readable}")

