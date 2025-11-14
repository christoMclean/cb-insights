thonpython
def normalize_text(value):
    if not isinstance(value, str):
        return value
    return " ".join(value.strip().split())