
# Nutri-Score Prediction Project

Ce projet permet de prédire le Nutri-Score d'un produit alimentaire en fonction de ses informations nutritionnelles. Il fournit une interface utilisateur pour entrer les informations du produit et voir le Nutri-Score prédit. Le projet inclut également une API pour effectuer des prédictions de Nutri-Score.

## Fonctionnalités

- **Formulaire de prédiction** : Entrer les informations nutritionnelles pour obtenir un Nutri-Score prédit.
- **Affichage du résultat** : Voir le Nutri-Score sous forme d'image et de texte.
- **API de prédiction** : Faire des prédictions via une requête API.

## Capture d'écran

### Formulaire de prédiction

![Formulaire de prédiction](app/static/images/screenshot-form.PNG)

### Résultat de prédiction

![Résultat de prédiction](app/static/images/screenshot-result.PNG)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone git@github.com:TheSmartisen/nutriscore-prediction.git
   cd nutriscore-prediction
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Exécutez l'application :

   ```bash
   python run.py
   ```

## Utilisation

Accédez à `http://localhost:5000` dans votre navigateur pour utiliser l'interface utilisateur et prédire un Nutri-Score.

### API

L'API de prédiction est disponible à l'URL suivante :

**Endpoint** : `/api/v1/predict-nutriscore`

**Méthode** : `POST`

**Données d'entrée** (JSON) :
```json
{
    "pnns_groups_1": "Beverages",
    "energy_100g": 42.0,
    "fat_100g": 0.0,
    "saturated_fat_100g": 0.0,
    "trans_fat_100g": 0.0,
    "cholesterol_100g": 0.0,
    "carbohydrates_100g": 10.6,
    "sugars_100g": 10.6,
    "fiber_100g": 0.0,
    "proteins_100g": 0.0,
    "salt_100g": 0.01,
    "sodium_100g": 0.004,
    "calcium_100g": 0.0,
    "iron_100g": 0.0,
    "fruits_vegetables_nuts_estimate_from_ingredients_100g": 0.0
}
```

**Exemple de réponse** :
```json
{
    "predicted_score": "B"
}
```

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
