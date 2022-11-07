import os
from PIL import Image

path = r"./"

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if name != "script.py":
            print(os.path.join(root, name))

            im = Image.open(os.path.join(root, name))

            fill_color = (0, 0, 0)

            im = im.convert("RGBA")
            if im.mode in ('RGBA', 'LA'):
                background = Image.new(im.mode[:-1], im.size, fill_color)
                background.paste(im, im.split()[-1])  # omit transparency
                im = background
            result = name.replace(".png", ".jpg")
            os.remove(os.path.join(root, name))

            im.convert("RGB").save(os.path.join(root, result))

print('Tout les fonds des images transparent on été remplacé')
