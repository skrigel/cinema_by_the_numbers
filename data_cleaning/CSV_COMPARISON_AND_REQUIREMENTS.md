# CSV Files Comparison & Model Requirements

## Overview of CSV Files

### 1. `final_df.csv` (Base Dataset)
- **Rows:** 10,067
- **Columns:** 39
- **Content:** SOVAI box office data + TMDB metadata (merged and filtered)
- **Status:** Complete base dataset (before OMDB merge and deduplication)

### 2. `final_with_omdb.csv` (Old Merge - NOT RECOMMENDED)
- **Rows:** 4,152 (**Lost 5,915 movies - 58.7% data loss**)
- **Columns:** 71
- **Content:** SOVAI + TMDB + OMDB data
- **Status:** **Outdated - drops movies without Rotten Tomatoes ratings**
- **Issue:** Uses `dropna(subset=["Rating_RottenTomatoes"])` which removes valuable data
- **Note:** This file is kept for reference but should not be used for analysis

### 3. `final_merged_dataset.csv` (Recommended)
- **Rows:** 4,429 unique movies (after deduplication)
- **Columns:** 61
- **Content:** SOVAI + TMDB + OMDB data (left join - preserves all movies)
- **Date range:** 1993-02-11 to 2025-10-23 (excludes pre-1990 and last 30 days)
- **OMDB coverage:** 68.2% of movies have OMDB ratings data
- **Deduplication:** Removed 5,575 duplicate rows (55.7% reduction) using intelligent value aggregation
- **Status:** **Use this file for all analysis**

### 4. `final_merged_dataset_with_genres.csv` (Recommended)
- **Rows:** 4,429 unique movies (same as `final_merged_dataset.csv`)
- **Columns:** 81 (61 original + 19 binary genre columns + 1 genres_list column)
- **Content:** All data from `final_merged_dataset.csv` plus binary-encoded genre columns
- **Genre encoding:** 19 binary columns (0/1) for each genre: action, adventure, animation, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, romance, science_fiction, thriller, tv_movie, war, western
- **Date range:** 1993-02-11 to 2025-10-23 (same as base dataset)
- **OMDB coverage:** 68.2% of movies have OMDB ratings data
- **Status:** **Use this file for choice modeling and any analysis requiring binary genre features**

---

## Detailed Column Comparison

### Columns in `final_df.csv` (39 columns)

**SOVAI Box Office Data:**
1. `ticker` - Stock ticker of distributor
2. `date` - Date of box office record
3. `title` - Movie title
4. `distributor` - Distribution company
5. `gross` - Daily gross revenue
6. `percent_yd` - Percent change year-over-year
7. `percent_lw` - Percent change week-over-week
8. `theaters` - Number of theaters showing movie
9. `per_theater` - Gross per theater
10. `total_gross` - Cumulative total gross
11. `days_in_release` - Days since release
12. `parent company` - Parent company of distributor
13. `release_date` - Original release date
14. `year` - Release year
15. `gross_per_theater` - Calculated feature

**TMDB Metadata:**
16. `title_key` - Normalized title for merging
17. `tmdb_id` - TMDB unique identifier
18. `popularity` - TMDB popularity score
19. `imdb_id` - IMDb unique identifier
20. `original_language` - Original language
21. `status` - Movie status (Released, etc.)
22. `budget` - Production budget
23. `revenue` - Total revenue
24. `adult` - Adult content flag
25. `overview` - Movie description/plot
26. `runtime` - Movie duration in minutes **NEEDED**
27. `vote_average` - Average rating
28. `vote_count` - Number of votes
29. `origin_country` - Country of origin
30. `spoken_languages` - Languages spoken
31. `genre_ids` - Genre IDs **NEEDED**
32. `genre_names` - Genre names **NEEDED**
33. `production_company_ids` - Production company IDs
34. `production_company_names` - Production company names
35. `belongs_to_collection` - Collection membership

**Engineered Features:**
36. `weekday` - Day of week (0-6)
37. `release_month` - Release month
38. `release_weekday` - Day of week of release
39. `is_weekend` - Weekend flag **NEEDED**

---

### Additional Columns in `final_with_omdb.csv` (32 extra columns)

