from pathlib import Path
import subprocess
import platform
from app.logger import log_event



def create_file(file_name, content=""):
    """Creates a new file with optional content, if it doesnt exist. Has error handling."""
    path = Path(file_name)
    
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        
        if path.exists():
            log_event("warning", f"File '{file_name}' already exists.")
            return f"File '{file_name}' already exists."
        
        path.write_text(content)
        log_event("info", f"File '{file_name}' created successfully.")
        return f"File '{file_name}' created successfully."

    except PermissionError:
        log_event("error", f"Permission denied when creating file: {file_name}")
        return f"Error: Permission denied when creating '{file_name}'."

    except Exception as e:
        log_event("error", f"Unexpected error when creating file: {str(e)}")
        return f"An unexpected error occurred: {e}"



def delete_file(file_name):
    """Deletes a file if it exists, with error handling"""
    path = Path(file_name)
    
    try:
        if path.exists():
            path.unlink()
            log_event("info", f"File '{file_name}' deleted successfully.")
            return f"File '{file_name}' deleted successfully."
        else:
            log_event("warning", f"File '{file_name}' not found.")
            return f"File '{file_name}' not found."
    
    except PermissionError:
        log_event("error", f"Permission denied when deleting file: {file_name}")
        return f"Error: Permission denied when deleting '{file_name}'."

    except Exception as e:
        log_event("error", f"Unexpected error when deleting file: {str(e)}")
        return f"An unexpected error occurred: {e}"


def open_file(file_path):
    """Opens a file using the default system application."""
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        return f"Error: File '{file_path}' not found."
    
    try:
        if platform.sytem() == "Windows":
            subprocess.run(["start", str(path)], shell=True, check=True)
        elif platform.system() == "Darwin": # macOS
            subprocess.run(["open", str(path)], check=True)
        else: # Linux
            subprocess.run(["xdg-open", str(path)], check=True)
        
        return f"Opened '{file_path}' successfully."
    except Exception as e:
        return f"Error opening file: {e}"


def bulk_create_files(file_list):
    """Create multiple files with optional content."""
    for file_name, content in file_list:
        try:
            path = Path(file_name)
            path.parent.mkdir(parents=True, exist_ok=True)

            if path.exists():
                log_event("warning", f"File '{file_name}' already exists.")
                return f"File '{file_name}' already exists."
            else:
                path.write_text(content)
                log_event("info", f"File '{file_name}' created successfully.")
                return f"File '{file_name}' created successfully."

        except PermissionError:
            log_event("error", f"Permission denied when creating file: {file_name}")
            return f"Error: Permission denied when creating '{file_name}'."

        except Exception as e:
            log_event("error", f"Unexpected error when creating '{file_name}': {str(e)}")
            return f"An unexpected error occurred: {e}"


def bulk_delete_files(file_list):
    """Deletes multiple files, with error handling"""
    for file_name in file_list:
        try:
            path = Path(file_name)
            if path.exists():
                path.unlink()
                log_event("info", f"File '{file_name}' deleted successfully.")
                return f"File '{file_name}' deleted successfully."
            else:
                log_event("warning", f"File '{file_name}' not found.")
                return f"File '{file_name}' not found."

        except PermissionError:
            log_event("error", f"Permission denied when deleting file: {file_name}")
            return f"Error: Permission denied when deleting '{file_name}'."

        except Exception as e:
            log_event("error", f"Unexpected error when deleting '{file_name}': {str(e)}")
            return f"An unexpected error occurred: {e}"



def bulk_move_files(file_list, target_directory):
    """Moves multiple files to a target directory"""
    target_path = Path(target_directory)

    try:
        target_path.mkdir(parents=True, exist_ok=True)

        for file_name in file_list:
            source_path = Path(file_name)
            if source_path.exists():
                new_location = target_path / source_path.name
                source_path.rename(new_location)
                log_event("info", f"Moved '{file_name}' to '{target_directory}'.")
                return f"Moved '{file_name}' to '{target_directory}'."
            else:
                log_event("warning", f"File '{file_name}' not found.")
                return f"File '{file_name}' not found."

    except PermissionError:
        log_event("error", f"Permission denied when moving files to: {target_directory}")
        return f"Error: Permission denied when moving to '{target_directory}'."

    except Exception as e:
        log_event("error", f"Unexpected error while moving files: {str(e)}")
        return f"An unexpected error occurred: {e}"
