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
    (266, "Fri"): 27987,
    (266, "Mon"): 17222,
    (266, "Sat"): 34445,
    (266, "Sun"): 34445,
    (266, "Thu"): 21528,
    (266, "Tue"): 17222,
    (266, "Wed"): 19375,
    (471, "Fri"): 32028,
    (471, "Mon"): 19709,
    (471, "Sat"): 39419,
    (471, "Sun"): 39419,
    (471, "Thu"): 24637,
    (471, "Tue"): 19709,
    (471, "Wed"): 22173,
    (978, "Fri"): 1125338,
    (978, "Mon"): 692515,
    (978, "Sat"): 1385031,
    (978, "Sun"): 1385031,
    (978, "Thu"): 865644,
    (978, "Tue"): 692515,
    (978, "Wed"): 779080,
    (1292, "Fri"): 14886,
    (1292, "Mon"): 9161,
    (1292, "Sat"): 18322,
    (1292, "Sun"): 18322,
    (1292, "Thu"): 11451,
    (1292, "Tue"): 9161,
    (1292, "Wed"): 10306,
    (1751, "Fri"): 29557,
    (1751, "Mon"): 18189,
    (1751, "Sat"): 36378,
    (1751, "Sun"): 36378,
    (1751, "Thu"): 22736,
    (1751, "Tue"): 18189,
    (1751, "Wed"): 20463,
    (1793, "Fri"): 40083,
    (1793, "Mon"): 24666,
    (1793, "Sat"): 49333,
    (1793, "Sun"): 49333,
    (1793, "Thu"): 30833,
    (1793, "Tue"): 24666,
    (1793, "Wed"): 27749,
    (2464, "Fri"): 50647,
    (2464, "Mon"): 31167,
    (2464, "Sat"): 62335,
    (2464, "Sun"): 62335,
    (2464, "Thu"): 38959,
    (2464, "Tue"): 31167,
    (2464, "Wed"): 35063,
    (2486, "Fri"): 49152,
    (2486, "Mon"): 30247,
    (2486, "Sat"): 60495,
    (2486, "Sun"): 60495,
    (2486, "Thu"): 37809,
    (2486, "Tue"): 30247,
    (2486, "Wed"): 34028,
    (2552, "Fri"): 36998,
    (2552, "Mon"): 22768,
    (2552, "Sat"): 45536,
    (2552, "Sun"): 45536,
    (2552, "Thu"): 28460,
    (2552, "Tue"): 22768,
    (2552, "Wed"): 25614,
    (2686, "Fri"): 18518,
    (2686, "Mon"): 11396,
    (2686, "Sat"): 22792,
    (2686, "Sun"): 22792,
    (2686, "Thu"): 14245,
    (2686, "Tue"): 11396,
    (2686, "Wed"): 12820,
    (2799, "Fri"): 45432,
    (2799, "Mon"): 27958,
    (2799, "Sat"): 55917,
    (2799, "Sun"): 55917,
    (2799, "Thu"): 34948,
    (2799, "Tue"): 27958,
    (2799, "Wed"): 31453,
    (2876, "Fri"): 50545,
    (2876, "Mon"): 31104,
    (2876, "Sat"): 62209,
    (2876, "Sun"): 62209,
    (2876, "Thu"): 38881,
    (2876, "Tue"): 31104,
    (2876, "Wed"): 34992,
    (3488, "Fri"): 106403,
    (3488, "Mon"): 65479,
    (3488, "Sat"): 130958,
    (3488, "Sun"): 130958,
    (3488, "Thu"): 81848,
    (3488, "Tue"): 65479,
    (3488, "Wed"): 73663,
    (3664, "Fri"): 143794,
    (3664, "Mon"): 88489,
    (3664, "Sat"): 176978,
    (3664, "Sun"): 176978,
    (3664, "Thu"): 110611,
    (3664, "Tue"): 88489,
    (3664, "Wed"): 99550,
    (3903, "Fri"): 31843,
    (3903, "Mon"): 19596,
    (3903, "Sat"): 39192,
    (3903, "Sun"): 39192,
    (3903, "Thu"): 24495,
    (3903, "Tue"): 19596,
    (3903, "Wed"): 22045,
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
