import os
import joblib
import mlflow
import numpy as np
import pandas as pd
import mlflow.sklearn
from pathlib import Path
from urllib.parse import urlparse
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.data_science.entity.config_entity import ModelEvaluationConfig
from src.data_science.utils.common import save_json

os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/saibhavadeesh/data_science_project.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'saibhavadeesh'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '168a072a928c94440c3e0ade0a3b6eba20bb5b8d'

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        # Load the test data
        test_data = pd.read_csv(self.config.test_data_path)
        X_test = test_data.drop(columns=[self.config.target_column])
        y_test = test_data[self.config.target_column]

        # Load the model
        model = joblib.load(self.config.model_path)

        # Make predictions
        y_pred = model.predict(X_test)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(X_test)
            (rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)

            # Saving the metrics to a JSON file
            metrics = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metrics_file_path), data=metrics)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Model registry doesnot work with file store
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="ElasticNetModel"
                )
            else:
                mlflow.sklearn.log_model(model, "model")
