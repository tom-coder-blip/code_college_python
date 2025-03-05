from pathlib import Path
import json

path = Path("favorite_number.json")


contents = path.read_text()
fav_number = json.loads(contents)

