from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import LabTestResponse
from app.ocr.processor import extract_text_from_image
from app.parser.lab_parser import parse_lab_tests
from fastapi import UploadFile, File
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/get-lab-tests", response_model=LabTestResponse)
async def get_lab_tests(file: UploadFile = File(...)):
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        ocr_text = extract_text_from_image(temp_file_path)
        parsed_data = parse_lab_tests(ocr_text)
        return {"is_success": True, "data": parsed_data}
    finally:
        os.remove(temp_file_path)
