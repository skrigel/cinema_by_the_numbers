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
- `final_df.csv`: Filtered version (English, post-2000, valid data) - 10,068 rows
- `final_with_omdb.csv`: Only 4,152 rows - loses ~60% of data due to dropping rows without Rotten Tomatoes ratings (outdated, not recommended)
- **`final_merged_dataset.csv`**: Complete merged dataset - 10,067 rows, 61 columns (RECOMMENDED)

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
   - 10,068 movies with complete box office and TMDB metadata

2. **Load and combine OMDB batch files**
   - Combine all 11 batch CSV files
   - Remove duplicates based on `imdbID`
   - Filter to post-2000 releases (matching final_df filter)

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

5. **Clean up columns**
   - Remove duplicate date columns (`date_x`, `date_y`)
   - Drop columns with all null values
   - Rename columns for clarity

6. **Save final dataset**
   - Output: `data/cleaned/final_merged_dataset.csv`
   - Expected: ~10,068 rows (same as final_df)
   - Columns: All from final_df + OMDB columns (with nulls where OMDB data unavailable)

## Actual Results

- **Total rows:** 10,067 (preserves all movies from final_df)
- **Movies with OMDB data:** 6,233 (61.9% of movies)
- **Movies without OMDB data:** 3,834 (38.1% of movies - OMDB columns are null)
- **Total columns:** 61 (combining all data sources)

## Benefits of This Approach

1. **No data loss:** All movies from final_df are preserved
2. **Flexible analysis:** Can analyze with or without OMDB ratings
3. **Handles missing data:** Missing OMDB data is represented as nulls, not dropped rows
4. **Clean column structure:** Proper naming and no duplicates

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

This file contains all movies from `final_df.csv` with OMDB ratings data added where available. Movies without OMDB data have null values for OMDB columns, preserving all 10,067 movies.

## Key Features of Final Dataset

1. **Complete data preservation:** All 10,067 movies from final_df.csv are included
2. **OMDB ratings available:** 61.9% of movies have OMDB data (Rotten Tomatoes, Metacritic, IMDb ratings)
3. **Clean column structure:** All OMDB columns properly prefixed with `omdb_` to avoid conflicts
4. **No duplicate columns:** Removed duplicate date columns and irrelevant TV series data
5. **Ready for modeling:** Contains all required features for prediction and optimization models

## Dataset Usage

Use `final_merged_dataset.csv` for:
- Time series forecasting models
- Choice modeling (multinomial logit)
- Optimization model inputs
- Feature engineering

See `CSV_COMPARISON_AND_REQUIREMENTS.md` for detailed column descriptions and model requirements.

## Next Steps

1. Use `final_merged_dataset.csv` as the primary dataset for all modeling
2. Handle missing OMDB data gracefully in models (61.9% have it, 38.1% don't)
3. Consider feature engineering with OMDB rating columns
4. Archive or delete `final_with_omdb.csv` (outdated, loses 58.7% of data)

