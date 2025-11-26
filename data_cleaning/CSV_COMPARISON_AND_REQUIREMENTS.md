# CSV Files Comparison & Model Requirements

## Overview of CSV Files

### 1. `final_df.csv` (Base Dataset)
- **Rows:** 4,002
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
- **Rows:** 3,971 unique movies (after date filtering)
- **Columns:** 72 (61 original + 9 inflation-adjusted + 2 helper columns)
- **Content:** SOVAI + TMDB + OMDB data (left join - preserves all movies)
- **Date range:** 1993-02-11 to 2025-10-23 (excludes pre-1990 and last 30 days)
- **OMDB coverage:** 68.2% of movies have OMDB ratings data
- **Inflation adjustment:** All monetary values adjusted to 2024 dollars (present value)
- **Deduplication:** No duplicates found (each row is already a unique movie)
- **Status:** **Use this file for all analysis**

### 4. `final_merged_dataset_with_genres.csv` (Recommended)
- **Rows:** 3,971 unique movies (same as `final_merged_dataset.csv`)
- **Columns:** 92 (72 from base + 19 binary genre columns + 1 genres_list column)
- **Content:** All data from `final_merged_dataset.csv` plus binary-encoded genre columns
- **Genre encoding:** 19 binary columns (0/1) for each genre: action, adventure, animation, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, romance, science_fiction, thriller, tv_movie, war, western
- **Inflation adjustment:** Includes all inflation-adjusted monetary values in 2024 dollars
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

### Additional Columns in `final_merged_dataset.csv` (33 extra columns)

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

**Inflation Adjustment (2024 dollars - present value):**
62. `release_year` - Extracted year from release_date for CPI lookup
63. `cpi_release_year` - Consumer Price Index for the movie's release year
64. `inflation_factor` - Multiplier to convert to 2024 dollars
65. `gross_adjusted_2024` - Daily gross revenue in 2024 dollars **USEFUL FOR COMPARISONS**
66. `total_gross_adjusted_2024` - Cumulative total gross in 2024 dollars **USEFUL FOR COMPARISONS**
67. `per_theater_adjusted_2024` - Gross per theater in 2024 dollars
68. `gross_per_theater_adjusted_2024` - Calculated gross per theater in 2024 dollars
69. `budget_adjusted_2024` - Production budget in 2024 dollars **USEFUL FOR COMPARISONS**
70. `revenue_adjusted_2024` - Total revenue in 2024 dollars **USEFUL FOR COMPARISONS**
71. `omdb_boxoffice_adjusted_2024` - OMDB box office earnings in 2024 dollars
72. `omdb_boxoffice_clean` - Cleaned numeric version of omdb_boxoffice (intermediate column)

---

### Additional Columns in `final_merged_dataset_with_genres.csv` (20 extra columns)

**All columns from `final_merged_dataset.csv` (72 columns) plus:**

**Genre Encoding (binary 0/1 columns):**
73. `genres_list` - List of normalized genre names (intermediate column)
74. `action` - Binary flag (1 if movie has Action genre, 0 otherwise) **USEFUL FOR CHOICE MODELING**
75. `adventure` - Binary flag for Adventure genre
76. `animation` - Binary flag for Animation genre
77. `comedy` - Binary flag for Comedy genre
78. `crime` - Binary flag for Crime genre
79. `documentary` - Binary flag for Documentary genre
80. `drama` - Binary flag for Drama genre
81. `family` - Binary flag for Family genre
82. `fantasy` - Binary flag for Fantasy genre
83. `history` - Binary flag for History genre
84. `horror` - Binary flag for Horror genre
85. `music` - Binary flag for Music genre
86. `mystery` - Binary flag for Mystery genre
87. `romance` - Binary flag for Romance genre
88. `science_fiction` - Binary flag for Science Fiction genre
89. `thriller` - Binary flag for Thriller genre
90. `tv_movie` - Binary flag for TV Movie genre
91. `war` - Binary flag for War genre
92. `western` - Binary flag for Western genre

**Note:** These binary genre columns are created using `MultiLabelBinarizer` from scikit-learn, which converts the comma-separated `genre_names` string into individual binary columns. This format is ideal for machine learning models, especially choice modeling where genre preferences are key features.

---

## Model Inputs

