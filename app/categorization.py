from pathlib import Path
import shutil


FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".rar"],
    "Code": [".py", ".java", ".js", ".html", ".css"],
}


def categorize_files(directory):
    # Categorize files into subdirectories based on their type
    path = Path(directory)

    if not path.exists() or not path.is_dir():
        return f"Directory '{directory}' not found."
        return
    
    for file in path.iterdir():
        if file.is_file():
            file_extension = file.suffix.lower()
            category_found = False

            # Find the right category for the file
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    move_file_to_category(file, directory, category)
                    category_found = True
                    break

            if not category_found:
                move_file_to_category(file, directory, "Other")
            
    return "File categorization completed."


def move_file_to_category(file, base_directory, category):
    # Moves a file to its corresponding category folder
    category_path = Path(base_directory) / category
    category_path.mkdir(exist_ok=True)
    shutil.move(str(file), str(category_path / file.name))
    return f"Moved '{file.name}' to '{category}'"