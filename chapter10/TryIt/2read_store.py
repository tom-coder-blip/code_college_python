from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    # Read and display the stored favorite number
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"I know your favorite number! It’s {fav_number}.")
else:
    # Ask for the favorite number and store it
    fav_number = input("Enter your favorite number: ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print("Your favorite number has been stored!")