from PIL import Image

import pytesseract
import os



#uncomment below line if you dont want to set "Environment variables" path
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" 


im = Image.open("Screenshot_66.png")


text = pytesseract.image_to_string(im, lang = 'eng')


print(text)

os.system('pause')