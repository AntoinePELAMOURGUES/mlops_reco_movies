from typing import Optional
import pandas as pd
import logging
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OrdinalEncoder
import spacy
import re


logger = logging.getLogger(__name__)

nlp = spacy.load("en_core_web_sm")


def clean_tag(tag: str) -> str:
    doc = nlp(tag)
    return " ".join(
        token.text.lower() for token in doc if not token.is_punct and not token.is_stop
    )


def preprocess_genome_tags(df: pd.DataFrame, min_term_freq: Optional[int] = 2) -> pd.DataFrame:
    """
    Prétraite le dataset genome-tags avec gestion MLOps :
    - Nettoyage sémantique des tags
    - Dédoublonnage par similarité textuelle
    - Optimisation pour l'embedding

    Args:
        min_term_freq: Seuil d'occurrence minimal pour conserver un terme (TF-IDF)
    """
    # Validation initiale
    assert {"tagId", "tag"}.issubset(df.columns), "Colonnes manquantes"
    df = df.astype({"tagId": "int32"})
    df = df.rename(columns={"tagId": "tag_id"})

    try:
        # Nettoyage des tags
        df["clean_tag"] = df["tag"].apply(clean_tag)

        # Gestion des doublons sémantiques
        if min_term_freq:
            vectorizer = TfidfVectorizer(min_df=min_term_freq)
            tfidf_matrix = vectorizer.fit_transform(df["clean_tag"])
            df = df.iloc[list(vectorizer.vocabulary_.values())].reset_index(drop=True)

        # Catégorisation automatique
        df["category"] = df["clean_tag"].apply(
            lambda x: (
                "decade"
                if (
                    re.search(r"\d{4}s?$", x)
                    or re.search(r"\d{1,2}(st|nd|rd|th) century", x, re.IGNORECASE)
                )
                else "concept"
            )
        )

        # Encodage ordinal des catégories
        encoder = OrdinalEncoder(categories=[df["category"].unique().tolist()])
        df["category_encoded"] = encoder.fit_transform(df[["category"]])

    except Exception as e:
        logger.error(f"Erreur de prétraitement : {str(e)}")
        raise

    # Validation finale
    assert df["tagId"].is_unique, "IDs de tags dupliqués"
    assert df["clean_tag"].str.len().gt(0).all(), "Tags vides après nettoyage"
    logger.info(f"Prétraitement genome-tags terminé. Tags traités : {len(df)}")

    return df
