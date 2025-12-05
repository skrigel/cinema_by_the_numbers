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
    (266, "Fri"): 34,
    (266, "Mon"): 21,
    (266, "Sat"): 42,
    (266, "Sun"): 42,
    (266, "Thu"): 26,
    (266, "Tue"): 21,
    (266, "Wed"): 23,
    (471, "Fri"): 9,
    (471, "Mon"): 5,
    (471, "Sat"): 11,
    (471, "Sun"): 11,
    (471, "Thu"): 7,
    (471, "Tue"): 5,
    (471, "Wed"): 6,
    (978, "Fri"): 2198,
    (978, "Mon"): 1352,
    (978, "Sat"): 2705,
    (978, "Sun"): 2705,
    (978, "Thu"): 1691,
    (978, "Tue"): 1352,
    (978, "Wed"): 1521,
    (1292, "Fri"): 6,
    (1292, "Mon"): 3,
    (1292, "Sat"): 7,
    (1292, "Sun"): 7,
    (1292, "Thu"): 4,
    (1292, "Tue"): 3,
    (1292, "Wed"): 4,
    (1751, "Fri"): 55,
    (1751, "Mon"): 34,
    (1751, "Sat"): 68,
    (1751, "Sun"): 68,
    (1751, "Thu"): 42,
    (1751, "Tue"): 34,
    (1751, "Wed"): 38,
    (1793, "Fri"): 158,
    (1793, "Mon"): 97,
    (1793, "Sat"): 195,
    (1793, "Sun"): 195,
    (1793, "Thu"): 122,
    (1793, "Tue"): 97,
    (1793, "Wed"): 109,
    (2464, "Fri"): 33765,
    (2464, "Mon"): 20778,
    (2464, "Sat"): 41556,
    (2464, "Sun"): 41556,
    (2464, "Thu"): 25973,
    (2464, "Tue"): 20778,
    (2464, "Wed"): 23375,
    (2486, "Fri"): 14,
    (2486, "Mon"): 8,
    (2486, "Sat"): 17,
    (2486, "Sun"): 17,
    (2486, "Thu"): 11,
    (2486, "Tue"): 8,
    (2486, "Wed"): 10,
    (2552, "Fri"): 16,
    (2552, "Mon"): 9,
    (2552, "Sat"): 19,
    (2552, "Sun"): 19,
    (2552, "Thu"): 12,
    (2552, "Tue"): 9,
    (2552, "Wed"): 11,
    (2686, "Fri"): 13,
    (2686, "Mon"): 8,
    (2686, "Sat"): 16,
    (2686, "Sun"): 16,
    (2686, "Thu"): 10,
    (2686, "Tue"): 8,
    (2686, "Wed"): 9,
    (2799, "Fri"): 39,
    (2799, "Mon"): 24,
    (2799, "Sat"): 48,
    (2799, "Sun"): 48,
    (2799, "Thu"): 30,
    (2799, "Tue"): 24,
    (2799, "Wed"): 27,
    (2876, "Fri"): 25,
    (2876, "Mon"): 15,
    (2876, "Sat"): 30,
    (2876, "Sun"): 30,
    (2876, "Thu"): 19,
    (2876, "Tue"): 15,
    (2876, "Wed"): 17,
    (3488, "Fri"): 994,
    (3488, "Mon"): 611,
    (3488, "Sat"): 1223,
    (3488, "Sun"): 1223,
    (3488, "Thu"): 764,
    (3488, "Tue"): 611,
    (3488, "Wed"): 688,
    (3664, "Fri"): 80,
    (3664, "Mon"): 49,
    (3664, "Sat"): 99,
    (3664, "Sun"): 99,
    (3664, "Thu"): 62,
    (3664, "Tue"): 49,
    (3664, "Wed"): 55,
    (3903, "Fri"): 24,
    (3903, "Mon"): 15,
    (3903, "Sat"): 30,
    (3903, "Sun"): 30,
    (3903, "Thu"): 19,
    (3903, "Tue"): 15,
    (3903, "Wed"): 17,
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
