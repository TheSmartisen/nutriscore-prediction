# Nutriscore Prediction Project

Ce projet est une application Flask qui permet de faire des prédictions de Nutri-Score et de stocker les résultats en base de données PostgreSQL. Il utilise Docker pour faciliter l’installation et le déploiement.

## Prérequis

- [Docker](https://www.docker.com/get-started) et [Docker Compose](https://docs.docker.com/compose/install/) installés
- Connaissances de base en Python et SQL

## Installation

### 1. Cloner le dépôt

Clonez ce projet sur votre machine :

```bash
git clone https://github.com/TheSmartisen/nutriscore-prediction.git
cd nutriscore-prediction
```

### 2. Configurer les Variables d’Environnement

Créez un fichier `.env` à la racine du projet avec les informations suivantes :

```env
POSTGRES_USER=monutilisateur
POSTGRES_PASSWORD=monmotdepasse
POSTGRES_DB=ma_base_de_donnees
DATABASE_URL=postgresql://monutilisateur:monmotdepasse@db:5432/ma_base_de_donnees
```

Assurez-vous que le fichier `.env` est ajouté dans le `.gitignore` pour protéger les informations sensibles.

### 3. Lancer les Conteneurs

Pour démarrer les conteneurs (Flask, PostgreSQL), exécutez la commande suivante :

```bash
docker-compose up --build
```

Cette commande crée et lance les conteneurs définis dans le fichier `docker-compose.yml`.

### 4. Création des Tables dans PostgreSQL

Une fois les conteneurs lancés, suivez ces étapes pour créer les tables nécessaires dans PostgreSQL.

#### a. Connexion à PostgreSQL dans le Conteneur

Connectez-vous au conteneur PostgreSQL avec :

```bash
docker exec -it postgres_db psql -U $POSTGRES_USER -d $POSTGRES_DB
```

#### b. Création des Tables

Dans le client PostgreSQL, exécutez les commandes suivantes pour créer les tables `products` et `logs_request` :

```sql
CREATE TABLE products (
    code BIGINT PRIMARY KEY,
    url TEXT,
    product_name VARCHAR(255),
    quantity VARCHAR(50),
    brands VARCHAR(255),
    categories TEXT,
    countries_en VARCHAR(255),
    nutriscore_score NUMERIC,
    nutriscore_grade CHAR(1),
    image_url TEXT,
    pnns_groups_1 VARCHAR(100),
    pnns_groups_2 VARCHAR(100),
    fat_100g NUMERIC,
    saturated_fat_100g NUMERIC,
    trans_fat_100g NUMERIC,
    cholesterol_100g NUMERIC,
    carbohydrates_100g NUMERIC,
    sugars_100g NUMERIC,
    fiber_100g NUMERIC,
    proteins_100g NUMERIC,
    salt_100g NUMERIC,
    sodium_100g NUMERIC,
    calcium_100g NUMERIC,
    iron_100g NUMERIC,
    fruits_vegetables_nuts_estimate_from_ingredients_100g NUMERIC,
    energy_100g NUMERIC
);

CREATE TABLE logs_request (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    params JSONB,
    predicted_score VARCHAR(10),
    status_code INT
);
```

#### c. Quitter le Client PostgreSQL

Tapez `\q` pour quitter le client PostgreSQL.

### 5. Initialiser la Base de Données avec des Données Initiales

Si le projet nécessite de charger un fichier de données initial comme `openfoodfacts_clean.csv`, exécutez le script correspondant dans le conteneur Flask pour charger les données :

```bash
docker exec -it flask_app python app/modules/load_openfoodfacts_data.py
```

### 6. Tester l’API

Pour tester que l’application fonctionne correctement, vous pouvez envoyer une requête à l'API de prédiction.

Exemple de requête (remplacez les paramètres `param1` et `param2` par ceux attendus par l’API) :

```bash
curl -X POST http://localhost:5000/api/v1/predict -H "Content-Type: application/json" -d '{"param1": "value1", "param2": "value2"}'
```

### Dépannage

- **Erreur de connexion à PostgreSQL** : Assurez-vous que le conteneur PostgreSQL est en cours d’exécution et que les informations dans `.env` sont correctes.
- **Erreur de montage de volume** : Vérifiez que les dossiers sont correctement montés dans `docker-compose.yml`, surtout si vous avez du mal à accéder au fichier `openfoodfacts_clean.csv`.

### Résumé

Ce projet utilise Flask, PostgreSQL, et Docker pour fournir une application de prédiction de Nutri-Score. Les instructions ci-dessus permettent de configurer et démarrer l'application, de créer les tables dans PostgreSQL et de charger les données initiales.
