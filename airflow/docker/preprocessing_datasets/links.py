# links.py
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def preprocess_links(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prétraite le dataset links avec :
    - Gestion des IDs manquants
    - Typage cohérent pour les jointures
    """
    try:
        df = df.astype({"movieId": "int32"}).rename(columns={"movieId": "movie_id", "tmdbId": "tmdb_id", "imdbId": "imdb_id"})
        df["tmdb_id"] = df["tmdb_id"].fillna(0).astype("int64")
        df["imdb_id"] = "tt" + df["imdb_id"].astype(str).str.lstrip("tt").str.zfill(7)

        # Validation des clés externes
        missing_tmdb = df["tmdb_id"].eq(0).mean()
        if missing_tmdb > 0.1:
            logger.warning(f"{missing_tmdb:.1%} des tmdbId manquants")

    except Exception as e:
        logger.error(f"Erreur de prétraitement links : {str(e)}")
        raise

    assert df["movie_id"].is_unique, "IDs de films dupliqués"
    logger.info(f"Links traités : {len(df)} lignes")

    return df
