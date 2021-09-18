import logging

import cv2
import numpy as np
import pytesseract

from .config import NUMBER_OCR_CONFIG


def new_number(image_data: bytes) -> str:
    image = cv2.imdecode(np.asarray(bytearray(image_data), dtype=np.uint8), cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    result = pytesseract.image_to_string(image, lang='eng', config=NUMBER_OCR_CONFIG).strip()
    logging.debug(f"number ocr {result}")
    return result
