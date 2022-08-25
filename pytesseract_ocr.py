from PIL import Image
import pytesseract

from data_utils import read_pdf, pdf_to_images

# Add "C:\Users\USER\AppData\Local\Tesseract-OCR" to PATH

def benchmark_ocr():
    pass


def run_ocr(image_fp, custom_config=True):
    """
    This function will handle the core OCR processing of images.
    """
    if custom_config:
        text = pytesseract.image_to_string(image_fp, lang='eng',
                                           config=r'--oem 3 --psm 6')
    else:
        text = pytesseract.image_to_string(image_fp, lang='eng')
    return text


if __name__ == '__main__':
    # Test
    pdf_data = read_pdf()
    pdf_images = pdf_to_images(pdf_data)

    # lang='eng'
    # "OMP_THREAD_LIMIT"
    #  TODO: https://indiantechwarrior.com/how-to-install-tesseract-on-windows/
    print(pytesseract.get_languages(config=''))
    for image in pdf_images:
        text = run_ocr(image)
        print(text)
