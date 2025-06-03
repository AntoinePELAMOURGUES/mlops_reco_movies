from typing import Optional
import pandas as pd
import logging
import os
import numpy as np
from pandas.api.types import is_float_dtype

logger = logging.getLogger(__name__)

def preprocess_genome_scores(
    df: pd.DataFrame,
    tags_df: pd.DataFrame,
    min_relevance: Optional[float] = 0.2,
    max_memory_usage: Optional[int] = 1024
) -> pd.DataFrame:
    """
    Prétraite le dataset genome-scores avec gestion MLOps :
    - Optimisation mémoire pour les grands volumes
    - Filtrage des signaux faibles
    - Validation d'intégrité référentielle

    Args:
        min_relevance: Seuil minimal de pertinence (défaut: environ 0.01)
        max_memory_usage: Mémoire max en MB pour l'optimisation des types
    """
    # Configuration adaptive
    min_relevance = float(os.getenv("MIN_RELEVANCE", min_relevance))

    # Validation initiale
    assert {"movieId", "tagId", "relevance"}.issubset(df.columns), "Colonnes manquantes"

    try:
        # Optimisation mémoire
        df = df.astype({
            "movieId": "int32",
            "tagId": "int32",
            "relevance": "float32"
        }).rename(columns={"movieId": "movie_id", "tagId": "tag_id"})

        # Filtrage des valeurs non-informatives
        if min_relevance > 0:
            df = df[df["relevance"] >= min_relevance]

        # Normalisation adaptative
        if os.getenv("LOG_SCALE_RELEVANCE", "false").lower() == "true":
            df["relevance"] = np.log1p(df["relevance"])

        # Validation référentielle
        valid_tags = tags_df["tag_id"].unique()
        df = df[df["tag_id"].isin(valid_tags)]

        # Gestion des doublons complets
        df = df.drop_duplicates(["movie_id", "tag_id"])

        # Optimisation mémoire dynamique
        if max_memory_usage:
            for col in df.columns:
                if is_float_dtype(df[col]):
                    df[col] = pd.to_numeric(df[col], downcast="float")
                else:
                    df[col] = pd.to_numeric(df[col], downcast="integer")

    except Exception as e:
        logger.error(f"Erreur de prétraitement : {str(e)}")
        raise

    # Validation finale
    assert df.merge(tags_df, on="tag_id").notna().all().all(), "Références tagId invalides"
    logger.info(
        f"Prétraitement genome-scores terminé. "
        f"Lignes traitées : {len(df)} - Mémoire utilisée : {df.memory_usage().sum() / 1024**2:.1f}MB"
    )

    return df
