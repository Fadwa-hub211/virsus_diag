
import pandas as pd


class ClinicalInterface:
    def __init__(self, predictor):
        self.predictor = predictor

    def run(self):
        print("\n=== Diagnostic viral ===")

        age = float(input("Âge : "))
        temperature = float(input("Température : "))
        toux = int(input("Toux (1=oui, 0=non) : "))
        saturation_o2 = float(input("Saturation O2 : "))
        globules_blancs = float(input("Globules blancs : "))
        crp = float(input("CRP : "))
        maux_de_tete = int(input("Maux de tête (1=oui, 0=non) : "))
        contact_infecte = int(
            input("Contact avec une personne infectée (1=oui, 0=non) : ")
        )

        patient_data = pd.DataFrame([{
            "age": age,
            "temperature": temperature,
            "toux": toux,
            "saturation_o2": saturation_o2,
            "globules_blancs": globules_blancs,
            "crp": crp,
            "maux_de_tete": maux_de_tete,
            "contact_infecte": contact_infecte
        }])

        result = self.predictor.diagnose(patient_data)

        print("\nRésultat du modèle :", result)
        print("Attention : résultat pédagogique, non médicalement validé.")
