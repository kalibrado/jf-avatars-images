import os
import json
from urllib.parse import urljoin
from PIL import Image
from datetime import datetime


base_url = "https://raw.githubusercontent.com/kalibrado/js-avatars-images/main/images/"
image_folder = "images"
output_src_images = "images_metadata.json"
output_src_folders = "folders_names.json"


def generate_image_metadata(image_folder, base_url, output_src_images):
    image_data = []
    folders_names = []

    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                file_path = os.path.join(root, file)
                folder_name = os.path.basename(root)
                relative_path = os.path.relpath(file_path, image_folder)
                url = urljoin(base_url, relative_path.replace("\\", "/"))
                if not folder_name in folders_names:
                    folders_names.append(folder_name)

                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        size_in_bytes = os.path.getsize(file_path)
                        creation_time = os.path.getctime(file_path)
                        creation_date = datetime.fromtimestamp(creation_time).strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )

                        image_data.append(
                            {
                                "name": os.path.splitext(file)[0],
                                "folder": folder_name,
                                "url": f"{url}?raw=true",
                                "size_in_bytes": size_in_bytes,
                                "dimensions": {"width": width, "height": height},
                            }
                        )
                except Exception as e:
                    print(f"Erreur lors du traitement de l'image {file}: {e}")

    with open(output_src_images, "w", encoding="utf-8") as f:
        json.dump(image_data, f, indent=2, ensure_ascii=False)
    print(f"Fichier JSON généré : {output_src_images}")

    with open(output_src_folders, "w", encoding="utf-8") as f:
        json.dump(folders_names, f, indent=2, ensure_ascii=False)
    print(f"Fichier JSON généré : {output_src_folders}")


generate_image_metadata(image_folder, base_url, output_src_images)
