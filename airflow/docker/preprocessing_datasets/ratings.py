# ratings.py
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)


def preprocess_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prétraite le dataset ratings avec :
    - Filtrage configurable des utilisateurs
    - Typage optimisé pour le stockage
    - Calcul de métriques pour le monitoring
    """
    # Configuration via environnement
    user_threshold = int(os.getenv("USERID_THRESHOLD", 20000))
    sample_ratio = float(os.getenv("RATINGS_SAMPLE_RATIO", 1.0))

    try:
        # Typage et filtrage
        df = df.astype({"userId": "int32", "movieId": "int32"})
        df = df.rename(columns={"userId": "userid", "movieId": "movieid"})

        if sample_ratio < 1.0:
            df = df.sample(frac=sample_ratio, random_state=42)

        if user_threshold > 0:
            df = df[df["userid"] < user_threshold]

        # Calcul de métriques
        user_stats = df.groupby("userid")["rating"].agg(["count", "mean", "std"])
        movie_stats = df.groupby("movieid")["rating"].agg(["count", "mean", "std"])

        # Enregistrement pour monitoring
        if os.getenv("LOG_STATS", "false").lower() == "true":
            logger.info(f"User stats:\n{user_stats.describe()}")
            logger.info(f"Movie stats:\n{movie_stats.describe()}")

    except Exception as e:
        logger.error(f"Erreur de prétraitement ratings : {str(e)}")
        raise

    # Validation
    assert df["userid"].between(1, 200000).all(), "Valeurs userid hors plage"
    logger.info(f"Ratings traités : {len(df)} lignes")

    return df
