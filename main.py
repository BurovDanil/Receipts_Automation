import Receipts
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_images(folder):
    data = []
    for file in os.listdir(folder):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder, file)
            text = pytesseract.image_to_string(Image.open(img_path))
            data.append({'file': file, 'text': text})
    return data

extract_text_from_images(Receipts)