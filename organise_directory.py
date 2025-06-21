import os
import shutil



DOWNLOAD_DIR = os.path.expanduser("~/Downloads/image")

FOLDER = {
    "pdf":[".pdf"],
    "program_file":[".py",".html",".db",".sqlite3"],
    "zip":[".zip"],
    "profile_photo":[".jpeg"],
    "image":[".jpg",".png",".gif",".bmp",".webp", ".tiff"],
    "document":[".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"]
}

def org_downloads():
    for filename in os.listdir(DOWNLOAD_DIR):
        file_path = os.path.join(DOWNLOAD_DIR,filename)

        if os.path.isdir(file_path):
            continue
        _,ext = os.path.splitext(filename)
        ext = ext.lower()

        for folder, extensions in FOLDER.items():
            if ext in extensions:
                dest_folder = os.path.join(DOWNLOAD_DIR,folder)
                print(dest_folder)
                os.makedirs(dest_folder,exist_ok=True)
                shutil.move(file_path,os.path.join(dest_folder,filename))
                break



def main():
    org_downloads()
    print("✅ Downloads organized successfully.")
if __name__ == "__main__":
    main()

