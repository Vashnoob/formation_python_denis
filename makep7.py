from pathlib import Path

# Création de la structure de projet dans un dossier projet8
project_root = Path("projet8")
structure = {
    "projet8/__init__.py": "",
    "projet8/models/__init__.py": "",
    "projet8/models/trajet.py": "",  # sera rempli avec la version actuelle améliorée
    "projet8/models/trajet_express.py": "",
    "projet8/models/utilisateur.py": "",
    "projet8/services/__init__.py": "",
    "projet8/services/persistence.py": "",  # pour gestion fichiers JSON + datetime
    "projet8/services/logger.py": "",       # module logging
    "projet8/data/.gitkeep": "",            # dossier pour fichiers persistants
    "projet8/logs/.gitkeep": "",            # dossier pour logs
    "projet8/main.py": "",                  # point d'entrée
    "pyproject.toml": """
[project]
name = "projet8"
version = "0.1.0"
description = "Système de gestion de trajets et réservations (exercice pédagogique)"
authors = [{name = "Formateur Python"}]
dependencies = []
requires-python = ">=3.8"

[tool.setuptools.packages.find]
where = ["projet8"]
"""
}

# Création des fichiers et dossiers
created_files = []
for relative_path, content in structure.items():
    file_path = Path(".") / relative_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content,encoding='utf-8')
    created_files.append(file_path)

