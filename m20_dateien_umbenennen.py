"""
Kopiert Dateien in ein neues Verzeichnis,
benennt sie um und ersetzt Unterstriche durch Leerzeichen.
"""
from pathlib import Path
import shutil

base_dir = Path("dateien_original")
target_dir = Path("dateien_kopie")
target_dir.mkdir(exist_ok=True)

for child in base_dir.iterdir():
    if child.is_file():
        filename_old = child.name
        filename_new = filename_old.replace("_", " ")
        target_path = target_dir.joinpath(filename_new)
        print("Kopiere:", target_path)
        shutil.copy2(child, target_path)
