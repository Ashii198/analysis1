import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Read image from which text needs to be extracted
img = cv2.imread("com_doc.png")
img = cv2.resize(img, (10000, 10000))


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))


cv2.imshow('Result',img)

cv2.waitKey(0)
cv2.destroyAllWindows()