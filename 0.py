import os
import datetime

def add_prefix():
    keyword = input("Enter the keyword to add as a prefix to the file names: ")
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]
    for file in mp4_files:
        base_name, extension = os.path.splitext(file)
        new_name = f"{keyword}{base_name}{extension}"
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")

def add_suffix():
    suffix = input("Enter the suffix to add as a suffix to the file names: ")
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]
    for file in mp4_files:
        base_name, extension = os.path.splitext(file)
        new_name = f"{base_name}{suffix}{extension}"
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")

def capitalize_first_letter():
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]
    for file in mp4_files:
        if file[0].islower():
            new_name = file[0].upper() + file[1:]
            os.rename(file, new_name)
            print(f"Renamed '{file}' to '{new_name}'")

def remove_keyword():
    keyword = input("Enter the keyword to search for: ")
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]
    for file in mp4_files:
        if keyword in file:
            new_name = file.replace(keyword, "")
            os.rename(file, new_name)
            print(f"Renamed '{file}' to '{new_name}'")

def rename_by_modified_time():
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]
    suggested_base_name = ""
    if mp4_files:
        common_pattern = mp4_files[0].split(' (')[0]
        suggested_base_name = common_pattern
    user_input = input(f"Enter the base name for the files (suggested: '{suggested_base_name}'): ")
    base_name = suggested_base_name if not user_input else user_input
    file_mod_times = [(file, os.path.getmtime(file)) for file in mp4_files]
    file_mod_times.sort(key=lambda x: x[1])
    for i, (file, _) in enumerate(file_mod_times):
        _, extension = os.path.splitext(file)
        new_name = f"{base_name} ({i}){extension}"
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")

def rename_yy_mm_dd_hhmm():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        new_filename = created_time.strftime("%y-%m-%d [%H%M]") + os.path.splitext(filename)[1]
        count = 1
        while os.path.exists(os.path.join(folder_path, new_filename)):
            new_filename = created_time.strftime("%y-%m-%d [%H%M]") + f"_{count}" + os.path.splitext(filename)[1]
            count += 1
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')

def add_proxy_in_the_name():
    folder_path = os.getcwd()
    for filename in os.listdir(folder_path):
        if "_Proxy" in filename:
            continue
        elif "_01" in filename:
            new_filename = filename.replace("_01", "_Proxy")
        else:
            new_filename = filename.rsplit(".", 1)[0] + "_Proxy." + filename.rsplit(".", 1)[1]
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

def main():
    print("1. Add Prefix")
    print("2. Add Suffix")
    print("3. Capitalize First Letter")
    print("4. Remove Keyword")
    print("5. Rename by Modified Time")
    print("6. Rename YY-MM-DD [HHMM]")
    print("7. Add Proxy in the Name")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_prefix()
    elif choice == '2':
        add_suffix()
    elif choice == '3':
        capitalize_first_letter()
    elif choice == '4':
        remove_keyword()
    elif choice == '5':
        rename_by_modified_time()
    elif choice == '6':
        rename_yy_mm_dd_hhmm()
    elif choice == '7':
        add_proxy_in_the_name()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