**OMDB Data (unprefixed - causes confusion):**
40. `Title` - OMDB title (duplicate of `title`)
41. `Year` - OMDB year
42. `Rated` - MPAA rating
43. `Released` - Release date
44. `Runtime` - Runtime (duplicate of `runtime`)
45. `Genre` - Genre (duplicate of `genre_names`)
46. `Director` - Director name
47. `Writer` - Writer name
48. `Actors` - Actor names
49. `Plot` - Plot description (duplicate of `overview`)
50. `Language` - Language
51. `Country` - Country
52. `Awards` - Awards information
53. `Poster` - Poster URL
54. `Metascore` - Metacritic score **POTENTIALLY USEFUL**
55. `imdbRating` - IMDb rating **POTENTIALLY USEFUL**
56. `imdbVotes` - IMDb vote count
57. `BoxOffice` - Box office earnings
58. `Production` - Production company
59. `Website` - Movie website
60. `Response` - API response status
61. `Rating_InternetMovieDatabase` - IMDb rating (formatted)
62. `Rating_RottenTomatoes` - Rotten Tomatoes rating **POTENTIALLY USEFUL**
63. `Rating_Metacritic` - Metacritic rating **POTENTIALLY USEFUL**
64. `Season` - TV season (not relevant)
65. `Episode` - TV episode (not relevant)
66. `seriesID` - Series ID (not relevant)
67. `Error` - API error flag
68. `totalSeasons` - Total seasons (not relevant)
69. `date_x` - Duplicate date column (merge artifact)
70. `date_y` - Duplicate date column (merge artifact)

**Issues:**
- Duplicate columns (Title, Runtime, Genre, Plot)
- Unprefixed OMDB columns cause confusion
- Duplicate date columns (`date_x`, `date_y`)
- Includes irrelevant TV series columns

---

### Additional Columns in `final_merged_dataset.csv` (22 extra columns)

**OMDB Data (properly prefixed with `omdb_`):**
40. `omdb_title` - OMDB title
41. `omdb_year` - OMDB year
42. `omdb_rated` - MPAA rating **POTENTIALLY USEFUL**
43. `omdb_released` - Release date
44. `omdb_runtime` - Runtime (alternative source)
45. `omdb_genre` - Genre (alternative source)
46. `omdb_director` - Director name
47. `omdb_writer` - Writer name
48. `omdb_actors` - Actor names
49. `omdb_plot` - Plot description
50. `omdb_language` - Language
51. `omdb_country` - Country
52. `omdb_awards` - Awards information
53. `omdb_poster` - Poster URL
54. `omdb_metascore` - Metacritic score **POTENTIALLY USEFUL**
55. `omdb_imdbrating` - IMDb rating **POTENTIALLY USEFUL**
56. `omdb_imdbvotes` - IMDb vote count
57. `omdb_boxoffice` - Box office earnings
58. `omdb_production` - Production company
59. `omdb_rating_internetmoviedatabase` - IMDb rating (formatted)
60. `omdb_rating_rottentomatoes` - Rotten Tomatoes rating **POTENTIALLY USEFUL**
61. `omdb_rating_metacritic` - Metacritic rating **POTENTIALLY USEFUL**

---

### Additional Columns in `final_merged_dataset_with_genres.csv` (20 extra columns)

**All columns from `final_merged_dataset.csv` (61 columns) plus:**

**Genre Encoding (binary 0/1 columns):**
62. `genres_list` - List of normalized genre names (intermediate column)
63. `action` - Binary flag (1 if movie has Action genre, 0 otherwise) **USEFUL FOR CHOICE MODELING**
64. `adventure` - Binary flag for Adventure genre
65. `animation` - Binary flag for Animation genre
66. `comedy` - Binary flag for Comedy genre
67. `crime` - Binary flag for Crime genre
68. `documentary` - Binary flag for Documentary genre
69. `drama` - Binary flag for Drama genre
70. `family` - Binary flag for Family genre
71. `fantasy` - Binary flag for Fantasy genre
72. `history` - Binary flag for History genre
73. `horror` - Binary flag for Horror genre
74. `music` - Binary flag for Music genre
75. `mystery` - Binary flag for Mystery genre
76. `romance` - Binary flag for Romance genre
77. `science_fiction` - Binary flag for Science Fiction genre
78. `thriller` - Binary flag for Thriller genre
79. `tv_movie` - Binary flag for TV Movie genre
80. `war` - Binary flag for War genre
81. `western` - Binary flag for Western genre

**Note:** These binary genre columns are created using `MultiLabelBinarizer` from scikit-learn, which converts the comma-separated `genre_names` string into individual binary columns. This format is ideal for machine learning models, especially choice modeling where genre preferences are key features.

