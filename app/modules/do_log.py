import os
import pandas as pd
from datetime import datetime


def save_prediction(data, prediction):
    """Enregistre les prédictions et les données dans un fichier CSV."""
    save_path = os.getenv("DATA_PATH", os.path.join("data", "requests"))
    os.makedirs(save_path, exist_ok=True)

    # Créer un DataFrame pour la requête et ajouter la prédiction
    df = data
    df['prediction'] = prediction
    df['timestamp'] = datetime.now()

    # Sauvegarder dans un fichier CSV
    file_path = os.path.join(save_path, 'predictions.csv')
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)