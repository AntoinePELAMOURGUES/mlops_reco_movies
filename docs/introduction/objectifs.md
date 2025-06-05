# 🎯 **Objectifs**

_Documenter l’évolution de chaque brique du projet, garantir une approche structurée et scientifique, et préparer une mise en production robuste._

Rien que ça... Pour y parvenir, il va falloir garder en tête une ligne conductrice et s'y tenir... Pas toujours évident.
En débutant ma formation, je me suis très rapidement aperçu de la diversité des choses à connaître et donc de la difficulté de ne pas trop s'éparpiller. J'adore cette . Si j'ai bien une quête professionnelle, c'est de trouver le boulot qui m'enrichisse quotidiennement. Et je crois avoir choisi la bonne voie...

Revenons à notre projet.. Les questions qui m'animent sont nombreuses. Je me demande par où commencer. Dois-je visualiser l'UI/UX pour avoir un rendu concret et adapter le code par la suite ? Dois-je m'attaquer directement au machine learning en testant des modèles? Dois-je anticipier l'architecture de déploiement avant d'avoir un premier modèle fonctionnel? Difficile de trouver une réponse claire. Je vais donc prendre en considération ma formation de data product manager pour orienter mes choix. Que souhaiterait un client? Quel impact attend-on d'un point de vue business? Quelles seront les contraintes d'infractrusture? Comment les utilisateurs intéragiront avec nos recommandations? En obtenant une meilleure vision des parties prenantes, il sera plus facile d'aborder une démarche pragmatique.

### **1. Affiner les briques existantes**

- **📦 Données**

  - *Objectif* : Exploiter scientifiquement le dataset MovieLens (20M+ de notes) pour en extraire des insights exploitables.
  - *Actions* :
    - Valider l’intégrité des données (sommes de contrôle, analyse des missing values).
    - Explorer le _Tag Genome_ pour enrichir les features des films.
    - Documenter chaque étape de preprocessing dans des notebooks dédiés.

- **🎬 Systèmes de recommandation**

  - *Objectif* : Implémenter, comparer et optimiser 3 approches (collaborative, contenu, hybride).
  - *Actions* :
    - Benchmark des algorithmes (k-NN, factorisation de matrices, deep learning).
    - Mesurer l’impact des métriques de similarité (cosinus, Pearson) sur les résultats.
    - Tester des combinaisons hybrides (ex : filtrage collaboratif + NLP sur les tags).

- **⚙️ MLOps**
  - *Objectif* : Industrialiser chaque phase du projet pour un déploiement fiable.
  - *Actions* :
    - **Dockeriser** l’environnement (isolation des dépendances).
    - **Orchestrer** les workflows avec **Airflow** (entraînements récurrents, prétraitements).
    - **Surveiller** les modèles en production via **Prometheus/Grafana** (dérive des données, performance en temps réel).

---

### **2. Indicateurs de progression**

Pour chaque brique, le cahier de bord inclura :

- ✅ **Checklists** des étapes validées (ex : _Données nettoyées_, _Modèle collaboratif entraîné_).
- 📊 **Metrics comparatives** entre les approches (précision, recall, temps d’exécution).
- 🐞 **Journal des problèmes rencontrés** et correctifs appliqués (ex : _fuite de données détectée le 15/06_).
- 📂 **Liens versionnés** vers le code (GitHub), les modèles (MLflow) et les artefacts (Docker Hub).

---

### **3. Feuille de route**

- **Phase 1** (2 semaines) : Exploration des données + MVP du filtrage collaboratif.
- **Phase 2** (3 semaines) : Implémentation des approches hybrides + tests A/B.
- **Phase 3** (1 semaine) : Intégration CI/CD (tests automatisés avec GitHub Actions).
- **Phase 4** (1 semaine) : Déploiement et monitoring avec alertes Slack/Prometheus.

---

### **4. Philosophie du projet**

- **Itératif** : Chaque brique est conçue pour évoluer indépendamment (_ex : remplacer un modèle sans toucher au preprocessing_).
- **Transparent** : Toutes les décisions techniques sont justifiées par des données (logs, métriques, visualisations).
- **Reproductible** : Un collaborateur doit pouvoir relancer l’intégralité du pipeline avec `docker-compose up` et une commande.
