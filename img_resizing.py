import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, UnidentifiedImageError

# The number of provided folder names and the number of provided ratios have to match.
FOLDER_NAMES = ["drawable-mdpi", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]
# mdpi(x1), hdpi(x1.5), xhdpi(x2), xxhdpi(x3), xxxhdpi(x4)
# 154x240, 231x360, 308x480, 462x720, 616x960
IMAGE_RATIOS = [0.25, 0.375, 0.5, 0.75, 1]


def select_files():
    root = tk.Tk()
    root.withdraw()
    filetypes = (
        ("All files", "*.*"),
        ("Bitmap files", "*.bmp"),
        ("JPEG files", "*.jpeg *.jpg"),
        ("PNG files", "*.png"),
        ("GIF files", "*.gif")
    )
    cwd = os.getcwd()  # Get current working directory
    filenames = filedialog.askopenfilenames(
        title="Open a file or files",
        initialdir=cwd,
        filetypes=filetypes)
    return filenames


def create_folders():
    if not os.path.exists("output"):
        os.mkdir("output")
    for folder_name in FOLDER_NAMES:
        if not os.path.exists(f"output/{folder_name}"):
            os.mkdir(f"output/{folder_name}")


def resize_files(filenames):
    for filename in filenames:
        try:
            img = Image.open(filename)
        except UnidentifiedImageError:
            print(f"ERROR: Selected file {filename.split('/')[-1]} wasn't identified as image file.")
            continue
        width, height = img.size
        for index, value in enumerate(IMAGE_RATIOS):
            print(value)
            resized_img = img.resize((int(width * value), int(height * value)))
            resized_img.save(f"output/{FOLDER_NAMES[index]}/{filename.split('/')[-1]}")


if __name__ == "__main__":
    if len(FOLDER_NAMES) == len(IMAGE_RATIOS):
        selected_filenames = select_files()
        create_folders()
        resize_files(selected_filenames)
    else:
        print("ERROR: The number of provided folder names doesn't match the number of provided ratios.")
