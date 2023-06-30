# Programmation Orientée Objet

Le projet actuel utilise la programmation orientée objet (POO), une approche de développement logiciel qui permet de structurer le code autour d'objets qui interagissent les uns avec les autres. La POO offre de nombreux avantages, tels que la modularité, l'encapsulation des données, la réutilisabilité du code et la facilité de maintenance.

## Le Polymorphisme
Le polymorphisme en POO vous permet donc de concevoir un code plus flexible, extensible et réutilisable en exploitant les relations d'héritage entre les classes et en utilisant des méthodes polymorphes pour manipuler des objets de manière uniforme.

Polymorphisme lors de l'initialisation des manipulateurs : Dans la classe Engine, j'utilise le polymorphisme pour initialiser les manipulateurs en fonction des options choisies. J'ai une méthode initialize_manipulators() qui crée différentes instances de manipulateurs en fonction des options spécifiées. Chaque manipulateur peut avoir une implémentation différente des méthodes communes telles que manipulate(), permettant ainsi une manipulation spécifique des mots.

[Lien vers le code :](https://github.com/altib1/Python/blob/main/engine.py)

Sur le fichier CapitalizeCaseWord :

[Lien vers le code :](https://github.com/altib1/Python/blob/main/Options/CapitalizeCaseWord.py)

## Encapsulation

L'encapsulation est un mécanisme de la programmation orientée objet qui permet de regrouper des données et des méthodes qui agissent sur ces données au sein d'une même entité appelée classe. L'encapsulation permet de cacher les détails internes de la classe et de restreindre l'accès direct aux données, en fournissant des méthodes publiques pour interagir avec les attributs de la classe de manière contrôlée.

dans la classe Engine, j'ai encapsulé les listes words, results, manipulators, etc., ainsi que les méthodes initialize_manipulators(), run(), get_date_variations(), etc. Cela permet de cacher les détails internes de la classe Engine et de ne donner accès qu'aux méthodes publiques nécessaires pour interagir avec l'objet Engine.

[Lien vers le code :](https://github.com/altib1/Python/blob/main/engine.py)

## Composition

La composition est un mécanisme de la programmation orientée objet qui permet de construire des objets complexes en combinant plusieurs autres objets. Elle établit une relation "a un" ou "contient" entre les objets, où un objet est composé d'un ou plusieurs autres objets. Le conteneur contrôle le cycle de vie des objets contenus, qui ne peuvent pas exister indépendamment du conteneur.

Dans la classe Engine, j'ai une relation de composition avec les classes GetLeetMin, GetLeetMaj, LowerCaseWord, etc. J'ai crée une instance de chaque classe manipulatrice à l'intérieur de la classe Engine et utilisez ces instances pour effectuer les manipulations nécessaires.

[Lien vers le code :](https://github.com/altib1/Python/blob/main/engine.py)

## Héritage

L'héritage est un mécanisme de la programmation orientée objet qui permet de créer de nouvelles classes en se basant sur des classes existantes, appelées classes parentes ou classes de base. Les classes dérivées héritent des attributs et méthodes de leurs classes parentes, ce qui leur permet d'étendre ou de spécialiser leur comportement. Les classes dérivées peuvent ajouter de nouveaux attributs et méthodes, ou redéfinir ceux hérités de la classe parente.

Dans le projet, j'ai utilisé l'héritage pour créer des classes dérivées à partir de classes existantes. Par exemple, j'ai créé la classe GetLeetMin en héritant de la classe de base WordManipulator. La classe GetLeetMin hérite ainsi des attributs et méthodes de la classe WordManipulator et peut les utiliser ou les redéfinir selon ses besoins.

WordManipulator:
[Lien vers le parent :](https://github.com/altib1/Python/blob/main/Options/WordManipulator.py)
GetLeetMin:
[Lien vers le parent :](https://github.com/altib1/Python/blob/main/Options/GetLeetMin.py)

## Interface

Une interface est une spécification d'un ensemble de méthodes qu'une classe doit implémenter. Elle définit un contrat ou un comportement commun que les classes peuvent adopter. Les interfaces sont utilisées pour définir des fonctionnalités communes sans spécifier comment elles doivent être mises en œuvre. Une classe peut implémenter une ou plusieurs interfaces, ce qui lui permet d'adopter le comportement spécifié par ces interfaces.

J'ai ajoutée un une interface sur WordManipulator qui définit la mathode a utiliséer.
WordManipulator:
[Lien vers le code :](https://github.com/altib1/Python/blob/main/Options/WordManipulator.py)
L'interface: 
[Lien vers le code :](https://github.com/altib1/Python/blob/main/Options/ManipulatorInterface.py)

## Méthodes et attributs d'objets

Les attributs d'objets sont des variables définies à l'intérieur d'une classe qui représentent les caractéristiques ou les données de l'objet. Chaque instance de la classe possède ses propres valeurs d'attributs, ce qui leur donne une identité unique. Les attributs permettent de stocker et de manipuler des informations associées à l'objet.

[Lien vers méthode d'objet :](https://github.com/altib1/Python/blob/main/engine.py) 

## Méthodes et attributs statiques

Les méthodes statiques sont des méthodes définies au niveau de la classe plutôt qu'au niveau de l'instance. Elles sont liées à la classe elle-même plutôt qu'à une instance spécifique. Les attributs statiques sont des attributs qui appartiennent à la classe elle-même plutôt qu'à une instance particulière de la classe.

J'ai mis en place une méthode statique sur GetLeetMaj
[Lien vers méthode statique :](https://github.com/altib1/Python/blob/main/Options/GetLeetMaj.py)


## Méthodes et attributs de classe

La définition des méthodes et attributs de classe est la suivante :

Méthodes de classe :
Les méthodes de classe sont des méthodes qui sont définies au niveau de la classe et non au niveau de l'instance. Elles sont décorées avec le décorateur @classmethod et prennent la classe elle-même (cls) comme premier paramètre plutôt que l'instance (self). Les méthodes de classe peuvent être utilisées pour effectuer des opérations qui concernent la classe dans son ensemble, plutôt que des opérations spécifiques à une instance particulière.

Attributs de classe :
Les attributs de classe sont des variables définies au niveau de la classe et partagées par toutes les instances de cette classe. Ils sont définis en dehors des méthodes et peuvent être accédés via la classe elle-même (NomDeClasse.attribut) ou via une instance de la classe (instance.attribut). Les attributs de classe peuvent être utilisés pour stocker des valeurs communes à toutes les instances de la classe ou pour définir des constantes spécifiques à la classe.

[Lien vers méthode de classe :](https://github.com/altib1/Python/blob/main/engine.py)


