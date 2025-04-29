from app.ocr.processor import extract_text_from_image

print("OCR test starting...")

image_path = "lab_reports_samples/AHD-0425-PA-0007561_JITENDRA TRIVEDI DS_28-04-2025_1019-21_AM.pdf_page_9.png"  # <-- Replace with real image
text = extract_text_from_image(image_path)

print("Extracted text:\n")
print(text or "[No text detected]")