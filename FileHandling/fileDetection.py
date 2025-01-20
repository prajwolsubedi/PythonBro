#Python file detection

import os

file_path = "fileDetection.py"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")
else:
    print(f"The file doesn't exists")