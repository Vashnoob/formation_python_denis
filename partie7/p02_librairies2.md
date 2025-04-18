## Librairies Python utiles

---

### 📊 1. `plotnine` (ggplot2 style en Python)
**Pourquoi c’est cool :**  
C’est un **portage de ggplot2 de R** en Python, avec une syntaxe déclarative élégante.

```python
from plotnine import ggplot, aes, geom_line
ggplot(df, aes('x', 'y')) + geom_line()
```

**Use case typique :**
Faire des visualisations rapidement en pensant en "grammaire des graphiques".

---

### 📈 2. `datatable` (pas `pandas`, mais ultra rapide !)
**Pourquoi c’est puissant :**  
Inspirée de `data.table` de R, cette librairie est **optimisée pour les très grands jeux de données**.

**Points forts :**
- Chargement plus rapide que Pandas
- Bon support du multithreading
- API proche de Pandas mais plus stricte

---

### 🔍 3. `pandas-profiling` (maintenant renommé en `ydata-profiling`)
**Pourquoi c’est indispensable :**  
Génère un **rapport d’analyse exploratoire complet** (EDA) en une ligne.

```python
from ydata_profiling import ProfileReport
report = ProfileReport(df)
report.to_notebook_iframe()
```

**Use case typique :**
Explorer un dataset inconnu en 1 minute.

---

### 🕵️ 4. `sweetviz`
**Pourquoi c’est malin :**  
Génère des **visualisations interactives** de données, avec comparaison de datasets (ex : train vs test).

**Use case typique :**
- Trouver des biais
- Visualiser des corrélations ou outliers

---

### 💡 5. `pyjanitor`
**Pourquoi c’est pratique :**  
Ajoute des méthodes utiles à Pandas, avec une syntaxe "pipe-friendly".

```python
import pandas as pd
import janitor
df.clean_names().remove_empty().filter_on("column > 0")
```

**Use case typique :**
Nettoyage express de datasets cracra.

---

### 🧹 6. `datacleaner`
**Pourquoi c’est smart :**  
Essaie de **nettoyer automatiquement un DataFrame** : imputation, suppression des colonnes peu utiles, etc.

```python
from datacleaner import autoclean
df_clean = autoclean(df)
```

**Use case typique :**
Préparation rapide avant un modèle.

---

### 📐 7. `polars`
**Pourquoi c’est surpuissant :**  
Une alternative moderne à Pandas, écrite en Rust, **ultra rapide** et **très performante en colonne**.

**Exemples puissants :**
- Traitement lazy (comme Spark)
- Support du multithread
- API fonctionnelle claire

---

### 📋 8. `tabulate`
**Pourquoi c’est pratique :**  
Affiche des tableaux jolis en console (text, markdown, html...).

```python
from tabulate import tabulate
print(tabulate(df.head(), headers='keys', tablefmt='github'))
```

**Use case typique :**
Console clean, rapports markdown.

---

### 📦 9. `pyarrow` et `fastparquet`
**Pourquoi c’est utile :**  
Manipuler les formats **Parquet** et **Arrow**, très utiles pour les données massives, typés et compressés.

**Use case typique :**
Travailler avec des pipelines Big Data, ou accélérer les temps de lecture/écriture.

---

### 💫 10. `dtale`
**Pourquoi c’est interactif :**  
Interface web live pour **explorer un DataFrame Pandas** comme dans un outil BI.

```python
import dtale
dtale.show(df)
```

**Use case typique :**
Explorer rapidement sans coder.

---