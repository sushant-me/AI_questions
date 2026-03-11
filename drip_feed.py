import os
import shutil

# Configuration
SOURCE_DIR = "pending_solutions"
TARGET_DIR = "." # Move to the main folder

# Get the list of generated files (day_116, day_117, etc.)
if not os.path.exists(SOURCE_DIR):
    print("Folder not found!")
    exit()

files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith(".py")])

if files:
    next_file = files[0] # Take the first one in the list
    source_path = os.path.join(SOURCE_DIR, next_file)
    target_path = os.path.join(TARGET_DIR, next_file)
    
    # Move the file out of the hidden folder into the main repo
    shutil.move(source_path, target_path)
    print(f"Successfully moved {next_file}")
else:
    print("All 300 days are already uploaded!")