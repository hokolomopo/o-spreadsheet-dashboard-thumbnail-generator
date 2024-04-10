import os
from PIL import Image

folder = "dashboard thumbnails"
out_folder = "out"

def thumnailize_image(infile, outfile):
    app = infile.split()[0] if " " in infile else infile.split(".")[0]
    app_icon = Image.open(os.path.join("app_icons", app + ".png"))
    app_icon = app_icon.resize((24, 24))
    round_box = Image.open("round_box.png")
    round_box.paste(app_icon, (4, 4), app_icon)
    app_icon = round_box

    img = Image.open(os.path.join(folder, file))
    width, height = img.size
    min_size = min(width, height)
    area = (0, 0, min_size, min_size)
    img = img.crop(area)
    size = (128, 128)
    img.thumbnail(size)

    img.paste(app_icon, (92, 92), app_icon)

    img.save(outfile, format="jpeg")


for file in os.listdir(folder):
    print(file)
    pre, ext = os.path.splitext(file)
    outfile = pre.lower()
    outfile = outfile if len(outfile.split()) == 1 else " ".join(outfile.split()[1:])
    outfile = outfile.replace(" ", "_")
    outfile = outfile + "_dashboard_thumbnail.jpg"
    outfile = os.path.join(out_folder, outfile)
    thumnailize_image(file, outfile)
