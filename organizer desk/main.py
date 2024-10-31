import os
import shutil
from pathlib import Path

def organize_desktop():
    # Get desktop path
    desktop = str(Path.home() / "Desktop")
    
    # Dictionary to map file extensions to folder names
    extension_map = {
        # Images
        '.png': 'Screenshots',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.gif': 'Images',
        
        # Documents
        '.pdf': 'PDFs',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        
        # Other common types
        '.zip': 'Archives',
        '.exe': 'Programs',
    }
    
    # Iterate through files on desktop
    for filename in os.listdir(desktop):
        file_path = os.path.join(desktop, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
            
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Skip if no extension
        if not file_extension:
            continue
            
        # Get the target folder name from our mapping
        folder_name = extension_map.get(file_extension, 'Other')
        
        # Create the folder if it doesn't exist
        folder_path = os.path.join(desktop, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        # Move the file
        try:
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved {filename} to {folder_name}")
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")

if __name__ == "__main__":
    organize_desktop()
