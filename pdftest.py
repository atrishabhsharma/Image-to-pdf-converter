from PIL import Image
import os

file = "F:\id.jpg"
im = Image.open(file)
if im.mode =="RGBA":
    im= im.convert("RGB")

new_file="F:\id.pdf"
##if the file doesnt exist then it will create one and you dont need to overwrite it
if not os.path.exists(new_file):
    im.save(new_file,"PDF",resolution=100.0)

