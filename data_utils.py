from typing import List
import base64

from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image

import conf


def pdf_to_images(pdf_data) -> list[Image]:
    """ Cuts pages """
    pdf_images = convert_from_bytes(
        pdf_file=pdf_data,
        poppler_path=conf.poppler_path  # TODO: thread_count, grayscale, use_pdftocairo
    )
    return pdf_images


def read_pdf(fpath="1706.03762.pdf"):
    with open(fpath, "rb") as fp:
        file_data = fp.read()
    return file_data


def bytes_to_b64_str(data_b):
    base64_bytes = base64.b64encode(data_b)
    b64_str = base64_bytes.decode("utf8")
    return b64_str