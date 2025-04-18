## R & Python
Faire collaborer **R** (via RStudio ou Rscript) 
et **Python** (via Jupyter, scripts ou notebooks) est courant en data science. Il existe plusieurs moyens 
d'interopérabilité dans **les deux sens**, en fonction du contexte (analyse, visualisation, automatisation, 
pipeline, etc.).
---

### 🔁 **Intégration de R dans Python**

#### 1. **Utiliser `rpy2`**
- C’est l'outil le plus connu pour exécuter du code R depuis Python.
- Permet d’appeler des fonctions R, charger des packages R, manipuler des objets `pandas` ↔ `data.frame`.

```python
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri

pandas2ri.activate()
ro.r('summary(cars)')  # Exécution de code R
```

#### 2. **Cellule magique R dans Jupyter**
- Avec `ipython` et `rpy2`, on peut mélanger R et Python dans un notebook :
```python
%load_ext rpy2.ipython

%%R
plot(cars)
```

#### 3. **Appel d’un script R via `subprocess`**
- Méthode bas niveau mais robuste.

```python
import subprocess
subprocess.run(["Rscript", "mon_script.R"])
```

---

### 🔁 **Intégration de Python dans R**

#### 1. **Utiliser `reticulate`**
- Le package R `reticulate` permet d’utiliser Python comme s’il était natif dans R.
- Conversion automatique des objets `data.frame` ↔ `pandas`, accès aux packages Python.

```R
library(reticulate)
py_run_string("import numpy as np; x = np.array([1,2,3])")
py$x
```

#### 2. **Cellules Python dans R Markdown**
- Utilisation de blocs Python dans un rapport `.Rmd` :
```markdown
```{python}
import pandas as pd
pd.DataFrame({'a': [1,2], 'b':[3,4]})
```
```

#### 3. **Appel de scripts Python depuis R**
```R
system("python3 mon_script.py")
```

---

### 📦 **Interopérabilité des formats**
- Sauvegarde en CSV, Feather, Parquet, JSON : lecture facile des deux côtés.
- Utilisation commune de **Arrow** pour performances + compatibilité.
- Conversion via **HDF5**, **SQLite**, ou **DuckDB** aussi très performante.

---

### 🔄 **Dans un pipeline automatisé**
- Airflow, Luigi ou Snakemake peuvent gérer une chaîne mixant des tâches R et Python.
- Exemple : prétraitement Python → modélisation R → reporting Python ou R Markdown.

---

### 🔧 Cas d'usage typiques

| Besoin                          | Solution idéale                       |
|-------------------------------|----------------------------------------|
| Visualiser un modèle R dans Python     | `rpy2` + matplotlib/plotly             |
| Utiliser `ggplot2` dans Python        | `%R` magics ou `rpy2`                  |
| Utiliser `pandas` dans R              | `reticulate`                          |
| Intégrer un modèle scikit-learn dans R| `reticulate` ou REST API              |
| Reporting croisé R/Python             | `RMarkdown` avec blocs Python         |

---
