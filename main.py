#! /home/olalekan/Projects/odoo-projects/lorin_qr_code/env/bin/python
import io
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from decouple import config


def extract_images_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    images = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        images.append(img)
    return images


def main(pdf_path):
    images = extract_images_from_pdf(pdf_path)
    text = pytesseract.image_to_string(images[-1])
    return text


if __name__ == "__main__":
    pdf_path = config('PDF_PATH')
    print(main(pdf_path))
