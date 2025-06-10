## LET'S GO 🚀

Travail terminé, enfants couchés, ma femme s'allonge sur le canapé prête à plonger dans sa série. Il est temps maintenant pour moi de rejoindre l'univers de la data.

En réalité, je suis loin d'en être au premier jour de ce projet mais l'idée de créer ce carnet de bord étant survenu en cours de route, il va falloir remonter un peu dans le temps.

### 1. Création de mon environnement

Pour garantir l’isolation, la portabilité et la reproductibilité de mon projet, j’ai choisi de créer un environnement dédié avec **Miniconda** et Conda, plutôt que d’installer directement les paquets sur mon système ou d’utiliser uniquement pip.

---

## <img src="https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fraw.githubusercontent.com%2Fbybatkhuu%2Fwiki%2Fmain%2Fassets%2Fimages%2Fpython.jpg" alt="Illustration Python" class="jour-1-photo"/>

---

#### **Pourquoi Miniconda et Conda ?**

- **Isolation complète** : Chaque environnement Conda est indépendant, ce qui évite les conflits de versions entre projets et permet de travailler sur plusieurs projets aux dépendances différentes sans risque d’interférence.
- **Gestion robuste des dépendances** : Conda gère aussi bien les packages Python que des bibliothèques système (C, CUDA, etc.), ce qui est crucial en data science où de nombreuses librairies reposent sur des dépendances compilées.
- **Légèreté de Miniconda** : Miniconda est une version minimaliste d’Anaconda. Il n’installe que le gestionnaire de paquets Conda, ce qui me permet d’ajouter uniquement les outils nécessaires à mon projet, limitant ainsi l’encombrement et les risques de conflits inutiles.
- **Reproductibilité** : Grâce à un fichier de configuration (`conda_env.yml`), il est possible de recréer à l’identique l’environnement sur n’importe quelle machine, ce qui est essentiel pour la collaboration, le déploiement et la traçabilité scientifique.

#### **Fichier de configuration : conda_env.yml**

Ce fichier liste précisément les versions de chaque dépendance utilisée dans le projet. Il sert de référence pour :

- **Recréer l’environnement** : Un simple `conda env create -f conda_env.yml` permet de retrouver exactement le même contexte logiciel.
- **Documenter l’état du projet** : Garder ce fichier versionné dans le dépôt Git permet de suivre l’évolution des dépendances et de garantir la reproductibilité des résultats.
- **Résoudre les problèmes de compatibilité** : Le fichier permet de figer les versions, ce qui limite les risques de bugs liés à des mises à jour inattendues.

```yaml
name: reco_movies
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - jupyter
  - numpy=1.26.4 # Version compatible avec spaCy 3.8
  - pandas=2.2.2
  - seaborn=0.13.2
  - spacy=3.8.2
  - thinc=8.3.2 # Version critique pour la compatibilité
  - cupy=13.2.0 # Si utilisation GPU (adapter à ta version CUDA)
  - pip
  - pip:
      - pandera==0.18.0 # Pour les validations de données
      - plotly==5.18.0 # Visualisations avancées
      - scikit-learn==1.6.0
```

#### **Problèmes rencontrés avec Numpy et SciPy**

Lors de l’installation, j’ai rencontré des incompatibilités avec la version 2.x de Numpy, fraîchement sortie (juin 2024). Certaines librairies (notamment SciPy et spaCy) ne sont pas encore pleinement compatibles avec cette version majeure, ce qui génère des erreurs d’import ou des crashs. Après vérification sur PyPI et dans la documentation des projets concernés, il a donc fallu figer Numpy en version 1.26.4, actuellement la plus stable et compatible avec l’ensemble des outils utilisés.

> _Astuce : Toujours vérifier la compatibilité des versions sur PyPI ou dans la documentation officielle avant de figer une version dans le fichier de configuration, surtout lors de la sortie de versions majeures._

---
