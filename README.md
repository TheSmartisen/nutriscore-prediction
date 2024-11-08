```markdown
# Projet NutriScore Prediction

Ce projet est une application Flask conçue pour prédire le NutriScore d'aliments en se basant sur des données nutritionnelles. Il inclut un modèle d'IA entraîné pour classer les aliments selon leur score nutritionnel, des routes API, et une interface utilisateur web.

## Structure du projet

- `config.py` : fichier de configuration de l'application.
- `requirements.txt` : dépendances nécessaires pour exécuter l'application.
- `run.py` : script principal pour lancer l'application.
- `app/` : répertoire principal de l'application contenant les modules suivants :
  - `ai-model/` : contient le modèle ML (`model.pkl`), les encodages des colonnes et le label encoder.
  - `modules/` : contient les modules Python pour la création de l'IA, le logging et l'exploration des données.
  - `notebook/` : inclut un notebook pour l'exploration initiale des données (`Notebook - NutriScore.ipynb`).
  - `routes/` : contient les routes Flask (`api_routes.py` pour les API, `main_routes.py` pour les routes de base).
  - `static/` : contient les ressources statiques (images, icônes).
  - `templates/` : fichiers HTML pour le rendu des pages (`base.html`, `prediction_form.html`).
- `tests/` : contient les tests unitaires pour les modèles d'IA et les routes de l'application.

## Installation

1. Clonez le dépôt et accédez au répertoire :
   ```bash
   git clone <URL_DU_DEPOT>
   cd nom_du_projet
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application :
   ```bash
   python run.py
   ```

2. Accédez à l'interface utilisateur via `http://localhost:5000`.

## Tests

Pour exécuter les tests, utilisez la commande suivante :
```bash
python -m unittest discover -s tests
```

## Auteur

Développé par Patrick.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
```

Ce `README.md` donne un aperçu clair du projet, des étapes d'installation, d'utilisation et des tests, tout en mentionnant les principaux fichiers et répertoires. N'hésitez pas à adapter les descriptions en fonction de vos besoins !