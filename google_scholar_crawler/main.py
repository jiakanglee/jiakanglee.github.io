from datetime import datetime, timezone
import json
import os
from pathlib import Path
from urllib.request import urlopen

from fp.fp import FreeProxy
from scholarly import ProxyGenerator, scholarly


RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

BAD_FALLBACK_VALUES = {"", "updating", "unavailable", "temporarily unavailable"}


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
        message = str(data.get("message", "")).strip()
        if message.lower() not in BAD_FALLBACK_VALUES:
            return message
    except Exception as exc:
        print(f"Could not read previous badge value: {exc}")
    return "unavailable"


def fetch_author(scholar_id: str) -> dict:
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts"])
    return author


def fetch_with_free_proxy(scholar_id: str, attempt: int) -> dict:
    # free-proxy checks candidate proxies before returning one. We then hand the
    # selected proxy to scholarly instead of using scholarly.FreeProxies(),
    # avoiding version/API incompatibilities between scholarly and free-proxy.
    proxy_url = FreeProxy(
        https=True,
        rand=True,
        timeout=2.0,
        request_timeout=8,
    ).get()
    print(f"Free proxy attempt {attempt}: candidate acquired")

    proxy = ProxyGenerator()
    if not proxy.SingleProxy(http=proxy_url, https=proxy_url):
        raise RuntimeError("scholarly rejected the selected free proxy")

    scholarly.use_proxy(proxy)
    return fetch_author(scholar_id)


def main() -> None:
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    errors = []
    author = None

    # First try the GitHub runner directly. It occasionally works and is faster
    # than using a public proxy.
    try:
        print("Trying Google Scholar directly...")
        author = fetch_author(scholar_id)
    except Exception as exc:
        errors.append(f"direct: {type(exc).__name__}: {exc}")
        print(f"Direct request failed: {exc}")

    # Fall back to several independently selected free proxies.
    if author is None:
        for attempt in range(1, 5):
            try:
                author = fetch_with_free_proxy(scholar_id, attempt)
                break
            except Exception as exc:
                errors.append(f"proxy {attempt}: {type(exc).__name__}: {exc}")
                print(f"Free proxy attempt {attempt} failed: {exc}")

    if author is not None:
        author["updated"] = datetime.now(timezone.utc).isoformat()
        citation_count = str(author["citedby"])
        write_results(author, citation_count)
        print(f"Google Scholar citations: {citation_count}")
        return

    # All attempts failed. Keep the last known good citation value so the
    # homepage badge never becomes a broken resource or causes the workflow to
    # fail merely because Google Scholar blocked today's requests.
    previous = previous_badge_message()
    fallback = {
        "scholar_id": scholar_id,
        "updated": datetime.now(timezone.utc).isoformat(),
        "warning": "All Google Scholar fetch attempts failed; retained last known badge value.",
        "errors": errors,
    }
    write_results(fallback, previous)
    print("All Google Scholar attempts failed.")
    print(f"Keeping previous citation badge value: {previous}")


if __name__ == "__main__":
    main()
