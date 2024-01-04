'''
import os

# Get a list of all .mp4 files in the current directory
mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

# Suggest a base name based on the common pattern in file names
suggested_base_name = ""
if mp4_files:
    # Extract the common pattern from the first file name
    common_pattern = mp4_files[0].split(' (')[0]
    suggested_base_name = common_pattern

# Prompt the user for the base name with the suggestion
user_input = input(f"Enter the base name for the files (suggested: '{suggested_base_name}'): ")

# Use the suggested base name if the user input is empty
base_name = suggested_base_name if not user_input else user_input

# Create a list of (file, modified_time) tuples
file_mod_times = [(file, os.path.getmtime(file)) for file in mp4_files]

# Sort the files by their modified time
file_mod_times.sort(key=lambda x: x[1])

# Iterate through the sorted list and rename the files with the base name and numbers
for i, (file, _) in enumerate(file_mod_times):
    # Get the extension of the file
    _, extension = os.path.splitext(file)
    
    # Generate the new name with the base name and a number
    new_name = f"{base_name} ({i}){extension}"
    
    # Rename the file, overwriting existing files with the same names
    os.rename(file, new_name)
    print(f"Renamed '{file}' to '{new_name}'")
'''

import os

# Get a list of all .mp4 files in the current directory
mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

# Suggest a base name based on the common pattern in file names
suggested_base_name = ""
if mp4_files:
    # Extract the common pattern from the first file name
    common_pattern = mp4_files[0].split(' (')[0]
    suggested_base_name = common_pattern

# Prompt the user for the base name with the suggestion
user_input = input(f"Enter the base name for the files (suggested: '{suggested_base_name}'): ")

# Use the suggested base name if the user input is empty
base_name = suggested_base_name if not user_input else user_input

# Create a list of (file, modified_time) tuples
file_mod_times = [(file, os.path.getmtime(file)) for file in mp4_files]

# Sort the files by their modified time
file_mod_times.sort(key=lambda x: x[1])

# Rename the files with the base name and numbers based on the modified time
for i, (file, _) in enumerate(file_mod_times):
    _, extension = os.path.splitext(file)
    new_name = f"{base_name} ({i}){extension}"
    os.rename(file, new_name)

# Get the list of .mp4 files again
mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

# Create a list of (file, modified_time) tuples for the new file order
file_mod_times = [(file, os.path.getmtime(file)) for file in mp4_files]

# Sort the files by their modified time
file_mod_times.sort(key=lambda x: x[1])

# Rename the files with the user's input and numbers based on the modified time
for i, (file, _) in enumerate(file_mod_times):
    _, extension = os.path.splitext(file)
    new_name = f"{base_name} ({i}){extension}"
    os.rename(file, new_name)
    print(f"Renamed '{file}' to '{new_name}'")
