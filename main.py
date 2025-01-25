from app.file_operations import create_file, delete_file, bulk_create_files, bulk_delete_files, bulk_move_files
from app.directory_operations import create_directory, list_directory_contents, delete_directory
from app.search import search_file_by_name, search_files_by_extension, search_files_by_pattern
from app.categorization import categorize_files
from app.metadata import get_file_metadata
from app.logger import log_event




# create_file("test_folder/sample.txt", "This is a test file")

# get_file_metadata("test_folder/sample.txt")

# list_directory_contents("test_folder")





# Create a file and capture the return message
result = create_file("test_folder/test_gui.txt", "For GUI testing")
print(result)

# Delete the file and capture the return message
result = delete_file("test_folder/test_gui.txt")
print(result)