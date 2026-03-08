import cv2
import numpy as np
from scipy.fftpack import dct, idct

def embed_watermark(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    dct_image = dct(dct(image.T, norm='ortho').T, norm='ortho')
    dct_image[40:50,40:50] += 5
    watermarked = idct(idct(dct_image.T, norm='ortho').T, norm='ortho')
    watermarked = np.clip(watermarked, 0, 255)
    cv2.imwrite(output_path, watermarked)

embed_watermark("input.jpg", "watermarked.jpg")