---

## Model Inputs

### 1. **Time Series Forecasting Model** (Total Daily Theater Demand)

**Required Inputs:**
- `date` - For time series analysis
- `gross` or `total_gross` - Historical revenue data
- `weekday` / `is_weekend` - Day-of-week patterns
- `release_date` - For new release spikes
- `release_month` - Seasonality patterns
- `year` - Long-term trends

**Optional but Useful:**
- `theaters` - Theater count for normalization
- `per_theater` - Per-theater performance

---

### 2. **Choice Model** (Multinomial Logit - Demand Share per Film)

**Required Inputs:**
- `genre_names` or `genre_ids` - Genre preferences 
- **OR use binary genre columns** from `final_merged_dataset_with_genres.csv` (action, adventure, animation, etc.) - **Recommended for easier modeling**
- `runtime` - Movie duration
- `release_date` / `days_in_release` - Recency factor
- `overview` - Movie description (for text features)

**Highly Recommended:**
- `vote_average` - TMDB rating (popularity indicator)
- `vote_count` - Number of ratings (popularity indicator)
- `popularity` - TMDB popularity score
- `omdb_rating_rottentomatoes` - Rotten Tomatoes rating (if available)
- `omdb_rating_metacritic` - Metacritic rating (if available)
- `omdb_imdbrating` - IMDb rating (if available)
- `budget` - Production budget (quality signal)
- `is_weekend` - Weekend vs weekday preference

**Optional:**
- `omdb_rated` - MPAA rating (G, PG, PG-13, R)
- `distributor` - Distribution company (brand effect)
- `production_company_names` - Studio effects

---

### 3. **Optimization Model** (Showtime Scheduling)

**Required Inputs:**
- `runtime` - Movie duration (D_i)
- **Predicted attendance/demand** (A_i,d) - From prediction models
- `ticket_price` - Not in dataset (needs to be set/estimated)
- `release_date` - For recency constraints
- `days_in_release` - For recency calculations

**Optional:**
- `genre_names` - For diversity constraints
- `omdb_rated` - For age-appropriate scheduling

---

## Recommended Dataset: `final_merged_dataset.csv`

### Why Use This File:

1. **Complete Data:** Preserves all movies from base dataset (no data loss from merge)
2. **Deduplicated:** Each movie appears only once with intelligently aggregated values
3. **All Required Features:** Contains all columns needed for models
4. **Clean Structure:** Proper column naming, no duplicate columns
5. **OMDB Ratings Available:** 68.2% of movies have OMDB data for enhanced predictions
6. **Date Filtered:** Includes only movies from 1990 to October 2025 (excludes pre-1990 and very recent releases)

### Essential Columns for Your Models:

**From Base Dataset (always available):**
- `runtime` - For optimization and choice modeling
- `genre_names` / `genre_ids` - For choice modeling
- `release_date` / `days_in_release` - For recency features
- `overview` - For text-based features
- `vote_average`, `vote_count`, `popularity` - For popularity features
- `date`, `weekday`, `is_weekend` - For time series
- `gross`, `total_gross`, `theaters` - For demand prediction

**From OMDB (available for 68.2% of movies):**
- `omdb_rating_rottentomatoes` - Rotten Tomatoes score
- `omdb_rating_metacritic` - Metacritic score
- `omdb_imdbrating` - IMDb rating
- `omdb_rated` - MPAA rating

---

## Summary

| File | Rows | Columns | OMDB Data | Genre Encoding | Recommendation |
|------|------|---------|-----------|----------------|----------------|
| `final_df.csv` | 10,067 | 39 | No | No | Base dataset only |
| `final_with_omdb.csv` | 4,152 | 71 | Yes | No | **Don't use** (58.7% data loss) |
| `final_merged_dataset.csv` | 4,429 | 61 | Yes (68.2%) | No | **Use for general analysis** |
| `final_merged_dataset_with_genres.csv` | 4,429 | 81 | Yes (68.2%) | Yes (19 binary columns) | **Use for choice modeling** |

**Notes:**
- `final_merged_dataset.csv`: After deduplication, contains 4,429 unique movies. The original merge preserved all movies, but duplicates were removed using intelligent value aggregation (taking maximum values for numeric fields, longest text for descriptions, etc.).
- `final_merged_dataset_with_genres.csv`: Contains all data from `final_merged_dataset.csv` plus 19 binary genre columns (0/1) for machine learning models that require categorical genre features.

