from pandasgui import show

from pathlib import Path
from utilitaires.data_utils import load_reservations

pa = Path("reservations.json")

df = load_reservations(pa)

import plotly.express as px
from pandasgui import show

show(df)
