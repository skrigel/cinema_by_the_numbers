import requests
import json
from typing import List, Dict
import requests
import time
from tqdm.notebook import tqdm

MOVIE_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"
MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/"
NOW_PLAYING_URL = "https://api.themoviedb.org/3/movie/now_playing"
GENRE_URL = "https://api.themoviedb.org/3/genre/movie/list"


def get_genres(headers):
    resp = requests.get(GENRE_URL, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data.get("genres", [])


def collect_tmdb_data(movie_ids, output_file_path, checkpoint_every=500, sleep_time=0.35, resume=False):
    """
    Collect TMDB details for a list of movie IDs.
    - checkpoint_every: how often to save to disk (set None to disable)
    - sleep_time: delay between API calls to avoid rate limit
    - resume: if True, load existing 'tmdb_results.csv' and skip already done ones
    """

    # Resume support
    collected = []
    done_ids = set()

    if resume:
        try:
            collected = pd.read_csv(f"{output_file_path}").to_dict("records")
            done_ids = {int(row["id"]) for row in collected if pd.notnull(row["id"])}
            print(f"Resuming from checkpoint: {len(done_ids)} already collected.")
        except FileNotFoundError:
            pass

    session = requests.Session()
    results = collected.copy()
    errors = []

    for idx, mid in enumerate(tqdm(movie_ids, desc="Fetching TMDB data")):
        if mid in done_ids:
            continue

        url = f"{details_url}{int(mid)}"
        retries = 3
        for attempt in range(retries):
            try:
                r = session.get(url, headers=headers, timeout=20)
                if r.status_code == 200:
                    data = r.json()
                    results.append(flatten_movie_data(data))
                    break
                elif r.status_code == 404:
                    errors.append((mid, "404 Not Found"))
                    break
                else:
                    errors.append((mid, f"HTTP {r.status_code}"))
                    break
            except requests.exceptions.RequestException as e:
                if attempt == retries - 1:
                    errors.append((mid, str(e)))
                else:
                    time.sleep(2 ** attempt)
                    continue

        # Rate limit safety
        time.sleep(sleep_time)

        # Save checkpoint
        if checkpoint_every and (idx + 1) % checkpoint_every == 0:
            pd.DataFrame(results).to_csv("tmdb_results.csv", index=False)
            pd.DataFrame(errors, columns=["id", "error"]).to_csv("tmdb_failed.csv", index=False)
            print(f"Checkpoint saved at {idx+1}/{len(movie_ids)}")

    # Final save
    df = pd.DataFrame(results)
    return df

def flatten_movie_data(data: dict) -> dict:
    """Flatten a TMDB movie details JSON object into a flat dict suitable for a dataframe."""

    # handle potential missing keys gracefully
    def safe_get(key, default=None):
        return data.get(key, default)

    return {
        # Core identifiers
        "id": safe_get("id"),
        "imdb_id": safe_get("imdb_id"),
        "title": safe_get("title"),
        "original_title": safe_get("original_title"),
        "original_language": safe_get("original_language"),

        # Release info
        "release_date": safe_get("release_date"),
        "status": safe_get("status"),
        "homepage": safe_get("homepage"),

        # Financials
        "budget": safe_get("budget"),
        "revenue": safe_get("revenue"),

        # Content
        "adult": safe_get("adult"),
        "overview": safe_get("overview"),
        "tagline": safe_get("tagline"),
        "runtime": safe_get("runtime"),

        # Popularity & ratings
        "popularity": safe_get("popularity"),
        "vote_average": safe_get("vote_average"),
        "vote_count": safe_get("vote_count"),

        # Country & language
        "origin_country": ", ".join(safe_get("origin_country", [])),
        "spoken_languages": ", ".join(
            [lang.get("english_name") or lang.get("name", "") for lang in safe_get("spoken_languages", [])]
        ),

        # Genres (split IDs and names)
        "genre_ids": ", ".join([str(g["id"]) for g in safe_get("genres", [])]),
        "genre_names": ", ".join([g["name"] for g in safe_get("genres", [])]),

        # Production companies
        "production_company_ids": ", ".join([str(c["id"]) for c in safe_get("production_companies", [])]),
        "production_company_names": ", ".join([c["name"] for c in safe_get("production_companies", [])]),
        "production_company_countries": ", ".join([c["origin_country"] for c in safe_get("production_companies", [])]),

        # Production countries
        "production_country_codes": ", ".join([c["iso_3166_1"] for c in safe_get("production_countries", [])]),
        "production_country_names": ", ".join([c["name"] for c in safe_get("production_countries", [])]),

        # Extra metadata
        "belongs_to_collection": (
            safe_get("belongs_to_collection", {}).get("name")
            if isinstance(safe_get("belongs_to_collection"), dict)
            else None
        ),
    }


def get_n_most_recent_movies(
    n: int,
    headers: Dict[str, str],
    params: Dict[str, str] = None,
    verbose: bool = False,
) -> List[Dict]:
    collected: List[Dict] = []

    page = 1
    total_pages = None

    while len(collected) < n:

        if verbose:
            print(f"Requesting discover page {page}...")

        if params:
            resp = requests.get(MOVIE_DISCOVER_URL, headers=headers, params=params)
        else:
            resp = requests.get(MOVIE_DISCOVER_URL, headers=headers)

        resp.raise_for_status()
        data = resp.json()

        if total_pages is None:
            total_pages = data.get("total_pages", 1)

        results = data.get("results", [])
        if not results:
            # Nothing more to fetch
            break

        for movie in results:
            if len(collected) >= n:
                break

            movie_id = movie["id"]

            # Fetch full details
            details_resp = requests.get(f"{MOVIE_DETAILS_URL}{movie_id}", headers=headers)
            if details_resp.status_code != 200:
                if verbose:
                    print(f"Skipping movie {movie_id}, status {details_resp.status_code}")
                continue

            details_data = details_resp.json()
            flat = flatten_movie_data(details_data)

            # Optionally keep discover-level fields, like the discover release_date
            flat["discover_release_date"] = movie.get("release_date")
            flat["discover_popularity"] = movie.get("popularity")

            collected.append(flat)

        page += 1
        if total_pages is not None and page > total_pages:
            break  # no more pages

    # Truncate in case we grabbed extra in the last page
    return collected[:n]



def get_movies_from_url(url: str, headers: Dict[str, str], params: Dict[str, str] = None, limit=500, verbose: bool = False) -> List[Dict]:
    collected: List[Dict] = []

    page = 1
    total_pages = None

    while len(collected) < limit:

        if verbose:
            print(f"Requesting now playing page {page}...")

        if params:
            resp = requests.get(NOW_PLAYING_URL, headers=headers, params=params)
        else:
            resp = requests.get(NOW_PLAYING_URL, headers=headers)

        resp.raise_for_status()
        data = resp.json()

        if total_pages is None:
            total_pages = data.get("total_pages", 1)

        results = data.get("results", [])
        if not results:
            # Nothing more to fetch
            break

        for movie in results:

            movie_id = movie["id"]

            # Fetch full details
            details_resp = requests.get(f"{MOVIE_DETAILS_URL}{movie_id}", headers=headers)
            if details_resp.status_code != 200:
                if verbose:
                    print(f"Skipping movie {movie_id}, status {details_resp.status_code}")
                continue

            details_data = details_resp.json()
            flat = flatten_movie_data(details_data)

            # # Optionally keep discover-level fields, like the discover release_date
            # flat["discover_release_date"] = movie.get("release_date")
            # flat["discover_popularity"] = movie.get("popularity")

            collected.append(flat)

        page += 1
        if total_pages is not None and page > total_pages:
            break  # no more pages

    # Truncate in case we grabbed extra in the last page
    return collected[:limit]

def get_movies_out_now(headers: Dict[str, str], params: Dict[str, str] = None, limit=500, verbose: bool = False) -> List[Dict]:
    return get_movies_from_url(NOW_PLAYING_URL, headers, params, limit, verbose)