# js-avatars-images

A curated collection of avatar images and metadata designed to work seamlessly with the [jf-avatars](https://github.com/kalibrado/jf-avatars) project.

This repository contains avatar images and a metadata index used to dynamically populate the avatar selector interface.

## 📁 Repository Structure

- `images/` : All avatar images are stored here  
- `images_metadata.json` : Auto-generated metadata for all images  
- `image_indexer.py` : Python script to regenerate metadata (used internally or locally)

## 🧠 How It Works

- The `images/` folder contains all available avatar images.
- A GitHub Action (or manual script) scans the folder and generates a `images_metadata.json` file.
- This metadata is used by [jf-avatars](https://github.com/kalibrado/jf-avatars) to display and filter the avatars in the UI.

## 🚀 Usage with jf-avatars

To use this image repository with `jf-avatars`, simply point to the latest release of the JS module:

```html
<script
  type="module"
  src="https://github.com/kalibrado/js-avatars/releases/download/{version}/main.js"
  defer
></script>
```

Make sure to replace `{version}` with the desired release tag (e.g., `v1.0.0`).

## 🛠 Regenerate Metadata

To regenerate the `images_metadata.json` file manually after adding or changing images:

```bash
python image_indexer.py
```

> ⚙️ **Note**: In production, a GitHub Action will automatically regenerate this file when changes are pushed to the `images/` directory.

## 🖼 Adding New Avatars

1. Add your image(s) to the `images/` directory.
2. Commit and push the changes.
3. A GitHub workflow will run and automatically update the `images_metadata.json`.

## 🤝 Contributing

Feel free to open a PR if you'd like to contribute new avatars!  
Please ensure the following:
- Images are square (1:1 ratio)
- Max size around 512x512 px
- Content is appropriate for public use
