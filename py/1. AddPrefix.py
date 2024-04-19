import os

# Get the keyword from the user
keyword = input("Enter the keyword to add as a prefix to the file names: ")

# Get a list of all .mp4 files in the current directory
mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

# Iterate through the .mp4 files and rename them
for file in mp4_files:
    # Split the file name and extension
    base_name, extension = os.path.splitext(file)
    
    # Add the keyword as a prefix directly to the base name and recombine with the extension
    new_name = f"{keyword}{base_name}{extension}"
    
    # Rename the file
    os.rename(file, new_name)
    print(f"Renamed '{file}' to '{new_name}'")
