import os
import shutil

#CHANGE PATH ACCORDING TO NEED
path = "C:\\Users\\panch\\OneDrive\\Desktop\\Python\\ProjectFiles" 

folders = {
    "Images": ["png", "jpg"],
    "Documents": ["pdf", "docx"],
    "Scripts": ["cpp", "c", "py", "txt"]
}

# Create folders if not exist
for folder in folders.keys():
    os.makedirs(os.path.join(path, folder), exist_ok=True)

# Create Others folder too
others_path = os.path.join(path, "Others")
os.makedirs(others_path, exist_ok=True)

# List all files
files = os.listdir(path)

# Organize files
for file in files:
    file_path = os.path.join(path, file)

    # Only move files (not folders)
    if os.path.isfile(file_path):
        ext = file.split('.')[-1].lower()
        moved = False

        for folder_name, extensions in folders.items():
            if ext in extensions:
                dest_path = os.path.join(path, folder_name, file)
                try:
                    shutil.move(file_path, dest_path)
                    print(f"✅ Moved {file} → {folder_name}/")
                    moved = True
                    break
                except Exception as e:
                    print(f"❌ Error moving {file}: {e}")
                    moved = True
                    break

        if not moved:
            try:
                dest_path = os.path.join(others_path, file)
                shutil.move(file_path, dest_path)
                print(f"📁 Moved {file} → Others/")
            except Exception as e:
                print(f"❌ Error moving {file} to Others: {e}")
