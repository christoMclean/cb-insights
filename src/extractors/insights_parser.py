thonpython
from .utils_normalize import normalize_text

def parse_insights(insights):
    return [
        {
            "title": normalize_text(insight.get("title")),
            "content": normalize_text(insight.get("content"))
        }
        for insight in insights
    ]