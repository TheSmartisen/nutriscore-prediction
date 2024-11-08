import os
import sys
import pandas as pd
from config import Config

# Configure the path for the root directory to load configuration files if necessary
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def load_data():
    return pd.read_csv(Config.CLEANED_CSV_FULL_PATH, sep="\t", low_memory=False, on_bad_lines="skip")