#!/usr/bin/env python3
"""Strip EXIF metadata from images in the resources folder."""

from pathlib import Path

from PIL import Image

RESOURCES = Path(__file__).parent / "resources"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tiff"}


def strip_exif(path: Path) -> None:
    with Image.open(path) as img:
        has_exif = bool(img.getexif())
        if not has_exif:
            print(f"  clean: {path.name}")
            return
        # Rebuild the image from raw pixel data so no metadata carries over
        data = list(img.getdata())
        stripped = Image.new(img.mode, img.size)
        stripped.putdata(data)
        stripped.save(path)
        print(f"stripped: {path.name}")


def main() -> None:
    images = sorted(p for p in RESOURCES.iterdir() if p.suffix.lower() in EXTENSIONS)
    print(f"Found {len(images)} image(s) in {RESOURCES}\n")
    for path in images:
        try:
            strip_exif(path)
        except Exception as e:
            print(f"   error: {path.name} ({e})")
    print("\nDone.")


if __name__ == "__main__":
    main()
