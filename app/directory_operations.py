from pathlib import Path
import shutil
from app.logger import log_event




def create_directory(dir_name):
    """Creates a directory if it doesn't exist, with error handling."""
    path = Path(dir_name)

    try:
        path.mkdir(parents=True, exist_ok=True)
        log_event("info", f"Directory '{dir_name}' created successfully.")
        return f"Directory '{dir_name}' created successfully."

    except PermissionError:
        log_event("error", f"Permission denied when creating directory: {dir_name}")
        return f"Error: Permission denied when creating '{dir_name}'."

    except Exception as e:
        log_event("error", f"Unexpected error when creating directory: {str(e)}")
        return f"An unexpected error occurred: {e}"



def list_directory_contents(dir_name):
    """Lists all files and subdirectories, handling missing directory errors."""
    path = Path(dir_name)

    try:
        if path.exists() and path.is_dir():
            return f"Contents of '{dir_name}':"
            for item in path.iterdir():
                return item.name
            log_event("info", f"Listed contents of '{dir_name}'.")
        else:
            log_event("warning", f"Directory '{dir_name}' not found.")
            return f"Directory '{dir_name}' not found."
    except PermissionError:
        log_event("error", f"Permission denied when accessing '{dir_name}'")
        return f"Error: Permission denied when accessing '{dir_name}'."

    except Exception as e:
        log_event("error", f"Unexpected error when listing directory: {str(e)}")
        return f"An unexpected error occurred: {e}"



def delete_directory(dir_name):
    """Deletes a directory, even if it contains files, with safety checks."""
    path = Path(dir_name)

    try:
        if path.exists() and path.is_dir():
            shutil.rmtree(path)  # Deletes directory and all its contents
            log_event("info", f"Directory '{dir_name}' deleted successfully.")
            return f"Directory '{dir_name}' deleted successfully."
        else:
            log_event("warning", f"Directory '{dir_name}' not found.")
            return f"Directory '{dir_name}' not found."

    except PermissionError:
        log_event("error", f"Permission denied when deleting directory: {dir_name}")
        return f"Error: Permission denied when deleting '{dir_name}'."

    except Exception as e:
        log_event("error", f"Unexpected error when deleting directory: {str(e)}")
        return f"An unexpected error occurred: {e}"