---
hide:
  - feedback
---

## **📝 Introduction**

Plus les semaines d’apprentissage passent, plus le plaisir et l’envie d’en apprendre davantage inondent mon esprit. Et quoi de mieux pour apprendre qu’un projet? J’ai décidé de ne pas poursuivre celui choisi lors de ma formation de Data Scientist, à savoir l’exploration des approches multimodales de classification. Je souhaitais enrichir mes connaissances en m’intéressant cette fois-ci aux systèmes de recommandation. Il m’apparaissait essentiel de comprendre et d’analyser scientifiquement comment les différentes plateformes parviennent, grâce à nos données, à orienter nos choix.

## **🚩 Les systèmes de Recommandation**

DataScientest nous propose de travailler sur un système de recommandation de films. Le but est simple : proposer à l’utilisateur LE film qui va lui plaire, mais comment y parvenir? Une relecture des modules appris lors de ma précédente formation, m’amène à réfléchir aux 3 manières suivantes:

1. **Filtrage collaboratif →** L’idée ? Si des utilisateurs ayant des goûts proches du vôtre ont aimé un film que vous n’avez pas encore vu, il y a des chances que vous l’aimiez aussi. On peut faire ça de façon très simple, en cherchant les « voisins » les plus proches (méthode des k plus proches voisins), ou de façon plus avancée, avec des techniques comme la factorisation de matrice, qui permet de prédire les notes manquantes dans une grande matrice utilisateurs-films.
2. **Filtrage basé sur le contenu →** Ici, on s’intéresse surtout aux caractéristiques des films : genre, acteurs, réalisateur, résumé, etc. Si vous avez aimé plusieurs thrillers avec un certain acteur, le système va naturellement vous proposer des films similaires. C’est une approche très utile quand on a peu d’informations sur l’utilisateur, ou pour éviter le fameux « démarrage à froid »
3. **Approches hybrides →** Le projet Rakuten nous a déjà montré que les formats hybrides sont souvent performants. On va donc naturellement essayer de combiner le filtrage collaboratif et filtrage basé sur le contenu, pour profiter des forces de chacun. Par exemple, on peut d’abord filtrer les films par genre, puis affiner la sélection grâce aux préférences d’utilisateurs similaires

## 🗃️ Les données:

Nous utiliserons les données provenant du site MovieLens. Voici les éléments importants concernant nos données:

- **Volume et richesse** : Plus de 20 millions de notes et près de 500 000 tags sur plus de 27 000 films, provenant de près de 140 000 utilisateurs.
- **Sélection des utilisateurs** : Tous les utilisateurs ont noté au moins 20 films, ce qui garantit une certaine densité d’interactions.
- **Anonymat et absence de démographie** : Les utilisateurs sont anonymes, et aucune donnée démographique n’est fournie.
- **Structure des données** : Les informations sont réparties dans plusieurs fichiers (évaluations, tags, films, liens, scores de tags).
- **Tag Genome** : Présence d’un système avancé de tags, permettant d’analyser en profondeur les caractéristiques des films.
- **Vérification de l’intégrité** : Possibilité de vérifier que les fichiers téléchargés sont intacts grâce à des sommes de contrôle MD5.
