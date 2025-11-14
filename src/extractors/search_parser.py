thonpython
from .utils_normalize import normalize_text

def parse_search_results(results):
    parsed = []
    for item in results:
        parsed.append({
            "companyName": normalize_text(item.get("companyName")),
            "companyId": item.get("companyId"),
            "rank": item.get("rank", None)
        })
    return parsed