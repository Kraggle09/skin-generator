from PIL import Image
import random
import os

baseList = ['base0']
hairList = ['hair0', 'hair1']
eyeList = ['eye1']

def main():
    skin = randomSkin()
    skin.save('skin.png')

def randomSkin():
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    img = overlay(img, random.choice(baseList), False)
    img = overlay(img, random.choice(eyeList))
    img = overlay(img, random.choice(hairList))
    return img

def tint(image, color=(255, 255, 255, 255)):
    layer_image = Image.open(f"assets/{image}.png")
    tint_layer = Image.new("RGBA", (64, 64), color)
    if os.path.exists(f"assets/{image}_mask.png"):
        mask = Image.open(f"assets/{image}_mask.png").convert("L")
        return Image.composite(tint_layer, layer_image, mask)
    else:
        r, g, b, a = layer_image.split()
        base_rgb = Image.merge("RGB", (r, g, b))
        tint_rgb = Image.new("RGB", layer_image.size, color[:3])
        blended_rgb = Image.blend(base_rgb, tint_rgb, color[3] / 255.0)
        return Image.merge("RGBA", (*blended_rgb.split(), a))

def overlay(base, layer, should_tint=True):
    if should_tint:
        return Image.alpha_composite(base, tint(layer, random_color(225)))
    else:
        return Image.alpha_composite(base, Image.open(f"assets/{layer}.png"))

def random_color(alpha):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha)

if __name__ == "__main__":
    main()