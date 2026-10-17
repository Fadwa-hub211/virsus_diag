from abc import ABC, abstractmethod

class BaseModel(ABC):

    @abstractmethod
    def fit(self, X, y):
        """Entraîne le modèle."""

    @abstractmethod
    def predict(self, X):
        """Retourne la probabilité d'infection (0 à 1) pour chaque ligne de X."""
