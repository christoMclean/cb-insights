thonpython
import json
import logging

def export_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Export successful: {path}")
    except Exception as e:
        logging.error(f"Error exporting JSON: {e}")
        raise