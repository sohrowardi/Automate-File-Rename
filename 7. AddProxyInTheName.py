import os

def rename_video_files(folder_path):
    for filename in os.listdir(folder_path):
        if "_Proxy" in filename:
            continue
        elif "_01" in filename:
            new_filename = filename.replace("_01", "_Proxy")
        else:
            new_filename = filename.rsplit(".", 1)[0] + "_Proxy." + filename.rsplit(".", 1)[1]
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

# Get the current working directory
folder_path = os.getcwd()

rename_video_files(folder_path)
