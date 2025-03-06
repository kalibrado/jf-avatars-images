import os
import json
from urllib.parse import urljoin
from PIL import Image
from datetime import datetime

def generate_image_metadata(image_folder, base_url, output_file):
    image_data = []
    
    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, image_folder)
                url = urljoin(base_url, relative_path.replace('\\', '/'))
                
                # Récupération des métadonnées de l'image
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size  # Dimensions de l'image
                        size_in_bytes = os.path.getsize(file_path)  # Taille en octets
                        creation_time = os.path.getctime(file_path)  # Timestamp de création
                        creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')  # Format lisible
                        
                        # Ajout des données au tableau
                        image_data.append({
                            "name": os.path.splitext(file)[0],  # Nom sans extension
                            "url": f"{url}?raw=true",
                            "size_in_bytes": size_in_bytes,
                            "dimensions": {"width": width, "height": height},
                            "creation_date": creation_date
                        })
                except Exception as e:
                    print(f"Erreur lors du traitement de l'image {file}: {e}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(image_data, f, indent=2, ensure_ascii=False)

    print(f"Fichier JSON généré : {output_file}")

image_folder = "images"
base_url = "https://github.com/kalibrado/js-avatars-images/blob/main/images/"
output_file = "images_metadata.json"

generate_image_metadata(image_folder, base_url, output_file)
