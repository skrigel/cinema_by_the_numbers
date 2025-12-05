# Choice Model Output for Optimization Model
# Generated from choice_modeling.ipynb
#
# ⚠️ CRITICAL: ALL movie IDs are INTEGERS (not strings)
# - demand keys: (int, str) tuples, e.g., (266, "Mon")
# - runtimes keys: int, e.g., 266
# - movie_ids: list of int, e.g., [978, 3664, ...]
# - genre_to_movies values: lists of int, e.g., [978, 3488, ...]
#
# DO NOT convert these to strings - they must remain integers!
# The optimization model expects integer IDs to match the demand dictionary keys.
#
# ⚠️ IMPORTANT: If loading from JSON in optimization notebook:
#   Use: demand = load_demand_from_json('path/to/choice_model_demand.json')
#   OR: demand = {(int(k.split('_')[0]), k.split('_')[1]): v for k, v in json.load(f).items()}
#   NOT: demand = {tuple(k.split('_')): v for k, v in json.load(f).items()}  # This creates string IDs!
#
# ⚠️ IMPORTANT: If loading movie_ids from CSV:
#   Use: movie_ids = metadata['movie_id'].astype(int).tolist()  # Keep as integers!
#   NOT: movie_ids = metadata['movie_id'].astype(str).tolist()  # This causes KeyError!

demand = {
    (266, "Fri"): 26,
    (266, "Mon"): 16,
    (266, "Sat"): 32,
    (266, "Sun"): 32,
    (266, "Thu"): 20,
    (266, "Tue"): 16,
    (266, "Wed"): 18,
    (471, "Fri"): 30,
    (471, "Mon"): 18,
    (471, "Sat"): 37,
    (471, "Sun"): 37,
    (471, "Thu"): 23,
    (471, "Tue"): 18,
    (471, "Wed"): 21,
    (978, "Fri"): 1073,
    (978, "Mon"): 660,
    (978, "Sat"): 1320,
    (978, "Sun"): 1320,
    (978, "Thu"): 825,
    (978, "Tue"): 660,
    (978, "Wed"): 742,
    (1292, "Fri"): 14,
    (1292, "Mon"): 8,
    (1292, "Sat"): 17,
    (1292, "Sun"): 17,
    (1292, "Thu"): 10,
    (1292, "Tue"): 8,
    (1292, "Wed"): 9,
    (1751, "Fri"): 28,
    (1751, "Mon"): 17,
    (1751, "Sat"): 34,
    (1751, "Sun"): 34,
    (1751, "Thu"): 21,
    (1751, "Tue"): 17,
    (1751, "Wed"): 19,
    (1793, "Fri"): 38,
    (1793, "Mon"): 23,
    (1793, "Sat"): 47,
    (1793, "Sun"): 47,
    (1793, "Thu"): 29,
    (1793, "Tue"): 23,
    (1793, "Wed"): 26,
    (2464, "Fri"): 48,
    (2464, "Mon"): 29,
    (2464, "Sat"): 59,
    (2464, "Sun"): 59,
    (2464, "Thu"): 37,
    (2464, "Tue"): 29,
    (2464, "Wed"): 33,
    (2486, "Fri"): 46,
    (2486, "Mon"): 28,
    (2486, "Sat"): 57,
    (2486, "Sun"): 57,
    (2486, "Thu"): 36,
    (2486, "Tue"): 28,
    (2486, "Wed"): 32,
    (2552, "Fri"): 35,
    (2552, "Mon"): 21,
    (2552, "Sat"): 43,
    (2552, "Sun"): 43,
    (2552, "Thu"): 27,
    (2552, "Tue"): 21,
    (2552, "Wed"): 24,
    (2686, "Fri"): 17,
    (2686, "Mon"): 10,
    (2686, "Sat"): 21,
    (2686, "Sun"): 21,
    (2686, "Thu"): 13,
    (2686, "Tue"): 10,
    (2686, "Wed"): 12,
    (2799, "Fri"): 43,
    (2799, "Mon"): 26,
    (2799, "Sat"): 53,
    (2799, "Sun"): 53,
    (2799, "Thu"): 33,
    (2799, "Tue"): 26,
    (2799, "Wed"): 29,
    (2876, "Fri"): 48,
    (2876, "Mon"): 29,
    (2876, "Sat"): 59,
    (2876, "Sun"): 59,
    (2876, "Thu"): 37,
    (2876, "Tue"): 29,
    (2876, "Wed"): 33,
    (3488, "Fri"): 101,
    (3488, "Mon"): 62,
    (3488, "Sat"): 124,
    (3488, "Sun"): 124,
    (3488, "Thu"): 78,
    (3488, "Tue"): 62,
    (3488, "Wed"): 70,
    (3664, "Fri"): 137,
    (3664, "Mon"): 84,
    (3664, "Sat"): 168,
    (3664, "Sun"): 168,
    (3664, "Thu"): 105,
    (3664, "Tue"): 84,
    (3664, "Wed"): 94,
    (3903, "Fri"): 30,
    (3903, "Mon"): 18,
    (3903, "Sat"): 37,
    (3903, "Sun"): 37,
    (3903, "Thu"): 23,
    (3903, "Tue"): 18,
    (3903, "Wed"): 21,
}

