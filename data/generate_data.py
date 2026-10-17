"""Génère un jeu de données synthétique de patients (patient_data.csv)."""
import csv
import os
import numpy as np

FEATURES = ["age", "temperature", "toux", "saturation_o2",
            "globules_blancs", "crp", "maux_de_tete", "contact_infecte"]


def generate(n=1000, seed=42, path=None):
    rng = np.random.default_rng(seed)
    infecte = rng.random(n) < 0.4                       # ~40 % de patients infectés

    age = np.clip(rng.normal(45, 18, n), 1, 95).round()
    temp = np.where(infecte, rng.normal(38.3, 0.7, n), rng.normal(36.9, 0.4, n))
    toux = (rng.random(n) < np.where(infecte, 0.75, 0.15)).astype(int)
    spo2 = np.clip(np.where(infecte, rng.normal(93, 3, n), rng.normal(97.5, 1.2, n)), 70, 100)
    gb = np.where(infecte, rng.normal(11.5, 3, n), rng.normal(7, 1.8, n))
    crp = np.clip(np.where(infecte, rng.normal(45, 25, n), rng.normal(5, 4, n)), 0, None)
    head = (rng.random(n) < np.where(infecte, 0.55, 0.2)).astype(int)
    contact = (rng.random(n) < np.where(infecte, 0.65, 0.1)).astype(int)

    rows = np.column_stack([age, temp, toux, spo2, gb, crp, head, contact]).round(2)
    # bruit d'étiquettes : 3 % d'erreurs de diagnostic
    label = infecte.copy()
    flip = rng.random(n) < 0.03
    label[flip] = ~label[flip]

    path = path or os.path.join(os.path.dirname(__file__), "patient_data.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(FEATURES + ["infecte"])
        for r, y in zip(rows, label):
            w.writerow(list(r) + [int(y)])
    return path


if __name__ == "__main__":
    print("Fichier créé :", generate())
