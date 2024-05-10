import os
import click
import shutil
from pathlib import Path
from PIL import Image

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)  # remove files and symbolic links
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # remove directories
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

@click.command()
@click.option('--src_dir', '-s', help='Spotlight Source directory', default="%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
@click.option('--dest_dir', '-d', help='Spotlight Destination directory', default="./wallpapers")
def main(src_dir:str, dest_dir:str):
    # Expand environment variables
    src_dir = os.path.expandvars(src_dir)
    dest_dir = os.path.expandvars(dest_dir)

    if not os.path.exists(src_dir) or not os.path.isdir(src_dir):
        raise RuntimeError(f"Sportlight source is incorrect.")

    if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
        raise RuntimeError(f"{dest_dir} should be a directory.")
    
    if os.path.exists(dest_dir):
        print(f"Cleaning {dest_dir}")
        clear_folder(dest_dir)
    else:
        os.mkdir(dest_dir)

    for file in os.listdir(src_dir):
        source_path = f"{src_dir}/{file}"
        dest_path = f"{dest_dir}/{file}.jpg"

        # Keep files larger than 1MB.
        if os.path.isfile(source_path) and (Path(source_path).stat().st_size >> 20) >= 1:
            print(f"Copying {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)

            width, height = get_image_dimensions(dest_path)
            if width < 1920 or height < 1080:
                print(f"Removing {dest_path} as it is smaller than 1920x1080")
                os.remove(dest_path)

    print("Done")

if __name__ == '__main__':
    main()