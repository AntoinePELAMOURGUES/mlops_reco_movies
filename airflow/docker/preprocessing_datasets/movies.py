# movies.py
from typing import Optional
import pandas as pd
import logging
import os
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

logger = logging.getLogger(__name__)


def preprocess_movies(df: pd.DataFrame) -> pd.DataFrame:
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
    df = df.astype({"movieId": "int32"}).rename(columns={"movieId": "movie_id"})

    try:
        # Extraction de l'année avec regex robuste
        df["year"] = (
            df["title"]
            .str.extract(r"(?:\(|\[)?(\d{4})(?:\)|\]| TV)?")[0]
            .astype(float)
            .astype("Int64")
        )
        # Gestion des valeurs manquantes, outliers, par médiane
        ANNEE_MIN = 1888
        ANNEE_MAX = 2025
        # Remplacer les années aberrantes par NaN
        df.loc[(df["year"] < ANNEE_MIN) | (df["year"] > ANNEE_MAX), "year"] = np.nan

        # Imputation par la médiane des valeurs valides
        median_year = df.loc[df["year"].between(ANNEE_MIN, ANNEE_MAX), "year"].median()
        df["year"] = df["year"].fillna(median_year)

        # Nettoyage du titre
        df["clean_title"] = df["title"].str.replace(r"\s*[\[(]\d{4}[\])]\s*", "", regex=True)

        # Gestion des genres avec seuillage
        df["genres"] = df["genres"].str.replace("(no genres listed)|^$", "Unknown", regex=True)
        genre_lists = df["genres"].str.split("|")
        df["genres_list"] = genre_lists
        df["genres"] = genre_lists.str.join(", ")

        # One-Hot Encoding
        mlb = MultiLabelBinarizer()
        genres_encoded = pd.DataFrame(
            mlb.fit_transform(genre_lists), columns=mlb.classes_, index=df.index
        )
        df = pd.concat([df, genres_encoded], axis=1)

    except Exception as e:
        logger.error(f"Erreur de prétraitement : {str(e)}")
        raise

    # Validation finale
    assert df["movie_id"].is_unique, "IDs de films dupliqués"
    assert df["genres"].notna().all(), "Genres manquants"
    logger.info(f"Prétraitement movies terminé. Films traités : {len(df)}")

    return df
