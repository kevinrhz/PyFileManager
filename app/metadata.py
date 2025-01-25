from pathlib import Path
import os
from datetime import datetime


def get_file_metadata(file_path):
    # Retrieve and display metadata for a given file
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return f"File '{file_path}' not found."

    # Extracting metadata
    metadata = {
        "File Name": path.name,
        "File Size (KB)": round(path.stat().st_size / 1024, 2),
        "Created On": datetime.fromtimestamp(path.stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
        "Last Modified": datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        "File Type": path.suffix.lower() or "Unknown"
    }

    return metadata
