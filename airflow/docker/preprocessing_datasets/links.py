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
        df = df.astype({"movieId": "int32"}).rename(columns={"movieId": "movieid"})
        df["tmdbId"] = df["tmdbId"].fillna(0).astype("int64")
        df["imdbId"] = "tt" + df["imdbId"].str.lstrip("tt").str.zfill(7)

        # Validation des clés externes
        missing_tmdb = df["tmdbId"].eq(0).mean()
        if missing_tmdb > 0.1:
            logger.warning(f"{missing_tmdb:.1%} des tmdbId manquants")

    except Exception as e:
        logger.error(f"Erreur de prétraitement links : {str(e)}")
        raise

    assert df["movieid"].is_unique, "IDs de films dupliqués"
    logger.info(f"Links traités : {len(df)} lignes")

    return df
