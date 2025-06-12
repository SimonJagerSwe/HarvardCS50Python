from PIL import Image
from PIL import ImageFilter

def main():
    # img = Image.open("shirt.png")
    # img.close()
    with Image.open("shirt.png") as img:
        # print(img.size)
        # print(img.format)
        # img = img.rotate(180)
        # img.save("upside_down_shirt.png")
        img = img.filter(ImageFilter.BLUR)
        img.save("blurry_shirt.png")

        
main()