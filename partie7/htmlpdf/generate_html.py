from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from data_utils import load_reservations

pa = Path("../../data") / "systeme.json"

df = load_reservations(pa)

# Préparer l’environnement Jinja
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.htmlpdf")

# Générer le rendu HTML
html_out = template.render(rows=df.to_dict(orient="records"))

# Écriture dans un fichier
with open("reservations.html", "w", encoding="utf-8") as f:
    f.write(html_out)
