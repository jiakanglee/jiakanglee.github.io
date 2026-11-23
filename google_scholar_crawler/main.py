from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def fetch_author(scholar_id, api_key):
    query = urlencode({
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "hl": "en",
        "api_key": api_key,
    })
    print("Requesting the Google Scholar author profile from SerpApi.", flush=True)
    try:
        with urlopen(f"https://serpapi.com/search.json?{query}", timeout=30) as response:
            data = json.load(response)
    except HTTPError as exc:
        raise SystemExit(f"SerpApi returned HTTP {exc.code}. Check the API key and quota.") from None
    except (URLError, TimeoutError):
        raise SystemExit("The SerpApi request timed out or could not connect.") from None
    if data.get("error") or data.get("search_metadata", {}).get("status") != "Success":
        raise ValueError("SerpApi did not return a successful search.")
    if data.get("search_parameters", {}).get("author_id") != scholar_id:
        raise ValueError("SerpApi returned a different author ID.")
    return data


def count(value):
    if type(value) is int and value >= 0:
        return value
    if isinstance(value, str) and re.fullmatch(r"[0-9]+", value):
        return int(value)
    raise ValueError("Expected a nonnegative citation metric.")


def update_profile(previous, result, scholar_id):
    if previous and previous.get("scholar_id") != scholar_id:
        raise ValueError("The saved profile belongs to a different author.")
    author = result["author"]
    if not isinstance(author.get("name"), str) or not author["name"].strip():
        raise ValueError("The response has no author name.")
    profile = dict(previous)
    profile.update(container_type="Author", source="AUTHOR_PROFILE_PAGE",
                   scholar_id=scholar_id, name=author["name"],
                   filled=["basics", "indices", "counts"])
    profile.pop("warning", None)
    profile.pop("errors", None)
    for source, target in (("affiliations", "affiliation"), ("thumbnail", "url_picture")):
        if author.get(source):
            profile[target] = author[source]
    if "interests" in author:
        profile["interests"] = [item["title"] for item in author["interests"]]

    cited_by = result["cited_by"]
    metrics = {key: values for row in cited_by["table"] for key, values in row.items()}
    fields = {"citations": "citedby", "h_index": "hindex", "i10_index": "i10index"}
    for api_name, saved_name in fields.items():
        values = metrics[api_name]
        recent = [key for key in values if re.fullmatch(r"since_[0-9]{4}", key)]
        if len(recent) != 1:
            raise ValueError(f"Missing or ambiguous recent period for {api_name}.")
        profile[saved_name] = count(values["all"])
        profile[saved_name + "5y"] = count(values[recent[0]])
    profile["cites_per_year"] = {
        str(count(row["year"])): count(row["citations"]) for row in cited_by["graph"]
    }
    profile["updated"] = datetime.now(timezone.utc).isoformat()
    return profile


def main():
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    api_key = os.environ.get("SERPAPI_KEY", "").strip()
    if not api_key:
        raise SystemExit("Add SERPAPI_KEY to the repository's Actions secrets.")
    default_dir = Path(__file__).resolve().parent / "results"
    directory = Path(os.environ.get("SCHOLAR_STATS_DIR", default_dir))
    profile_path = directory / "gs_data.json"
    previous = json.loads(profile_path.read_text(encoding="utf-8")) if profile_path.exists() else {}
    result = fetch_author(scholar_id, api_key)
    try:
        profile = update_profile(previous, result, scholar_id)
    except (KeyError, TypeError, ValueError) as exc:
        raise SystemExit(f"Incomplete Scholar data. The saved snapshot was kept. {exc}") from None

    badge = {"schemaVersion": 1, "label": "citations",
             "message": str(profile["citedby"]), "color": "4285F4"}
    directory.mkdir(parents=True, exist_ok=True)
    for name, data in (("gs_data.json", profile), ("gs_data_shieldsio.json", badge)):
        (directory / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                                      encoding="utf-8")
    print(f"Google Scholar citations: {profile['citedby']}")


if __name__ == "__main__":
    main()
