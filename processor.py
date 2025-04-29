from PIL import Image
import pytesseract

def extract_text_from_image(image_path: str) -> str:
    """
    Reads an image from the given path and extracts text using Tesseract OCR.

    Args:
        image_path (str): Path to the input image.

    Returns:
        str: Extracted text from the image.
    """
    try:
        # Open the image using PIL
        img = Image.open(image_path)
        
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""