runtimes = {
    266: 12,
    471: 114,
    978: 98,
    1292: 73,
    1751: 120,
    1793: 97,
    2464: 84,
    2486: 116,
    2552: 126,
    2686: 91,
    2799: 111,
    2876: 92,
    3488: 110,
    3664: 93,
    3903: 120,
}

movie_ids = [978, 3664, 3488, 2464, 2876, 2486, 2799, 1793, 2552, 471, 3903, 1751, 266, 2686, 1292]

genre_to_movies = {
    'action': [],
    'adventure': [2876],
    'animation': [2876, 266],
    'comedy': [2464, 2876, 2552],
    'crime': [3488, 2552],
    'documentary': [3664, 1292],
    'drama': [978, 3488, 2486, 2799, 1793, 2552, 3903, 1751],
    'family': [2876],
    'fantasy': [],
    'history': [3903],
    'horror': [471, 2686],
    'music': [],
    'mystery': [2686],
    'romance': [2486],
    'science_fiction': [],
    'thriller': [471, 3903, 2686],
    'tv_movie': [],
    'war': [],
    'western': [],
}

genre_columns = ['action', 'adventure', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'history', 'horror', 'music', 'mystery', 'romance', 'science_fiction', 'thriller', 'tv_movie', 'war', 'western']

# Validation: Ensure all IDs are integers and consistent
assert all(isinstance(mid, int) for mid in movie_ids), "movie_ids must be integers"
assert all(isinstance(k[0], int) for k in demand.keys()), "demand keys must have integer movie IDs"
assert all(isinstance(k, int) for k in runtimes.keys()), "runtimes keys must be integers"
assert all(isinstance(mid, int) for genre_list in genre_to_movies.values() for mid in genre_list), "genre_to_movies must contain integer IDs"
# CRITICAL: Ensure all genre_to_movies IDs are in movie_ids (prevents KeyError in optimization)
movie_ids_set = set(movie_ids)
all_genre_ids = set()
for movie_list in genre_to_movies.values():
    all_genre_ids.update(movie_list)
invalid_genre_ids = all_genre_ids - movie_ids_set
assert len(invalid_genre_ids) == 0, f"CRITICAL: genre_to_movies contains IDs not in movie_ids: {invalid_genre_ids}"
print("✓ All movie IDs validated as integers and consistent")

# Helper function to load demand from JSON with integer movie IDs
def load_demand_from_json(json_path):
    """
    Load demand dictionary from JSON file with integer movie IDs.
    
    Args:
        json_path: Path to choice_model_demand.json
    
    Returns:
        dict: Demand dictionary with (int, str) tuple keys
    """
    import json
    with open(json_path, 'r') as f:
        demand_json = json.load(f)
    # Convert string keys to tuple keys with INTEGER movie IDs
    # Format: "2876_Mon" -> (2876, "Mon") not ('2876', 'Mon')
    return {(int(k.split('_')[0]), k.split('_')[1]): int(v) for k, v in demand_json.items()}
