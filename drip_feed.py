import os
import shutil

# This must match the folder name you pushed
SOURCE_DIR = "pending_solutions"
TARGET_DIR = "." 

if os.path.exists(SOURCE_DIR):
    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith(".py")])
    if files:
        next_file = files[0]
        shutil.move(os.path.join(SOURCE_DIR, next_file), os.path.join(TARGET_DIR, next_file))
        print(f"Moved {next_file}")
    else:
        print("No files left!")
else:
    print("Folder not found!")