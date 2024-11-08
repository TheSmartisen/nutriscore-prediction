from flask import Blueprint, render_template, current_app
from app.modules.forms import NutriScoreForm
from app.modules.explore_data import load_data

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def predict():
    """
    Renders the NutriScore prediction form.
    This function initializes the prediction form and provides the pnns_groups_1 choices.
    """

    # Check if the dataframe is already loaded
    if 'PRODUCTS_DF' not in current_app.config:
        current_app.config['PRODUCTS_DF'] = load_data()

    # Get the DataFrame from the app config
    products = current_app.config['PRODUCTS_DF']
    pnns_groups_list = sorted(products['pnns_groups_1'].dropna().unique())

    # Initialize the form
    form = NutriScoreForm()
    form.pnns_groups_1.choices = [(group, group) for group in pnns_groups_list]

    # Render the form template without prediction logic
    return render_template('prediction_form.html', form=form, pnns_groups_list=pnns_groups_list)
