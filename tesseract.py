import pytesseract
from PIL import Image

img_file = "new/bfs1.png"
no_noise = "demoimage.png"

img = Image.open(no_noise)

ocr_result = pytesseract.image_to_string(img)

print (ocr_result)