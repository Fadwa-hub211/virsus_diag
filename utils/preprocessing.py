
import pandas as pd


class Preprocessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)

        # Vérifier les colonnes nécessaires
        features = [
            "age",
            "temperature",
            "toux",
            "saturation_o2",
            "globules_blancs",
            "crp",
            "maux_de_tete",
            "contact_infecte"
        ]

        target = "infecte"

        missing_columns = [
            col for col in features + [target]
            if col not in data.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Colonnes absentes du dataset : {missing_columns}"
            )

        X = data[features]
        y = data[target]

        return X, y
