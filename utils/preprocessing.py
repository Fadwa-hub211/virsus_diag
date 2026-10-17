from sklearn.preprocessing import StandardScaler   # fonction déjà définie (scikit-learn)


class Preprocessor:
<<<<<<< HEAD
    """Prétraitement des données : nettoyage et normalisation."""
=======
>>>>>>> fa43aba (version 2)

    def __init__(self):
        self.scaler = StandardScaler()

    @staticmethod
    def clean(df):
        """Supprime les doublons et les lignes avec valeurs manquantes."""
        return df.drop_duplicates().dropna()

    def fit(self, X):
        """Apprend la moyenne et l'écart-type (sur le train uniquement)."""
        self.scaler.fit(X)
        return self

    def transform(self, X):
        """Normalise X (moyenne 0, écart-type 1)."""
        return self.scaler.transform(X)

    def fit_transform(self, X):
<<<<<<< HEAD
        return self.fit(X).transform(X)
=======
        return self.fit(X).transform(X)
>>>>>>> fa43aba (version 2)
