from flask import Blueprint, render_template, current_app
from config import Config
from app.modules.forms import NutriScoreForm
from app.modules.explore_data import load_data
from app.modules.do_log import save_prediction
import os
import pickle
import pandas as pd

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def predict():
    """
    Handles requests to predict the Nutri-Score for a product based on its nutritional information.

    This function checks if the required data and model components are loaded in the application
    configuration. If not, it loads them. It then initializes the prediction form and handles form
    submissions to predict the Nutri-Score of a product using a trained machine learning model.

    Returns:
        Renders the prediction form template with the form object and predicted score.
    """

    # Check if the dataframe is already loaded
    if 'PRODUCTS_DF' not in current_app.config:
        current_app.config['PRODUCTS_DF'] = load_data()

    # Get the DataFrame from the app config
    products = current_app.config['PRODUCTS_DF']
    pnns_groups_list = sorted(products['pnns_groups_1'].dropna().unique())

    # Paths for model and encoder files
    model_path = os.path.join('app', 'ai-model', 'model.pkl')
    label_encoder_path = os.path.join('app', 'ai-model', 'label_encoder_pnns.pkl')
    columns_path = os.path.join('app', 'ai-model', 'columns.pkl')  # Add path for columns order

    # Check if model and scaler exist, otherwise train and save the model
    if os.path.exists(Config.MODEL_PATH):
        # Charger le modèle et le LabelEncoder
        with open(Config.MODEL_PATH, "rb") as model_file:
            model = pickle.load(model_file)

        with open("app/ai-model/label_encoder.pkl", "rb") as encoder_file:
            label_encoder = pickle.load(encoder_file)

        with open("app/ai-model/columns.pkl", "rb") as encoder_file:
            columns_order = pickle.load(encoder_file)

    # Initialize the form
    form = NutriScoreForm()
    form.pnns_groups_1.choices = [(group, group) for group in pnns_groups_list]

    # Initialize the predicted score
    predicted_score = None

    # Handle form submission
    if form.validate_on_submit():
        try:
            # Collect form data into a DataFrame
            input_data = {
                "pnns_groups_1": label_encoder.transform([form.pnns_groups_1.data])[0],
                "energy_100g": float(form.energy_100g.data),
                "fat_100g": float(form.fat_100g.data),
                "saturated-fat_100g": float(form.saturated_fat_100g.data),
                "trans-fat_100g": float(form.trans_fat_100g.data),
                "cholesterol_100g": float(form.cholesterol_100g.data),
                "carbohydrates_100g": float(form.carbohydrates_100g.data),
                "sugars_100g": float(form.sugars_100g.data),
                "fiber_100g": float(form.fiber_100g.data),
                "proteins_100g": float(form.proteins_100g.data),
                "salt_100g": float(form.salt_100g.data),
                "sodium_100g": float(form.sodium_100g.data),
                "calcium_100g": float(form.calcium_100g.data),
                "iron_100g": float(form.iron_100g.data),
                "fruits-vegetables-nuts-estimate-from-ingredients_100g": float(
                    form.fruits_vegetables_nuts_estimate_from_ingredients_100g.data),
            }

            # Create DataFrame and ensure it follows the columns order
            input_df = pd.DataFrame([input_data])
            input_df = input_df.reindex(columns=columns_order)  # Ensure the correct order of columns

            # Cast to appropriate data types
            input_df = input_df.astype({
                "pnns_groups_1": 'int64',
                "energy_100g": 'float64',
                "fat_100g": 'float64',
                "saturated-fat_100g": 'float64',
                "trans-fat_100g": 'float64',
                "cholesterol_100g": 'float64',
                "carbohydrates_100g": 'float64',
                "sugars_100g": 'float64',
                "fiber_100g": 'float64',
                "proteins_100g": 'float64',
                "salt_100g": 'float64',
                "sodium_100g": 'float64',
                "calcium_100g": 'float64',
                "iron_100g": 'float64',
                "fruits-vegetables-nuts-estimate-from-ingredients_100g": 'float64',
            })


            # Predict the Nutri-Score
            prediction = model.predict(input_df)
            predicted_score = prediction[0]
            save_prediction(input_df, prediction[0])
        except Exception as e:
            # Print error and set the predicted score to error message
            print(f"Error during prediction: {e}")
            predicted_score = "Error"

    return render_template('prediction_form.html', form=form, pnns_groups_list=pnns_groups_list,
                           predicted_score=predicted_score)
# Loading Data Route

