import os

# Get the keyword from the user
keyword = input("Enter the keyword to search for: ")

# Get a list of all .mp4 files in the current directory
mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

# Iterate through the .mp4 files and rename them
for file in mp4_files:
    if keyword in file:
        new_name = file.replace(keyword, "")
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")
