import os
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

# Configure the path for the root directory to load configuration files if necessary
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from config import Config

# Configuration générale
NUTRISCORE_GRADES = ["a", "b", "c", "d", "e"]
COLS_TARGET = ['nutriscore_grade']



def load_and_prepare_data(df, target_column, feature_columns):
    """
    Charge et prépare les données en sélectionnant les colonnes de caractéristiques et en encodant les labels.

    Parameters:
    - df: DataFrame de la donnée
    - target_column: colonne cible pour le modèle.
    - feature_columns: colonnes utilisées comme caractéristiques.

    Returns:
    - features: DataFrame contenant les caractéristiques pré-traitées.
    - target: DataFrame contenant la cible.
    - label_encoder: L'encodeur de labels pour la colonne 'pnns_groups_1'.
    """

    # Préparation des caractéristiques et de la cible
    features = df[feature_columns].copy()
    label_encoder = LabelEncoder()
    features['pnns_groups_1'] = label_encoder.fit_transform(features['pnns_groups_1'])
    target = df[target_column].copy()

    return features, target, label_encoder


def train_random_forest(features, target):
    """
    Entraîne un modèle RandomForest avec les paramètres prédéfinis.

    Parameters:
    - features: DataFrame contenant les caractéristiques d'entraînement.
    - target: DataFrame contenant les labels pour l'entraînement.

    Returns:
    - rf_model: Modèle RandomForest entraîné.
    """
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2,
                                                                                random_state=42)

    rf_model = RandomForestClassifier(
        random_state=42,
        bootstrap=False,
        max_depth=10,
        min_samples_leaf=2,
        min_samples_split=5,
        n_estimators=100
    )

    rf_model.fit(features_train, target_train)
    return rf_model


def save_model_and_encoder(model, label_encoder, columns_fit, model_path="model.pkl", encoder_path="label_encoder.pkl", columns_path="columns.pkl"):
    """
    Sauvegarde le modèle et le label encoder dans des fichiers pickle.

    Parameters:
    - model: le modèle entraîné.
    - label_encoder: le label encoder utilisé.
    - model_path: chemin pour sauvegarder le modèle.
    - encoder_path: chemin pour sauvegarder le label encoder.
    """
    save_dir = os.path.join('app', 'ai-model')
    os.makedirs(save_dir, exist_ok=True)

    with open(os.path.join(save_dir, model_path), "wb") as file:
        pickle.dump(model, file)

    with open(os.path.join(save_dir, encoder_path), "wb") as file:
        pickle.dump(label_encoder, file)

    with open(os.path.join(save_dir, columns_path), "wb") as file:
        pickle.dump(columns_fit, file)
    print(f"Model saved to {model_path} and label encoder saved to {encoder_path}")


if __name__ == "__main__":
    # Définir les colonnes de caractéristiques
    df_output = pd.read_csv(Config.CLEANED_CSV_FULL_PATH, sep="\t", low_memory=False, on_bad_lines="skip")
    feature_columns = [col for col in df_output.columns if "_100g" in col or col == 'pnns_groups_1']

    # Charger et préparer les données
    features, target, label_encoder = load_and_prepare_data(df_output, COLS_TARGET, feature_columns)

    # Entraîner le modèle
    rf_model = train_random_forest(features, target)

    # Sauvegarder le modèle et le label encoder
    save_model_and_encoder(rf_model, label_encoder, feature_columns)
