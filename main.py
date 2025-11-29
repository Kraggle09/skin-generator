from PIL import Image
import random
import json

baseList = ['base0']
hairList = ['hair0', 'hair1']
eyeList = ['eye0', 'eye1']

def main():
    skin = randomSkin()
    skin.save('skin.png')

def randomSkin():
    img = Image.open(f"assets/{random.choice(baseList)}.png")
    img = overlay(img, random.choice(eyeList))
    return img

def tint(image, coordinate, color=(255, 255, 255, 255)):
    overlay = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    overlay.putpixel(coordinate, color)
    return Image.alpha_composite(image, overlay)

def overlay(base, layer):
    with open(f"assets/{layer}.json") as file:
        metadata = json.load(file)
    layer_image = Image.open(f"assets/{layer}.png")
    tint_color = random_color(200)
    for coord in metadata['coordinates']:
        layer_image = tint(layer_image, coord, tint_color)
    return Image.alpha_composite(base, layer_image)

def random_color(alpha):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha)

if __name__ == "__main__":
    main()