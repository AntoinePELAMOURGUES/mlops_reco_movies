
## ♻️ MLOps

Passons maintenant aux processus d’automatisation. La formation suivie jusqu’à aujourd’hui nous a permis de découvrir de nombreux outils permettant d’assurer un déploiement en respectant plusieurs principes tels que l’isolation, l’automatisation et la reproductibilité. Maintenant, entre la théorie et la mise en œuvre concrète, structurée et si possible au plus proche de la réalité en entreprise, il va falloir travailler dur.

Voici les points que je dois prendre en considération pour la suite du projet :

- **Reproductibilité et versionnement →** Ceci implique que chaque expérimentation puisse être relancée dans les mêmes conditions. Il va ainsi falloir effectuer un contrôle de version rigoureux du code, des modèles et des environnements. Nous utiliserons **GitHub** pour le code et **MLflow** pour nos modèles.
- **Automatisation et CI/CD →** Nous allons automatiser les tests, la validation et le déploiement des modèles afin d’assurer une fiabilité et une rapidité de mise en production.
- **Orchestration des workflows avec Airflow →** L’utilisation d’**Apache Airflow** permettra de planifier, d’automatiser et de surveiller l’exécution de nos pipelines de données et de machine learning. Cela garantit une meilleure traçabilité, une gestion efficace des dépendances et une reprise facilitée en cas d’échec.
- **Isolation et portabilité avec Docker →** Grâce à **Docker**, chaque composant du projet (applications, modèles, scripts, etc.) sera encapsulé dans un conteneur. Cela assure une portabilité maximale entre les environnements de développement, de test et de production, tout en évitant les problèmes de compatibilité logicielle.
- **Déploiement et surveillance →** Nous intègrerons des outils de monitoring tels que **Prometheus** et **Grafana** afin d’avoir des alertes en cas de problème lié à nos modèles.

