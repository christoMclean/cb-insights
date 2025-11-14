thonpython
import json
import logging
from extractors.search_parser import parse_search_results
from extractors.company_parser import parse_company_data
from extractors.insights_parser import parse_insights
from outputs.exporters import export_json

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Loading sample input data...")
    try:
        with open("data/sample.json", "r", encoding="utf-8") as f:
            raw = json.load(f)
    except Exception as e:
        logging.error(f"Error reading data/sample.json: {e}")
        return

    logging.info("Parsing search results...")
    search = parse_search_results(raw.get("searchResults", []))

    logging.info("Parsing company data...")
    company = parse_company_data(raw.get("companyData", {}))

    logging.info("Parsing insights...")
    insights = parse_insights(raw.get("insights", []))

    final = {
        "search": search,
        "company": company,
        "insights": insights
    }

    logging.info("Exporting output...")
    export_json("data/output.json", final)

    logging.info("Done. Output saved to data/output.json")

if __name__ == "__main__":
    main()