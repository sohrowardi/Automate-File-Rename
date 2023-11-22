import os
import datetime

def rename_all_files():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Get the creation time of the file
        created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        
        # Format the new filename
        new_filename = created_time.strftime("%y-%m-%d [%H%M]") + os.path.splitext(filename)[1]
        
        # Check if the new filename already exists
        count = 1
        while os.path.exists(os.path.join(folder_path, new_filename)):
            new_filename = created_time.strftime("%y-%m-%d [%H%M]") + f"_{count}" + os.path.splitext(filename)[1]
            count += 1
        
        # Rename the file
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    rename_all_files()
