# Imports 
import sys

from PIL import Image

# List to store images
images = []


# Fetch images from cmd line arguments
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)


# Combine images, set time for changing image, set infinite loop
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)