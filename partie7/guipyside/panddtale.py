import dtale

from pathlib import Path
from utilitaires.data_utils import load_reservations

pa = Path("../../data") / "systeme.json"

df = load_reservations(pa)



dtale.show(df)
