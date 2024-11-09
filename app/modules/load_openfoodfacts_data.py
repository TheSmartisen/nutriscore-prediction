import os, sys
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Charger la base de données
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Chemin du fichier CSV monté dans le conteneur
csv_file_path = "/data/openfoodfact_clean.csv"

def load_data():
    # Lire le CSV
    df = pd.read_csv(csv_file_path, sep="\t", low_memory=False, on_bad_lines="skip")

    # Renommer les colonnes pour correspondre aux noms de la table SQL si nécessaire
    df.columns = [
        "code", "url", "product_name", "quantity", "brands", "categories",
        "countries_en", "nutriscore_score", "nutriscore_grade", "image_url",
        "pnns_groups_1", "pnns_groups_2", "fat_100g", "saturated_fat_100g",
        "trans_fat_100g", "cholesterol_100g", "carbohydrates_100g", 
        "sugars_100g", "fiber_100g", "proteins_100g", "salt_100g", 
        "sodium_100g", "calcium_100g", "iron_100g",
        "fruits_vegetables_nuts_estimate_from_ingredients_100g", "energy_100g"
    ]

    # Insérer les données dans la table `products`
    df.to_sql('products', engine, if_exists='append', index=False)
    print("Les données ont été insérées dans la table `products`.")

if __name__ == "__main__":
    load_data()
