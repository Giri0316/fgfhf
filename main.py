# Install required libraries
# pip install pytesseract pillow

from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'tesseract-main'

def ocr(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

# Example usage
image_path = "a.png"
ocr(image_path)
