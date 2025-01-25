from pathlib import Path


def search_file_by_name(directory, file_name):
    # Search for a file by name within a directory.
    path = Path(directory).resolve()

    if not path.exists() or not path.is_dir():
        return f"Directory '{directory}' not found."
    
    file_name = Path(file_name).name

    found_files = [str(file) for file in path.rglob(file_name)]

    if found_files:
        result = f"Found {len(found_files)} matching file(s):\n"
        result += "\n".join(found_files)
        return result
    else:
        return f"No files named '{file_name}' found in '{directory}'."



def search_files_by_extension(directory, extension):
# Search for files with a specific extension
    path = Path(directory)

    if not path.exists() or not path.is_dir():
        return f"Directory '{directory}' not found."
        return
    
    found_files = list(path.rglob(f"*.{extension}"))

    if found_files:
        return f"Found {len(found_files)} '.{extension}' files:"
        for file in found_files:
            print(file)
    else:
        return f"No '.{extension}' files found in '{directory}'."


def search_files_by_pattern(directory, pattern):
    # Search for files matching a pattern (e.g., 'report_*.txt')
    path = Path(directory)

    if not path.exists() or not path.is_dir():
        return f"Directory '{directory}' not found."
        return
    
    found_files = list(path.rglob(pattern))

    if found_files:
        return f"Found {len(found_files)} file(s) matching '{pattern}':"
        for file in found_files:
            print(file)
    else:
        return f"No files matching '{pattern}' found in '{directory}'."