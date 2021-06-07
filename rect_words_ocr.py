
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D://tesseract/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('test.png') ,lang="chi_sim")
text.encode("gbk")
with open("result.txt", "w") as f:
    f.write(text)

print(text)