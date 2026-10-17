
import os
import pandas as pd
from sklearn.model_selection import train_test_split

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_PATH = os.path.join(BASE_DIR, "data", "patient_data.csv")

FEATURES = ["age", "temperature", "toux", "saturation_o2",
            "globules_blancs", "crp", "maux_de_tete", "contact_infecte"]
TARGET = "infecte"


class Dataset:
    def __init__(self, path=DEFAULT_PATH, features=None, target=TARGET):
        self.path = path
        self.features = features or FEATURES
        self.target = target
        self.data = None

    def load(self):
        """Lit le CSV, supprime les doublons et les lignes incomplètes."""
        self.data = pd.read_csv(self.path).drop_duplicates().dropna()
        return self

    def get_xy(self):
        """Retourne X et y."""
        return self.data[self.features].values, self.data[self.target].values

    def split(self, test_size=0.2, seed=42):
        """Retourne (X_train, X_test, y_train, y_test)."""
        X, y = self.get_xy()
        return train_test_split(X, y, test_size=test_size,
                                random_state=seed, stratify=y)

    def __len__(self):
        return len(self.data)


if __name__ == "__main__":
    ds = Dataset().load()
    X_train, X_test, y_train, y_test = ds.split()
    print(f"{len(ds)} patients | train={len(X_train)} | test={len(X_test)}")
    print(f"Taux d'infection : {y_train.mean():.2%}")