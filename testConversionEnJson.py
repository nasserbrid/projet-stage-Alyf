#Nous avons utilisé ce deuxième fichier, il permet de transformer le fichier excel au format xlsm (avec macro) en donnée Json (donc permet de faire une sérialisation) (programme 2).
import pandas as pd
import json
from datetime import datetime

# Chemin du fichier Excel à lire
excel_path = "C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\alyfDev.xlsm"  
output_path = "C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\data.json"

# Charger le fichier Excel avec pandas
try:
    df = pd.read_excel(excel_path, sheet_name="DEV WEB", header=None, usecols="A,B,C", skiprows=2, index_col=None)
except FileNotFoundError:
    print("Le fichier Excel est introuvable.")
    exit(1)
except ValueError:
    print('La feuille "DEV WEB" est introuvable.')
    exit(1)

# Remplacer les NaN par des espaces
df = df.fillna('')



# Convertir les objets datetime en chaînes de caractères
def convert_dates(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value

# Appliquer la conversion sur toutes les colonnes
#df = df.applymap(convert_dates) (cette expression est depreciée)
df = df.map(convert_dates)


# Convertir le DataFrame en JSON

print(df[1].unique())

data = df.to_dict(orient='records')
print(data[0].keys())



# Sauvegarder les données au format JSON
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4, default="str")

print(f"Les données ont été exportées avec succès vers {output_path}")

