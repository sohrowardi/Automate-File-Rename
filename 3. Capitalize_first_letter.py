import os

# Get a list of all .mp4 files in the current directory
mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

# Iterate through the .mp4 files and rename them
for file in mp4_files:
    # Check if the first letter of the file name is already uppercase
    if file[0].islower():
        # Capitalize the first letter and keep the rest of the name
        new_name = file[0].upper() + file[1:]
        
        # Rename the file
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")
