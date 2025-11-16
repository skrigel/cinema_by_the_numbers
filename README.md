# cinema_by_the_numbers


## Project Description

Cinema by the numbers is a project that involves using historical movie data to predict demand for movies in the future. 

## Project Structure
```
├── data
│   ├── cleaned
│   ├── codes.parq
│   ├── raw
│   └── tickers.parq
├── data_cleaning
│   ├── cleaning_and_merging.ipynb
│   ├── data
│   ├── final_cleaning.ipynb
│   └── schemas
├── optimization
│   └── optimizing_showtimes.ipynb
├── predictions
│   ├── choice_modeling.ipynb
│   └── train_predictor.ipynb
├── preprocessing
│   ├── data_exploration.ipynb
│   └── feature_engineering.ipynb
└── tmdb_api_calling
    ├── __pycache__
    ├── collecting_recent_movie_metadata.ipynb
    ├── collecting_tmdb_metadata.ipynb
    ├── tmdb_api_tutorial.ipynb
    └── utils.py
```

## Data Description
1. `data/cleaned`: Cleaned data: Merged data from SovAI and responses from TMDB API 
2. `data/raw`: Raw data from SovAI and TMDB Movie IDs
3. `data/tickers.parq`: Tickers data from SovAI

## Data Cleaning
1. `data_cleaning/cleaning_and_merging.ipynb`: Cleaning and merging data from SovAI and merging with TMDB ID data 
2. `data_cleaning/final_cleaning.ipynb`: Final cleaning of the data after recieving movie metadata from TMDB API

## TMDB API Calling
1. `tmdb_api_calling/collecting_tmdb_metadata.ipynb`: Collecting movie metadata from TMDB API to be merged with SovAI data in `data_cleaning/final_cleaning.ipynb`
2. `tmdb_api_calling/collecting_recent_movie_metadata.ipynb`: Collecting recent movie metadata from TMDB API to be used as inputs to our optimization model 

## Data Preprocessing
1. `preprocessing/data_exploration.ipynb`: Exploring the data [TODO]
2. `preprocessing/feature_engineering.ipynb`: Engineering features for the data [TODO]

## Optimization
1. `optimization/optimizing_showtimes.ipynb`: Optimizing showtimes [TODO]

## Predictions
1. `predictions/choice_modeling.ipynb`: Choice modeling [TODO]
2. `predictions/train_predictor.ipynb`: Training predictor [TODO]


