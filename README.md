# Extracting-text-from-images-with-Tesseract-OCR
Tesseract OCR using Python for Extracting text from images

Overview

extracting text from image using Tesseract ocr
image can be like
-screenshot
-printed page photo
-scanned image
-camera capture image
-window or any other application error message popup screenshot
etc (NOTE:input image should not blurry or noisy)
for recognize or read text you need to follow these steps
-first you should have knowledge of python if not then you need to first watch our video “Python install and helloworld program Tutorial” url : https://youtu.be/oTEf-fij-9g

-download and install tesseract Ocr Library
https://github.com/UB-Mannheim/tesseract/wiki

and add tesseract installation dir path into Environment variables } PATH } New

or use below line on start of your script
pytesseract.pytesseract.tesseract_cmd = r”C:\Program Files (x86)\Tesseract-OCR\tesseract.exe”

then install 2 python libraries
pip install pytesseract
&
pip install pillow

*************Example Code (example.py)**************
 from PIL import Image

import pytesseract

#uncomment below line if you dont want to set "Environment variables" path
 #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

im = Image.open("sample1.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)

******************************************

Summary

To using Tesseract ocr we can extract text from image like screenshot,printed page photo,scanned image,camera capture image,error message screenshot etc


for more detail go to https://hzonesp.com/programming/recognize-read-text-image-python-window/
go step by step video https://www.youtube.com/watch?v=3QISfjLdS8U
