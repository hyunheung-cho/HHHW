import os
import shutil

image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

# Create a static folder if it doesn't exist
static_folder = "static"
if not os.path.exists(static_folder):
    os.makedirs(static_folder)

# Get the list of files in the current directory
current_directory = os.getcwd()
files = os.listdir(current_directory)

# Copy image files to the static folder
for file in files:
    file_extension = os.path.splitext(file)[1]
    if file_extension.lower() in image_extensions:
        shutil.copy2(file, os.path.join(static_folder, file))
