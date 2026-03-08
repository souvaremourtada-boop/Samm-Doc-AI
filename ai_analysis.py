import cv2
import pytesseract

def detect_text_regions(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    boxes = []
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            boxes.append((x, y, w, h))
    return boxes
