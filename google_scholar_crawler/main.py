from datetime import datetime, timezone
import json
import os
from pathlib import Path
from urllib.request import urlopen

from scholarly import ProxyGenerator, scholarly
from scholarly._proxy_generator import MaxTriesExceededException


RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def write_results(author: dict, message: str) -> None:
    with (RESULTS_DIR / "gs_data.json").open("w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shield_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(message),
        "color": "4285F4",
    }
    with (RESULTS_DIR / "gs_data_shieldsio.json").open("w", encoding="utf-8") as outfile:
        json.dump(shield_data, outfile, ensure_ascii=False)


def previous_badge_message() -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "jiakanglee/jiakanglee.github.io")
    url = (
        f"https://raw.githubusercontent.com/{repo}/"
        "google-scholar-stats/gs_data_shieldsio.json"
    )
    try:
        with urlopen(url, timeout=15) as response:
            data = json.load(response)
        return str(data.get("message", "temporarily unavailable"))
    except Exception:
        return "temporarily unavailable"


def main() -> None:
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]

    scraper_api_key = os.environ.get("SCRAPERAPI_KEY", "").strip()
    if scraper_api_key:
        proxy = ProxyGenerator()
        if proxy.ScraperAPI(scraper_api_key):
            scholarly.use_proxy(proxy)

    try:
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=["basics", "indices", "counts"])
        author["updated"] = datetime.now(timezone.utc).isoformat()
        citation_count = str(author["citedby"])
        write_results(author, citation_count)
        print(f"Google Scholar citations: {citation_count}")
    except MaxTriesExceededException as exc:
        # Google Scholar frequently blocks shared GitHub-hosted runner IPs.
        # Keep the last published badge value instead of failing the workflow.
        message = previous_badge_message()
        fallback = {
            "scholar_id": scholar_id,
            "updated": datetime.now(timezone.utc).isoformat(),
            "warning": "Google Scholar blocked the GitHub-hosted runner.",
        }
        write_results(fallback, message)
        print(f"Warning: {exc}")
        print(f"Keeping previous citation badge value: {message}")


if __name__ == "__main__":
    main()
