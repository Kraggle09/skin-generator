from PIL import Image
import random

baseList = ['base0.png']
hairList = ['hair0.png', 'hair1.png']
eyeList = ['eye0.png', 'eye1.png']

def main():
    skin = randomSkin()
    skin.save('skin.png')

def randomSkin():
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    img = overlayAndTint(img, f"assets/{random.choice(baseList)}")
    img = overlayAndTint(img, f"assets/{random.choice(hairList)}", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 100))
    img = overlayAndTint(img, f"assets/{random.choice(eyeList)}", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 100))
    return img

def overlayAndTint(image, overlay_path, tint_color=None):
    overlay = Image.open(overlay_path).convert("RGBA")
    if tint_color:
        a = overlay.split()[3]
        tinted = Image.merge("RGBA", (
            Image.new("L", overlay.size, tint_color[0]),
            Image.new("L", overlay.size, tint_color[1]),
            Image.new("L", overlay.size, tint_color[2]),
            a
        ))
        overlay = tinted
    return Image.alpha_composite(image, overlay)

if __name__ == "__main__":
    main()