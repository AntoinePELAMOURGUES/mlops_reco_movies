# 🎯 **Objectifs**

_Documenter l’évolution de chaque brique du projet, garantir une approche structurée et scientifique, et préparer une mise en production robuste._

Pour y parvenir, il va falloir garder en tête une ligne conductrice et s'y tenir... Pas toujours évident au regard de ma curiosité.

Revenons à notre projet.. Les questions qui m'animent sont nombreuses. Je me demande par où commencer. Dois-je visualiser l'UI/UX pour avoir un rendu concret et adapter le code par la suite ? Dois-je m'attaquer directement au machine learning en testant des modèles? Dois-je anticipier l'architecture de déploiement avant d'avoir un premier modèle fonctionnel? Difficile de trouver une réponse claire. Je vais donc prendre en considération ma formation de data product manager pour orienter mes choix. Que souhaiterait un client? Quel impact attend-on d'un point de vue business? Quelles seront les contraintes d'infractrusture? Comment les utilisateurs intéragiront avec nos recommandations? En obtenant une meilleure vision des parties prenantes, il sera plus facile d'aborder une démarche pragmatique.

Des clients, j'en ai pas. Il va donc falloir être imaginatif et se challenger tout seul. Je veux arriver à créer une application web avec une base de données utilisateurs. Si un utilisateur n'est pas identifié, on lui demande de créer un compte. Il va ensuite devoir choisir 5 films qu'il aime, soit par une recherche sur le titre, soit en choississant en fonction des propositions que nous lui ferons. Ceci nous permettra ensuite de lui proposer 5 films qui pourraient lui convenir. Ok pour l'idée principale.

Voici maintenant les bases qui me serviront de fil d'Ariane:

---

## Reproductibilité et versionnement (GitHub, MLflow)

Pour garantir la reproductibilité du projet, nous versionnons systématiquement tout le code. À chaque modification, que ce soit sur les scripts de prétraitement des données, les notebooks ou les fichiers de configuration (requirements.txt, Dockerfile, etc.), nous utilisons Git. Cela nous permet de garder une trace précise de l’évolution du projet et de revenir facilement à une version antérieure si besoin.

Nous versionnons également les modèles. Grâce à MLflow, nous enregistrons chaque version de modèle entraîné, en y associant les hyperparamètres, les métriques de performance et les artefacts produits. Cette démarche nous assure de pouvoir reproduire n’importe quelle expérimentation et de comparer objectivement les résultats obtenus.

Pour aller plus loin, nous documentons les versions des jeux de données utilisés pour l’entraînement et les tests. Nous gardons aussi une trace des environnements d’exécution, par exemple via des fichiers YAML ou Docker, afin de garantir que chaque expérience puisse être relancée dans des conditions identiques.

Enfin, nous accordons une grande importance à la documentation. Nous décrivons chaque expérience, les choix d’architecture, les résultats et les itérations dans une documentation vivante, réalisée avec MkDocs. Cela permet à toute personne rejoignant le projet de comprendre rapidement les décisions prises et les étapes franchies.

---

## Automatisation et CI/CD (GitHub Actions)

Nous automatisons les tests en mettant en place des tests unitaires et d’intégration pour l’ensemble du code, qu’il s’agisse de l’API ou des scripts de recommandation. Ces tests sont déclenchés automatiquement à chaque push ou pull request grâce à GitHub Actions. Cela nous assure de détecter rapidement toute régression ou bug introduit lors du développement.

Nous avons également intégré une étape de validation automatique des modèles. Avant toute mise en production d’un nouveau modèle, nous contrôlons systématiquement ses performances sur un jeu de test. Ce processus garantit que seuls les modèles répondant à nos critères de qualité sont déployés.

Le déploiement de l’application web, de l’API de recommandation et des modèles est lui aussi automatisé via GitHub Actions. Nous pouvons ainsi déployer rapidement sur un serveur ou un cluster cloud, tout en gardant un historique précis des versions mises en production.

Enfin, nous avons prévu la possibilité de revenir facilement à une version antérieure du modèle ou de l’application en cas de problème, afin d’assurer la continuité du service.

---

## Orchestration des workflows (Apache Airflow)

Nous découpons nos pipelines en tâches indépendantes : ingestion des données, prétraitement, entraînement, évaluation, déploiement. Cette structuration nous permet de mieux organiser le travail et d’optimiser les ressources.

Avec Airflow, nous définissons précisément l’ordre d’exécution des tâches et leurs dépendances. Cela nous permet de relancer uniquement les étapes échouées, sans avoir à tout reprendre depuis le début.

Nous planifions également des tâches récurrentes, comme le réentraînement du modèle ou la mise à jour des recommandations, afin de garantir que notre système reste performant dans le temps.

L’interface d’Airflow nous offre un monitoring en temps réel de l’état des tâches. Nous pouvons ainsi détecter rapidement les erreurs et relancer les jobs si nécessaire.

---

## Isolation et portabilité (Docker)

Pour assurer la portabilité et l’isolation de chaque composant du projet, nous créons un Dockerfile dédié pour l’API, l’application web, le pipeline de machine learning et le monitoring. Chaque service fonctionne ainsi dans son propre conteneur, ce qui évite les conflits de dépendances et facilite la montée en production.

En développement local, nous utilisons Docker Compose pour orchestrer l’ensemble des services (API, base de données, Prometheus, Grafana, etc.). Cela simplifie grandement les tests et la gestion des environnements.

Nous veillons à ce que toutes les dépendances soient soigneusement listées dans les fichiers de configuration Docker, afin d’éviter toute incompatibilité entre les différents environnements.

---

## Déploiement et surveillance (Prometheus & Grafana)

Nous intégrons dans notre API des endpoints qui exposent des métriques (latence, taux d’erreur, nombre de requêtes, etc.) au format Prometheus. Prometheus est configuré pour scruter régulièrement ces endpoints et stocker les métriques dans sa base de données time-series.

Nous connectons ensuite Grafana à Prometheus pour créer des dashboards personnalisés. Ceux-ci nous permettent de visualiser la santé de l’API, la performance du modèle (précision, recall, etc.) et la distribution des données entrantes, notamment pour détecter tout phénomène de drift.

Des règles d’alerte sont mises en place dans Grafana : par exemple, en cas de latence trop élevée, de dérive du modèle ou de baisse de la précision, nous recevons immédiatement une notification par Slack ou email.

Enfin, nous surveillons la dérive des données en intégrant des métriques spécifiques et en configurant des alertes dédiées, afin de pouvoir réagir rapidement à tout changement anormal dans les données ou les performances du modèle[1].
