from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from core.logistic_regression import LogisticRegression
from pipeline.trainer import Trainer
from pipeline.predictor import ClinicalPredictor


class PatientData(BaseModel):
    temperature: float
    cough: int
    fatigue: int
    biological_rate: float


class ClinicalAPI:

    def __init__(self):
        self.app = FastAPI(title="Diagnostic viral")

        trainer = Trainer(
            LogisticRegression(),
            "data/patient_data.csv"
        )

        model, _, _ = trainer.train()
        self.predictor = ClinicalPredictor(model)

        self.app.post("/diagnose")(self.diagnose)

    def diagnose(self, patient: PatientData):
        data = pd.DataFrame([patient.model_dump()])
        result = self.predictor.diagnose(data)

        return {"diagnostic": result}


clinical_api = ClinicalAPI()
app = clinical_api.app