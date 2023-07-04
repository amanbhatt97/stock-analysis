import os

# Get the current file's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

class ProjectPaths:
    def __init__(self, parent_directory):
        self.parent_directory = parent_directory
        self.raw_data = os.path.join(parent_directory, 'data', 'raw_data')
        self.processed_data = os.path.join(parent_directory, 'data', 'processed_data')

