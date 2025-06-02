from fastapi import APIRouter, Query
import pandas as pd
import os

router = APIRouter()

# Mood-to-genre mapping (simple rule-based)
MOOD_GENRE_MAP = {
    "happy": ["Comedy", "Adventure", "Romance"],
    "sad": ["Drama", "Romance"],
    "angry": ["Action", "Thriller"],
    "nostalgic": ["Drama", "Family"],
    "stressed": ["Animation", "Fantasy", "Comedy"],
    "anxious": ["Mystery", "Sci-Fi"],
    "reflective": ["Drama", "Documentary"]
}

# Load the sample dataset once at startup
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned_movies_dataset.csv")
df = pd.read_csv(CSV_PATH)

@router.get("/recommend")
def recommend_movies(mood: str = Query(..., description="Your current mood")):
    genres = MOOD_GENRE_MAP.get(mood.lower())
    if not genres:
        return {
            "error": f"Mood '{mood}' is not supported.",
            "supported_moods": list(MOOD_GENRE_MAP.keys())
        }

    # Filter movies by genre and drop rows with missing genre
    filtered = df[df["genre"].isin(genres)].dropna(subset=["genre"])

    # Select up to 5 recommendations
    sample = filtered.sample(n=min(5, len(filtered)), random_state=1)

    return {
        "mood": mood,
        "genres_matched": genres,
        "recommendations": sample[["title", "genre", "release_date"]].to_dict(orient="records")
    }
