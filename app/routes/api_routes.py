from flask import Blueprint, request, jsonify
from app.modules.do_log import  save_prediction
from config import Config
import pandas as pd
import os, pickle

# Define the blueprint for the API
api_bp = Blueprint('api_bp', __name__)

# Load your model
# Checks if the model exists
if os.path.exists(Config.MODEL_PATH):
    # Charger le modèle et le LabelEncoder
    with open(Config.MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)

    with open("app/ai-model/label_encoder.pkl", "rb") as encoder_file:
        label_encoder = pickle.load(encoder_file)

    with open("app/ai-model/columns.pkl", "rb") as encoder_file:
        columns_fit = pickle.load(encoder_file)

@api_bp.route('/api/v1/predict-nutriscore', methods=['POST'])
def predict_nutriscore():
    try:
        # Extraire les données d'entrée JSON
        data = request.json
        df = pd.DataFrame([data])  # Convertir en DataFrame

        # Assurer la présence de 'pnns_groups_1' dans les données d'entrée
        if 'pnns_groups_1' in df.columns:
            # Encoder la colonne 'pnns_groups_1'
            df['pnns_groups_1'] = label_encoder.transform(df['pnns_groups_1'])

        # Filtrer les colonnes d'entrée pour correspondre aux caractéristiques du modèle
        input_features = columns_fit
        df = df[input_features]

        # Faire une prédiction
        prediction = model.predict(df)
        save_prediction(df, prediction[0])
        # Retourner la prédiction sous forme de JSON
        return jsonify({"prediction": prediction[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500