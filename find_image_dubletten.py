import os
from PIL import Image
import imagehash

# Verzeichnis, in dem sich Ihre Bilder befinden
IMAGE_DIR = 'IMAGES'

# Funktion zum Scannen von Bildern und Berechnung von Hashes
def find_duplicate_images(image_dir):
    image_hashes = {}
    duplicates = []

    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                file_path = os.path.join(root, file)
                try:
                    img = Image.open(file_path)
                    img_hash = imagehash.average_hash(img)
                    if img_hash in image_hashes:
                        duplicates.append((file_path, image_hashes[img_hash]))
                    else:
                        image_hashes[img_hash] = file_path
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
    
    return duplicates

# Duplikate finden
duplicates = find_duplicate_images(IMAGE_DIR)

# Ergebnis anzeigen
if duplicates:
    print("Duplicate images found:")
    for dup in duplicates:
        print(f"Duplicate: {dup[0]} and {dup[1]}")
else:
    print("No duplicates found.")