### 1. **Time Series Forecasting Model** (Total Daily Theater Demand)

**Required Inputs:**
- `date` - For time series analysis
- `gross` or `total_gross` - Historical revenue data (use `*_adjusted_2024` columns for accurate cross-year comparisons)
- `weekday` / `is_weekend` - Day-of-week patterns
- `release_date` - For new release spikes
- `release_month` - Seasonality patterns
- `year` - Long-term trends

**Optional but Useful:**
- `theaters` - Theater count for normalization
- `per_theater` - Per-theater performance
- `gross_adjusted_2024`, `total_gross_adjusted_2024` - Inflation-adjusted values for accurate comparisons across years

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
- `budget_adjusted_2024` - Production budget in 2024 dollars (quality signal, use adjusted for cross-year comparisons)
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
- `gross_adjusted_2024` or `total_gross_adjusted_2024` - Revenue in 2024 dollars for accurate revenue calculations

**Optional:**
- `genre_names` - For diversity constraints
- `omdb_rated` - For age-appropriate scheduling

---

## Recommended Dataset: `final_merged_dataset.csv`

### Why Use This File:

1. **Complete Data:** Preserves all movies from base dataset (no data loss from merge)
2. **Deduplicated:** Each movie appears only once (no duplicates found in current dataset)
3. **All Required Features:** Contains all columns needed for models
4. **Clean Structure:** Proper column naming, no duplicate columns
5. **OMDB Ratings Available:** 68.2% of movies have OMDB data for enhanced predictions
6. **Date Filtered:** Includes only movies from 1990 to October 2025 (excludes pre-1990 and very recent releases)
7. **Inflation Adjusted:** All monetary values converted to 2024 dollars (present value) for accurate cross-year comparisons

### Essential Columns for Your Models:

**From Base Dataset (always available):**
- `runtime` - For optimization and choice modeling
- `genre_names` / `genre_ids` - For choice modeling
- `release_date` / `days_in_release` - For recency features
- `overview` - For text-based features
- `vote_average`, `vote_count`, `popularity` - For popularity features
- `date`, `weekday`, `is_weekend` - For time series
- `gross`, `total_gross`, `theaters` - For demand prediction
- `gross_adjusted_2024`, `total_gross_adjusted_2024`, `budget_adjusted_2024`, `revenue_adjusted_2024` - Inflation-adjusted monetary values in 2024 dollars

**From OMDB (available for 68.2% of movies):**
- `omdb_rating_rottentomatoes` - Rotten Tomatoes score
- `omdb_rating_metacritic` - Metacritic score
- `omdb_imdbrating` - IMDb rating
- `omdb_rated` - MPAA rating

---

## Summary

| File | Rows | Columns | OMDB Data | Inflation Adjusted | Genre Encoding | Recommendation |
|------|------|---------|-----------|-------------------|----------------|----------------|
| `final_df.csv` | 4,002 | 39 | No | No | No | Base dataset only |
| `final_with_omdb.csv` | 4,152 | 71 | Yes | No | No | **Don't use** (58.7% data loss) |
| `final_merged_dataset.csv` | 3,971 | 72 | Yes (68.2%) | Yes (9 columns) | No | **Use for general analysis** |
| `final_merged_dataset_with_genres.csv` | 3,971 | 92 | Yes (68.2%) | Yes (9 columns) | Yes (19 binary columns) | **Use for choice modeling** |

**Notes:**
- `final_merged_dataset.csv`: Contains 3,971 unique movies after date filtering (1990-2025, excluding last 30 days). All monetary values are adjusted to 2024 dollars (present value) using Consumer Price Index (CPI) data. Includes 9 inflation-adjusted columns: `gross_adjusted_2024`, `total_gross_adjusted_2024`, `per_theater_adjusted_2024`, `gross_per_theater_adjusted_2024`, `budget_adjusted_2024`, `revenue_adjusted_2024`, `omdb_boxoffice_adjusted_2024`, plus helper columns `cpi_release_year` and `inflation_factor`.
- `final_merged_dataset_with_genres.csv`: Contains all data from `final_merged_dataset.csv` (including inflation-adjusted columns) plus 19 binary genre columns (0/1) for machine learning models that require categorical genre features. Ideal for choice modeling where both monetary values and genre preferences are needed.

