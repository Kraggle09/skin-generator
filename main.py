from PIL import Image
import random

baseList = ['base0.png', 'base1.png']
hairList = ['hair0.png', 'hair1.png']

def main():
    skin = randomSkin()
    skin.save('skin.png')

def randomSkin():
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    img = overlay(img, f"assets/{random.choice(baseList)}")
    img = overlay(img, f"assets/{random.choice(hairList)}")
    return img

def overlay(image, overlay):
    return Image.alpha_composite(image, Image.open(overlay))

if __name__ == "__main__":
    main()