import pandas as pd
from sqlalchemy import create_engine
from config import Config

def load_data():
    engine = create_engine(Config.DATABASE_URL)
    query = "SELECT * FROM products"
    return pd.read_sql(query, engine)
