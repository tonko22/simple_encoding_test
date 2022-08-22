import requests
import json
import base64
from time import time
from statistics import mean
from pdf2image import convert_from_path, convert_from_bytes
import sys
from PIL import Image
import numpy as np

url = "127.0.0.1:9001"


def read_pdf():
    with open("1706.03762.pdf", "rb") as fp:
        file_data = fp.read()
    return file_data


def bytes_to_b64_str(data_b):
    base64_bytes = base64.b64encode(data_b)
    b64_str = base64_bytes.decode("utf8")
    return b64_str


# 1 Multipart-form data
def send_post_multipart_form(file_data, ascii=True):
    url = "http://192.168.112.1:5011/search_query"
    base64_bytes = base64.b64encode(file_data)
    if ascii:
        coding = "ascii"
    else:
        coding = 'utf-8'
    b64_str = base64_bytes.decode(coding)
    # json_string = json.dumps(file_data)
    # resp = requests.post(url=url, json=json_string)
    return b64_str


def pdf_to_json():
    pdf_data = read_pdf()
    base64_bytes = base64.b64encode(pdf_data)
    # print("base64_bytes", base64_bytes)
    # print(type(base64_bytes))  # displays as utf-8, but actually bytes
    b64_str = base64_bytes.decode('utf-8')
    json_string = json.dumps({"data_b64_str": b64_str})
    return json_string


def pdf_to_numpy():
    pdf_data = read_pdf()
    base64_bytes = base64.b64encode(pdf_data)
    b64_str = base64_bytes.decode('utf-8')
    json_string = json.dumps({"data_b64_str": b64_str})
    return json_string


def pdf_images_to_numpy_list(pdf_data):
    base64_bytes = base64.b64encode(pdf_data)
    b64_str = base64_bytes.decode('utf-8')
    json_string = json.dumps({"data_b64_str": b64_str})
    return json_string

# 2 Base64 pdf-bytes

# 3 Base64 numpy-array bytes

# 4 Pickle-string
def compare_ascii_vs_utf8(n_experiments=1000):
    file_data = read_pdf()
    times = []
    for i in range(n_experiments):
        start = time()
        json_string = send_post_multipart_form(file_data=file_data, ascii=True)
        end = time()
        elapsed_time = end - start
        times.append(elapsed_time)

    print("ascii:")
    print(mean(times))

    times = []
    for i in range(n_experiments):
        start = time()
        json_string = send_post_multipart_form(file_data=file_data, ascii=False)
        end = time()
        elapsed_time = end - start
        times.append(elapsed_time)

    print("utf-8:")
    print(mean(times))


def pdf_to_images(pdf_data):
    pdf_images = convert_from_bytes(
        pdf_file=pdf_data,
        poppler_path="C:/Users/tonko22/Downloads/Release-22.04.0-0/poppler-22.04.0/Library/bin")
    return pdf_images


def images_to_lists(images):
    list_of_lists = []
    for image in images:
        image.to
    return list_of_lists


# Best way is probably RLE + protobuf
# also https://openbase.com/python/numproto
if __name__ == "__main__":
    pdf_data = read_pdf()
    # compare_ascii_vs_utf8(n_experiments=1000)
    # compare_sizes()
    start = time()
    images = pdf_to_images(pdf_data)
    end = time()
    elapsed = end - start
    print(f"pdf_to_images: {elapsed}")

    np_arrays = []
    for image in images:
        np_arrays.append(np.array(image))

    start = time()
    lists_of_ints = []
    for np_arr in np_arrays:
        lists_of_ints.append(np_arr.tolist())

    end = time()
    elapsed = end - start
    json_string = json.dumps({"np_list_str": lists_of_ints})
    print(type(json_string))
    print(f"numpy to list: {elapsed}, size: {sys.getsizeof(json_string)}")

    start = time()
    lists_of_ints = []
    for np_arr in np_arrays:
        b64_numpy_image_str = bytes_to_b64_str(np_arr.tobytes())
        lists_of_ints.append(b64_numpy_image_str)

    end = time()
    elapsed = end - start
    json_string = json.dumps({"np_b64_str": lists_of_ints})
    print(type(json_string))
    print(f"numpy to b64: {elapsed}, size: {sys.getsizeof(json_string)}")
