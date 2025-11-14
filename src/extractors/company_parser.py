thonpython
from .utils_normalize import normalize_text

def parse_company_data(data):
    return {
        "companyName": normalize_text(data.get("companyName")),
        "companyId": data.get("companyId"),
        "description": normalize_text(data.get("description")),
        "industry": normalize_text(data.get("industry")),
        "similarCompanies": [
            normalize_text(x) for x in data.get("similarCompanies", [])
        ],
        "rawData": data
    }