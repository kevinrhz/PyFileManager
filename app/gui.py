import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) # Ensure the project root is in the Python path
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QListWidget, QFileDialog
)
from PyQt6.QtCore import Qt

# Import app funcitonalities
from app.file_operations import create_file, delete_file, open_file
from app.directory_operations import create_directory, delete_directory
from app.metadata import get_file_metadata
from app.search import search_file_by_name, search_files_by_extension



def open_selected_item(self, item):
    """Handles opening a file when double-clicked in the file list."""
    file_path = Path(item.text())

    result = open_file(file_path)

    if result.startswith("Error"):
        QMessageBox.warning(self, "Error", result)
    else:
        QMessageBox.information(self, "Success", result)



# Main GUI Class
class FileManagementApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Management System")
        self.setGeometry(100, 100, 600, 400)

        layout = QGridLayout()

        # Search bar in the upper right
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search files...")
        layout.addWidget(QLabel("Search:"), 0, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.search_bar, 0, 3, 1, 2)
        
        # File display area (list view for now)
        self.file_list = QListWidget(self)
        self.file_list.itemDoubleClicked.connect(open_selected_item)
        layout.addWidget(self.file_list, 1, 0, 1, 5)

        # Placeholder for sidebar
        self.sidebar = QListWidget(self)
        self.sidebar.addItem("Home")
        self.sidebar.addItem("Documents")
        self.sidebar.addItem("Downloads")
        # self.sidebar.itemClicked.connect(self.sidebar_navigation)
        layout.addWidget(self.sidebar, 1, 0, 1, 1) 

        # Browse button to change directory
        self.browse_button = QPushButton("Browse")
        # self.browse_button.clicked.connect(self.browse_directory)
        layout.addWidget(self.browse_button, 2, 1, 1, 1)
        

        # Set layout
        self.setLayout(layout)

        self.list_files(Path("test_folder"))



    # Function to create a file
    def create_file_action(self):
        file_name = self.file_input.text()
        if file_name:
            result = create_file(file_name, "Default content")
            self.result_area.setText(result)
        else:
            self.show_message("Error", "Please enter a valid file name.")

    # Function to delete a file
    def delete_file_action(self):
        file_name = self.file_input.text()
        if file_name:
            result = delete_file(file_name)
            self.result_area.setText(result)
        else:
            self.show_message("Error", "Please enter a valid file name.")

    # Function to create a directory
    def create_directory_action(self):
        dir_name = self.file_input.text()
        if dir_name:
            result = create_directory(dir_name)
            self.result_area.setText(result)
        else:
            self.show_message("Error", "Please enter a valid directory name.")

    # Function to delete a directory
    def delete_directory_action(self):
        dir_name = self.file_input.text()
        if dir_name:
            result = delete_directory(dir_name)
            self.result_area.setText(result)
        else:
            self.show_message("Error", "Please enter a valid directory name.")


    # Function to list files
    def list_files(self, directory):
        """Lists files in the given directory and updates the GUI file list."""
        self.file_list.clear()

        path = Path(directory)

        if not path.exists() or not path.is_dir():
            QMessageBox.warning(self, "Error", f"Directory '{directory}' not found.")
            return

        for file in path.iterdir():
            if file.is_file():
                self.file_list.addItem(str(file))


    # Function to search for files by name
    def search_file_by_name_action(self):
        file_name = self.search_input.text()
        if file_name:
            result = search_file_by_name(".", file_name)
            self.result_area.setText("\n".join(result) if isinstance(result, list) else result)
        else:
            self.show_message("Error", "Please enter a file name to search.")

    # Function to search for files by extension
    def search_files_by_extension_action(self):
        extension = self.search_input.text()
        if extension:
            result = search_files_by_extension(".", extension)
            self.result_area.setText("\n".join(result) if isinstance(result, list) else result)
        else:
            self.show_message("Error", "Please enter a file extension to search.")

    # Function to get file metadata
    def get_metadata_action(self):
        file_name = self.file_input.text().strip()

        if not file_name:
            self.show_message("Error", "Please enter a valid file name.")
            return

        file_path = Path(file_name).resolve()

        if not file_path.exists() or not file_path.is_file():
            self.show_message("Error", f"File '{file_name}' not found. Ensure you provide the correct path.")
            return

        result = get_file_metadata(str(file_path))

        if isinstance(result, dict):
            metadata_info = "\n".join([f"{key}: {value}" for key, value in result.items()])
            self.result_area.setText(metadata_info)
        else:
            self.show_message("Error", result)


    # Function to display messages
    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManagementApp()
    window.show()
    sys.exit(app.exec())
