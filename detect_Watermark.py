import cv2
import numpy as np
from scipy.fftpack import dct

def detect_watermark(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    dct_image = dct(dct(image.T, norm='ortho').T, norm='ortho')
    score = np.mean(dct_image[40:50,40:50])
    if score > 3:
        print("Watermark detected")
    else:
        print("No watermark")

detect_watermark("watermarked.jpg")
