import re
from app.models.schemas import LabTest
from app.utils.helpers import is_out_of_range

def parse_lab_tests(text: str):
    results = []
    lines = text.split("\n")

    for line in lines:
        match = re.match(r"(.+?)\s+([\d.]+)\s+(\d+\.?\d*-\d+\.?\d*)", line)
        if match:
            name, value, ref_range = match.groups()
            value = float(value)
            low, high = map(float, ref_range.split('-'))
            unit_match = re.search(r'\((.*?)\)', name)
            unit = unit_match.group(1) if unit_match else ""

            results.append(LabTest(
                test_name=name.strip(),
                test_value=str(value),
                bio_reference_range=ref_range,
                test_unit=unit,
                lab_test_out_of_range=is_out_of_range(value, low, high)
            ))
    return results