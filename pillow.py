from PIL import Image

im_file ="demoimage.png"

im = Image.open(im_file)
print (im.size)
im.show()

im.save("demoimage.png")
