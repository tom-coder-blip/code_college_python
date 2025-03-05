from pathlib import Path

# Create the file and write content
file_path = Path('tom_textfile.txt')
file_path.write_text('Lets get it')

# Read the entire content and print it
contents = file_path.read_text()
print(contents)

# Create a new file and write content
file_path = Path("learning_python.tx")
file_path.write_text("Get in lads!")

# Append text to the file
with file_path.open(mode='a') as file:
    file.write("\nYou have such an amazing pair of shoes!\nYou drip is too clean.")