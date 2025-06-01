# movies.py
from typing import Optional
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)


def preprocess_movies(df: pd.DataFrame, genres_threshold: Optional[int] = None) -> pd.DataFrame:
    """
    Prétraite le dataset movies avec gestion MLOps :
    - Extraction robuste de l'année
    - Gestion des genres (one-hot encoding + liste)
    - Validation des données en sortie

    Args:
        genres_threshold: Seuil minimal d'occurrence pour garder un genre (évite le overfitting)
    """
    # Typage et validation initiale
    assert {"movieId", "title", "genres"}.issubset(df.columns), "Colonnes manquantes"
    df = df.astype({"movieId": "int32"}).rename(columns={"movieId": "movieid"})

    try:
        # Extraction de l'année avec regex robuste
        df["year"] = (
            df["title"]
            .str.extract(r"(?:\(|\[)?(\d{4})(?:\)|\]| TV)?")[0]
            .astype(float)
            .astype("Int64")
        )
        # Imputation par la médiane (configurable via environnement)
        df["year"] = (
            df["year"]
            .fillna(int(os.getenv("MOVIES_YEAR_MEDIAN", df["year"].median())))
            .astype("Int64")
        )

        # Nettoyage du titre
        df["clean_title"] = df["title"].str.replace(r"\s*[\[(]\d{4}[\])]\s*", "", regex=True)

        # Gestion des genres avec seuillage
        df["genres"] = df["genres"].str.replace("(no genres listed)|^$", "Unknown", regex=True)
        genre_lists = df["genres"].str.split("|")

        if genres_threshold:
            from collections import Counter

            genre_counts = Counter([g for sublist in genre_lists for g in sublist])
            valid_genres = {k for k, v in genre_counts.items() if v >= genres_threshold}
            genre_lists = genre_lists.apply(lambda x: [g for g in x if g in valid_genres])

        df["genres_list"] = genre_lists
        df["genres"] = genre_lists.str.join(", ")

        # One-Hot Encoding (optionnel)
        if os.getenv("ENABLE_ONEHOT", "false").lower() == "true":
            from sklearn.preprocessing import MultiLabelBinarizer

            mlb = MultiLabelBinarizer()
            genres_encoded = pd.DataFrame(
                mlb.fit_transform(genre_lists), columns=mlb.classes_, index=df.index
            )
            df = pd.concat([df, genres_encoded], axis=1)

    except Exception as e:
        logger.error(f"Erreur de prétraitement : {str(e)}")
        raise

    # Validation finale
    assert df["movieid"].is_unique, "IDs de films dupliqués"
    assert df["genres"].notna().all(), "Genres manquants"
    logger.info(f"Prétraitement movies terminé. Films traités : {len(df)}")

    return df
