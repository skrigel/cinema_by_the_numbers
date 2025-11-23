import requests
import json
from typing import List, Dict
import requests
import time
import os
from tqdm.notebook import tqdm


def make_params(movie_id):
    return {
        "i": movie_id
    }

def make_url(api_key):
    return f"http://www.omdbapi.com/?apikey={api_key}"


def query_omdb(movie_id: int, api_key: str, verbose: bool = False) -> List[Dict]:

    if verbose:
        print(f"Requesting movie {movie_id}...")
        print(f"URL: {make_url(api_key)}")

    params = make_params(movie_id)

    try:
        resp = requests.get(make_url(api_key), params=params)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        if verbose:
            print(f"Request failed for movie {movie_id}: {e}")
        return None
    if resp.status_code != 200:
        if verbose:
            print(f"Failed to retrieve movie {movie_id}, status {resp.status_code}")
        return None
    data = resp.json()

    data = flatten_omdb_movie(data)
    return data
    
    

def flatten_omdb_movie(movie_json: dict) -> dict:
    """
    Flatten an OMDB-style movie response into a single flat dict.
    Expands the Ratings array into separate fields.
    """
    flat = {}

    # Copy all top-level non-list fields directly
    for key, value in movie_json.items():
        if key != "Ratings":
            flat[key] = value

    # Expand Ratings list
    ratings = movie_json.get("Ratings", [])
    for rating in ratings:
        source = rating.get("Source")
        value = rating.get("Value")
        if source:
            # Create a clean key name, e.g. "Rating_IMDB", "Rating_RottenTomatoes"
            clean_key = (
                "Rating_" + source.replace(" ", "").replace("(", "").replace(")", "")
            )
            flat[clean_key] = value

    return flat

def get_movies_from_ids(api_key: str, movie_ids: List[str], limit=1000, verbose: bool = False) -> List[Dict]:
    """
    Fetch movies by their IDs.
    
    Args:
        api_key: OMDB API key
        movie_ids: List of movie IDs to fetch
        limit: Maximum number of movies to collect
        verbose: Whether to print progress messages
        headers: HTTP headers for the request
        params: Additional query parameters
        limit: Maximum number of movies to collect
        verbose: Whether to print progress messages
    
    Returns:
        List of movie dictionaries
    """
    collected: List[Dict] = []

    i = 0
    while i < len(movie_ids) and i < limit:

        if verbose:
            print(f"Requesting movie {i}...")

        data = query_omdb(movie_ids[i], api_key)

        if data is None:
            print(f"Failed to retrieve movie {movie_ids[i]}")
            i += 1
            continue

        collected.append(data)
        i+=1

    return collected

