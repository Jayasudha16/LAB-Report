def is_out_of_range(value: float, low: float, high: float) -> bool:
    return not (low <= value <= high)