import os
import shutil
from pathlib import Path

# Define the file types and their corresponding folders
FILE_TYPE_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Scripts': ['.py', '.sh', '.bat'],
    # Add more categories as needed
    'Others': []
}

def create_folders(base_path):
    """Create folders for each file type category."""
    for folder_name in FILE_TYPE_FOLDERS.keys():
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(base_path):
    """Move files into their corresponding folders based on file types."""
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)

        if os.path.isfile(item_path):
            file_extension = Path(item).suffix.lower()
            moved = False

            for folder_name, extensions in FILE_TYPE_FOLDERS.items():
                if file_extension in extensions:
                    shutil.move(item_path, os.path.join(base_path, folder_name, item))
                    moved = True
                    break

            if not moved:
                shutil.move(item_path, os.path.join(base_path, 'Others', item))

def main():
    # Ask the user for the directory path
    directory_to_organize = input("Please enter the path to the directory you want to organize: ").strip()

    # Check if the provided path exists
    if not os.path.exists(directory_to_organize):
        print(f"The directory '{directory_to_organize}' does not exist. Please check the path and try again.")
        return

    # Organize the files
    create_folders(directory_to_organize)
    organize_files(directory_to_organize)
    print(f"Files in '{directory_to_organize}' have been organized.")

if __name__ == "__main__":
    main()
