import json
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData, insert
from config import Config
import pandas as pd

def save_prediction(data, prediction, status_code=200):
    try:
        engine = create_engine(Config.DATABASE_URL)
        metadata = MetaData()
        logs_request = Table('logs_request', metadata, autoload_with=engine)
        
        log_entry = {
            "timestamp": datetime.now(),
            "params": json.dumps(data),
            "predicted_score": prediction,
            "status_code": status_code
        }
        
        with engine.connect() as connection:
            connection.execute(insert(logs_request).values(log_entry))
        print("Enregistrement réussi dans logs_request.")
    
    except Exception as e:
        print("Erreur lors de l'enregistrement dans logs_request :")
        print(e)