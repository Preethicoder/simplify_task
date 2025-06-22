# 🗂️ Download Organizer Script

This Python script organizes files in your `~/Downloads/image` directory into subfolders based on their file extensions. It's useful for cleaning up your download folder by categorizing files like PDFs, images, documents, ZIP files, etc.

---

## 📁 What It Does

- Scans your `~/Downloads/image` folder.
- Moves files into categorized folders:
  - `pdf/` → `.pdf`
  - `program_file/` → `.py`, `.html`, `.db`, `.sqlite3`
  - `zip/` → `.zip`
  - `profile_photo/` → `.jpeg`
  - `image/` → `.jpg`, `.png`, `.gif`, etc.
  - `document/` → `.doc`, `.txt`, `.pptx`, `.xlsx`, etc.
- Skips any directories already present.

---

## 🚀 How to Use

### 1. Clone or Download

Save the script (e.g., as `organizer.py`) to your computer.

### 2. Run the Script

#### On Linux/macOS:
     ```bash
  python3 organizer.py

#### 3. Output
After running, you’ll see a message:
✅ Downloads organized successfully.
Files will now be sorted into folders like pdf/, image/, etc., inside ~/Downloads/image.

