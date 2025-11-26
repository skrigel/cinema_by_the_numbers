# Data Merge Strategy: Cinema by the Numbers

## Overview

This document outlines the comprehensive merge strategy for combining all data sources into a single clean dataset. The merge has been completed and the final dataset is available at `data/cleaned/final_merged_dataset.csv`.

## Data Sources

1. **SOVAI Box Office Data** (`data/raw/sov_data.csv`)
   - Revenue, attendance, theater counts
   - Release dates, distributors
   - Already merged with TMDB basic data in `final_df.csv`

2. **TMDB Metadata** (`data/raw/tmdb_movie_metadata.csv`)
   - Movie details, genres, runtime
   - Popularity scores, vote counts
   - Already merged in `final_df.csv`

3. **OMDB Ratings Data** (`omdb_api/omdbmovies_batch_*.csv`)
   - Rotten Tomatoes, Metacritic, IMDb ratings
   - Additional movie metadata
   - **Merged into final dataset**

## Current State

- `merged_df.csv`: SOVAI + TMDB basic (15,812 rows)
- `merged_with_metadata.csv`: SOVAI + TMDB basic + TMDB metadata (15,811 rows)
- `final_df.csv`: Filtered version (English, post-1990, valid data) - 4,002 rows
- `final_with_omdb.csv`: Only 4,152 rows - loses ~60% of data due to dropping rows without Rotten Tomatoes ratings (outdated, not recommended)
- **`final_merged_dataset.csv`**: Complete merged dataset - 3,971 unique movies, 72 columns (includes inflation-adjusted values) (RECOMMENDED)
- **`final_merged_dataset_with_genres.csv`**: Same as above plus 19 binary genre columns - 3,971 unique movies, 92 columns (RECOMMENDED for choice modeling)

## Problem with Previous Merge

The previous merge in `omdb_api/collecting_data.ipynb` had a critical issue:
```python
final_with_omdb = final_with_omdb.dropna(subset=["Rating_RottenTomatoes"])
```

This drops all movies without Rotten Tomatoes ratings, losing valuable data. Many movies may have other ratings (Metacritic, IMDb) but not Rotten Tomatoes.

## Recommended Merge Strategy

### Approach: Left Join Merge

**Key Principle:** Preserve ALL movies from `final_df.csv`, even if they don't have OMDB data.

### Steps

1. **Load final_df.csv** (already has SOVAI + TMDB merged and filtered)
   - 4,002 movies with complete box office and TMDB metadata

2. **Load and combine OMDB batch files**
   - Combine all 11 batch CSV files
   - Remove duplicates based on `imdbID`
   - Filter to post-1990 releases (matching final_df filter)

3. **Clean OMDB data**
   - Rename `imdbID` → `imdb_id` for consistency
   - Select relevant columns (ratings, metadata)
   - Add `omdb_` prefix to avoid column conflicts

4. **Merge using LEFT JOIN**
   ```python
   final_merged = final_df.merge(
       omdb_cleaned,
       on="imdb_id",
       how="left"  # Keep all movies from final_df
   )
   ```

5. **Filter by date range**
   - Filter to movies from 1990-01-01 to 2025-10-31
   - Exclude movies from the last 30 days (if any are after Oct 31)
   - This ensures reliable training data

6. **Clean up columns and remove duplicate movies**
   - Remove duplicate date columns (`date_x`, `date_y`)
   - Drop columns with all null values
   - **Deduplicate movies** using intelligent value aggregation:
     - Group by `title_key` (normalized movie title)
     - For numeric columns (gross, revenue, theaters): take maximum value
     - For dates: take most recent
     - For text: take longest/most complete
     - For ratings: take first non-null value
   - Result: One row per unique movie with best available data

7. **Adjust monetary values for inflation**
   - Convert all dollar amounts to 2024 dollars (present value) using Consumer Price Index (CPI)
   - Creates adjusted columns: `gross_adjusted_2024`, `total_gross_adjusted_2024`, `budget_adjusted_2024`, `revenue_adjusted_2024`, etc.
   - Ensures accurate comparisons across different years

8. **Save final dataset**
   - Output: `data/cleaned/final_merged_dataset.csv`
   - Expected: ~3,971 unique movies (after date filtering)
   - Columns: All from final_df + OMDB columns + inflation-adjusted columns (with nulls where OMDB data unavailable)

## Actual Results (After Filtering and Deduplication)

The final dataset has been filtered to exclude:
- Movies released before 1990 (saved to `movies_before_1990.csv`)
- Movies released after October 2025 or in the last 30 days (saved to `movies_after_2025_10.csv`)

