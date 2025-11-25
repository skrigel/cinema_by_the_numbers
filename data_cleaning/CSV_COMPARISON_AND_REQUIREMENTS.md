# CSV Files Comparison & Model Requirements

## Overview of Three CSV Files

### 1. `final_df.csv` (Base Dataset)
- **Rows:** 10,068
- **Columns:** 39
- **Content:** SOVAI box office data + TMDB metadata (merged and filtered)
- **Status:** Complete base dataset

### 2. `final_with_omdb.csv` (Old Merge - NOT RECOMMENDED)
- **Rows:** 4,152 (**Lost 5,916 movies - 58.7% data loss**)
- **Columns:** 71
- **Content:** SOVAI + TMDB + OMDB data
- **Status:** **Outdated - drops movies without Rotten Tomatoes ratings**
- **Issue:** Uses `dropna(subset=["Rating_RottenTomatoes"])` which removes valuable data

### 3. `final_merged_dataset.csv` (Recommended)
- **Rows:** 10,067 (**Preserves all movies**)
- **Columns:** 61
- **Content:** SOVAI + TMDB + OMDB data (left join - preserves all movies)
- **Status:** **Use this file for all analysis**

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

1. **Complete Data:** Preserves all 10,067 movies (no data loss)
2. **All Required Features:** Contains all columns needed for models
3. **Clean Structure:** Proper column naming, no duplicates
4. **OMDB Ratings Available:** 61.9% of movies have OMDB data for enhanced predictions

### Essential Columns for Your Models:

**From Base Dataset (always available):**
- `runtime` - For optimization and choice modeling
- `genre_names` / `genre_ids` - For choice modeling
- `release_date` / `days_in_release` - For recency features
- `overview` - For text-based features
- `vote_average`, `vote_count`, `popularity` - For popularity features
- `date`, `weekday`, `is_weekend` - For time series
- `gross`, `total_gross`, `theaters` - For demand prediction

**From OMDB (available for 61.9% of movies):**
- `omdb_rating_rottentomatoes` - Rotten Tomatoes score
- `omdb_rating_metacritic` - Metacritic score
- `omdb_imdbrating` - IMDb rating
- `omdb_rated` - MPAA rating

---

## Summary

| File | Rows | Columns | OMDB Data | Data Loss | Recommendation |
|------|------|---------|-----------|-----------|----------------|
| `final_df.csv` | 10,068 | 39 | No | None | Base dataset only |
| `final_with_omdb.csv` | 4,152 | 71 | Yes | **58.7% lost** | **Don't use** |
| `final_merged_dataset.csv` | 10,067 | 61 | Yes (61.9%) | None | **Use this** |

