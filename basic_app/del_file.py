import os

folder_path = "C:/Users/ulugbek/PycharmProjects/Kale_project/media"

# Loop through all the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".png"):
        # If the file is a PNG image, delete it
        os.remove(os.path.join(folder_path, file_name))