**Final Dataset Statistics:**
- **Total rows:** 3,971 unique movies (after date filtering)
- **Total columns:** 72 (61 original + 9 inflation-adjusted + 2 helper columns)
- **Release date range:** 1993-02-11 to 2025-10-23
- **Movies with OMDB data:** ~2,710 movies (68.2% of movies)
- **Movies without OMDB data:** ~1,261 movies (31.8% of movies - OMDB columns are null)
- **Inflation adjustment:** All monetary values converted to 2024 dollars using CPI data
- **Deduplication:** No duplicates found (each row is already a unique movie)

## Benefits of This Approach

1. **No data loss from merge:** All movies from final_df are preserved (before deduplication)
2. **Intelligent deduplication:** Each movie appears only once with best available data aggregated
3. **Flexible analysis:** Can analyze with or without OMDB ratings
4. **Handles missing data:** Missing OMDB data is represented as nulls, not dropped rows
5. **Clean column structure:** Proper naming and no duplicate columns
6. **Value aggregation:** When duplicates exist, keeps maximum values for numeric fields, most recent dates, longest text descriptions

## Implementation

The merge has been implemented in:

**Jupyter Notebook:** `data_cleaning/merge_all_data.ipynb`
- Interactive, step-by-step merge process
- Includes data quality checks and summaries
- Documents the complete merge workflow
- Can be re-run if needed to regenerate the dataset

## Usage

To regenerate the merged dataset:
```bash
# Open and run all cells
jupyter notebook data_cleaning/merge_all_data.ipynb
```

## Output

The final merged dataset is saved at:
- `data/cleaned/final_merged_dataset.csv`

This file contains movies from 1990-2025 (excluding the last 30 days) with OMDB ratings data added where available. Movies without OMDB data have null values for OMDB columns. The dataset has been filtered to exclude very old movies (pre-1990) and very recent releases (last 30 days) to ensure reliable training data.

## Key Features of Final Dataset

1. **Filtered for modeling:** Excludes movies before 1990 and very recent releases (after October 2025 or last 30 days)
2. **Deduplicated:** Each movie appears only once (no duplicates in current dataset)
3. **Complete data preservation:** All unique movies from 1990-2025 (excluding last month) are included
4. **OMDB ratings available:** 68.2% of movies have OMDB data (Rotten Tomatoes, Metacritic, IMDb ratings)
5. **Clean column structure:** All OMDB columns properly prefixed with `omdb_` to avoid conflicts
6. **No duplicate columns:** Removed duplicate date columns and irrelevant TV series data
7. **Inflation adjusted:** All monetary values converted to 2024 dollars (present value) for accurate cross-year comparisons
8. **Ready for modeling:** Contains all required features for prediction and optimization models
9. **Inflation-adjusted columns:** Includes `gross_adjusted_2024`, `total_gross_adjusted_2024`, `budget_adjusted_2024`, `revenue_adjusted_2024`, and other monetary values in 2024 dollars

## Excluded Data

Two separate exclusion files are automatically generated by the merge notebook:
- `data/cleaned/movies_before_1990.csv`: Movies released before 1990 (45 movies)
- `data/cleaned/movies_after_2025_10.csv`: Movies released after October 2025 or in the last 30 days (18 movies)

These files are regenerated each time the merge notebook is run to ensure consistency.

## Dataset Usage

Use `final_merged_dataset.csv` for:
- Time series forecasting models
- General analysis and feature engineering
- Optimization model inputs

Use `final_merged_dataset_with_genres.csv` for:
- Choice modeling (multinomial logit) - **Recommended** (includes binary genre columns)
- Machine learning models requiring categorical genre features
- Any analysis benefiting from binary genre encoding

See `CSV_COMPARISON_AND_REQUIREMENTS.md` for detailed column descriptions and model requirements.

## Next Steps

1. Use `final_merged_dataset.csv` as the primary dataset for general modeling
2. Use `final_merged_dataset_with_genres.csv` for choice modeling (includes binary genre columns and inflation-adjusted values)
3. Use inflation-adjusted columns (`*_adjusted_2024`) for accurate cross-year monetary comparisons
4. Handle missing OMDB data gracefully in models (68.2% have it, 31.8% don't)
5. Consider feature engineering with OMDB rating columns
6. Archive or delete `final_with_omdb.csv` (outdated, loses 58.7% of data)

## Additional Dataset: Genre Encoding

A genre-encoded version of the dataset is available:
- **File:** `data/cleaned/final_merged_dataset_with_genres.csv`
- **Created by:** `tmdb_api_calling/genre_encoding.ipynb`
- **Features:** All columns from `final_merged_dataset.csv` (including inflation-adjusted columns) plus 19 binary genre columns (action, adventure, animation, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, romance, science_fiction, thriller, tv_movie, war, western)
- **Total columns:** 92 (72 base + 19 genre + 1 genres_list)
- **Use case:** Ideal for choice modeling and machine learning models requiring both binary genre features and inflation-adjusted monetary values

