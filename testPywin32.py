import win32com.client
import os

# Créer une instance d'Excel
excel = win32com.client.Dispatch("Excel.Application")


class excel_file:
    def __init__(self, workbook = None, worksheet = None , macro = None):
        self.workbook = workbook
        self.worksheet = worksheet 
        self.macro = macro

    def open_file(self):
            if excel.Visible == True :
                   try:
                        self.workbook = excel.Workbooks.Open("C:\\Users\\nasse\\projet-stage-Alyf\\alyfData.xlsm")
                      
                   except FileNotFoundError:
                         print("Le fichier Excel est introuvable.")
                         excel.Quit()
                         exit(1)
       
             
                         
excel_file01 = excel_file()

excel_file01.open_file()
                
       
       
         
             
            
             

        
    

    



# Créer une instance d'Excel
#excel = win32com.client.Dispatch("Excel.Application")

# Rendre Excel visible (optionnel)
#excel.Visible = True

# Ouvrir le fichier Excel
try:
    workbook = excel.Workbooks.Open(os.getenv("AlyfMasterpath"))
except FileNotFoundError:
    print("Le fichier Excel est introuvable.")
    excel.Quit()
    exit(1)

# Accéder à la feuille nommée "DEV WEB"
try:
    worksheet = workbook.Sheets("DEV WEB")
except Exception as e:
    print('La feuille "DEV WEB" est introuvable:', e)
    workbook.Close(SaveChanges=False)
    excel.Quit()
    exit(1)

# Lire la valeur de la cellule H1
cell_value = worksheet.Cells(1, 8).Value  # H1 est à la ligne 1, colonne 8
print("La valeur de la cellule H1 est:", cell_value)

# Modifier la valeur de la cellule H1
worksheet.Cells(1, 8).Value = "HUYNH"

# Sauvegarder les modifications dans un nouveau fichier
workbook.SaveAs(os.getenv("AlyfDevpath"))


# Fermer le classeur et quitter Excel
workbook.Close(SaveChanges=True)
excel.Quit()
