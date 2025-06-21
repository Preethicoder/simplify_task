import os
import shutil

# 📂 Directory to organize
DOWNLOAD_DIR = os.path.expanduser("~/Downloads/image")

# 📦 Folder mapping based on file extensions
FOLDER = {
    "pdf": [".pdf"],
    "program_file": [".py", ".html", ".db", ".sqlite3"],
    "zip": [".zip"],
    "profile_photo": [".jpeg"],
    "image": [".jpg", ".png", ".gif", ".bmp", ".webp", ".tiff"],
    "document": [".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"]
}

def org_downloads():
    """
    Organizes files in the DOWNLOAD_DIR by moving them into subfolders based on their file extensions.

    - Ignores directories inside DOWNLOAD_DIR.
    - Checks each file's extension and moves it to a corresponding folder defined in the FOLDER dictionary.
    - Creates folders if they do not already exist.
    """
    for filename in os.listdir(DOWNLOAD_DIR):
        file_path = os.path.join(DOWNLOAD_DIR, filename)

        if os.path.isdir(file_path):
            continue  # Skip directories

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        for folder, extensions in FOLDER.items():
            if ext in extensions:
                dest_folder = os.path.join(DOWNLOAD_DIR, folder)
                print(dest_folder)
                os.makedirs(dest_folder, exist_ok=True)  # Create folder if not exists
                shutil.move(file_path, os.path.join(dest_folder, filename))
                break  # Stop checking once matched


def main():
    """
    Main function to trigger the organization of the downloads directory.
    """
    org_downloads()
    print("✅ Downloads organized successfully.")

if __name__ == "__main__":
    main()
