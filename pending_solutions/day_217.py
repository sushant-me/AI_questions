"""
Create file search program.
"""

import os

def search_files(directory, target_name):
    """
    Search for files with a given name in a directory and its subdirectories.
    
    Args:
    directory (str): The root directory to start the search.
    target_name (str): The name of the file to search for.
    
    Returns:
    list: A list of file paths where the target file is found.
    """
    found_files = []
    for root, _, files in os.walk(directory):
        if target_name in files:
            found_files.append(os.path.join(root, target_name))
    return found_files

# Example usage:
# search_results = search_files('/path/to/search', 'example.txt')
# print(search_results)