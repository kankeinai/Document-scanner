from PIL import Image
import pyheif
import sys
import os

my_dir = sys.argv[1]
for pictures in os.listdir(my_dir):
    way = my_dir + "/" + pictures
    if os.path.splitext(pictures)[-1].lower() == ".heic":
        heif_file = pyheif.read(way)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        os.remove(way)
        image.save(os.path.splitext(way)[0] + ".jpg", "JPEG")
