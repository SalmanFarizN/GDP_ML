from src.model import model_fit
import pandas as pd
import joblib

df = pd.read_csv("data/global_development_data.csv")
model = model_fit(df)

# Save the model in models directory
joblib.dump(model, "models/RF_gdp_model.pkl")
