from pathlib import Path
import json

fav_number = input("Enter your favorite number: ")

path = Path("favorite_number.json")
contents = json.dumps(fav_number)
path.write_text(contents)

print("Your favorite number has been stored!")