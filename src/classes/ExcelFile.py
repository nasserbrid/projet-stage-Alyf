import win32com.client
import time
# importing os module for environment variables
import os
import Module
import pandas as pd
from datetime import date
from datetime import datetime
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 




class ExcelFile:
    EXCEL = win32com.client.Dispatch("Excel.Application")
    def __init__(self, workbook= None , worksheet= None, macro = None):
        self.workbook = workbook
        self.worksheet = worksheet 
        self.macro = macro
        

    def open_worksheet(self, sheetName):
           
           # self.EXCEL.Visible = True 
            ExcelFile.EXCEL.Visible = True
           # if self.EXCEL.Visible == True :
            if ExcelFile.EXCEL.Visible == True:
                   print("excel is visible")
                  
                                
                   try:
                                          
                       # self.workbook = self.EXCEL.Workbooks.Open("C:\\Users\\nasse\\projet-stage-Alyf\\Test-fichier-excel\\alyfData.xlsm")
                       
                        self.workbook = ExcelFile.EXCEL.Workbooks.Open(os.getenv("ALYFMASTERPATH"))
                        #print(self.workbook)
                
                        self.worksheet = self.workbook.Sheets(sheetName)
                        

                        print(self.workbook)
                      
                   except FileNotFoundError:
                         print("Le fichier Excel est introuvable.")
                         
                        # self.EXCEL.Quit()
                         ExcelFile.EXCEL.Quit()

                         exit(1)
                   except Exception as e:
                        print('La feuille "DEV WEB" est introuvable:', e)
                        self.workbook.Close(SaveChanges=False)
                        #self.EXCEL.Quit()
                        ExcelFile.EXCEL.Quit()
                        exit(1)

                    
                    

    def get_formateur_worksheet(self, formateur_name):
         
          
          self.worksheet.Cells(1, 8).Value = formateur_name
       
          self.workbook.SaveAs(os.getenv("ALYFDEVPATH"))
          
          self.workbook.Close(SaveChanges=True)
        
          #self.EXCEL.Quit()
          

          ExcelFile.EXCEL.Quit()
          
          
    #Définir une méthode qui permet d'utiliser le dataframe et qui va récupérer des sessions dans "DEV WEB"
    def create_fullYearTeachingDataFrame_from_instructorSheet(self, sheetName):
           
           excel_path = os.getenv("ALYFDEVPATH")
           
           #output_path = os.getenv("ALYFJSONPATH")
               
           
           try:
                  i=0 
                  df_fullYearTeachingData = pd.read_excel(excel_path, sheet_name=sheetName, header=None,  usecols=[i,i+1,i+2], skiprows=3, index_col=None)
                  df_fullYearTeachingData = df_fullYearTeachingData.fillna('')
               
                              
           except FileNotFoundError:
                   print("Le fichier Excel est introuvable.")
                   exit(1)
           except ValueError:
              print('La feuille "DEV WEB" est introuvable.')
              exit(1)
                  
           for month in range(2,13):
                   i +=3
                   df = pd.read_excel(excel_path, sheet_name=sheetName, header=None, usecols=[i, i+1, i+2], skiprows=3, index_col=None)
                   df = df.fillna('')
                                           
           # Convertir les objets datetime en chaînes de caractères
        #    def convert_dates(value):
        #         if isinstance(value, datetime):
        #             return value.strftime("%Y-%m-%d %H:%M:%S")
        #         return value
       
           
           # Renommer les colonnes de df2 pour qu'elles correspondent à celles de df1
                   df.columns = df_fullYearTeachingData.columns
                   #print(f"{df_fullYearTeachingData.columns} df1 colums")

           
           # Concaténation des deux DataFrames verticalement
                   df_fullYearTeachingData = pd.concat([df_fullYearTeachingData, df])
         

          # Réinitialisation de l'index si nécessaire
                   df_fullYearTeachingData.reset_index(drop=True, inplace=True)
       


      # Affichage du résultat
                   pd.set_option('display.max_rows', None)
           #print(concat)
                   df_fullYearTeachingData.dropna(subset=[0],  inplace= True)
                   #df_fullYearTeachingData = df_fullYearTeachingData.map(convert_dates)
      
           return df_fullYearTeachingData
           
       # Récupération des modules
                   #print(f"les valeurs unique sont :{df_fullYearTeachingData[1].unique()}")
        
           """Cette partie est à l'utilisation de la classe Calendar_Planning   
        # # Convertir le DataFrame en JSON
        #    df_fullYearTeachingData = df_fullYearTeachingData.to_dict(orient='records')
        #    #print(df1[0].keys())


        # # Sauvegarder les données au format JSON
        #    with open(output_path, 'w', encoding='utf-8') as json_file:
        #            json.dump(df_fullYearTeachingData, json_file, ensure_ascii=False, indent=4, default="str")
        #            print(f"Les données ont été exportées avec succès vers {output_path}")
           """          
     
     #Pour des raisons de lisibilité, nous utiliserons une autre méthode pour transformer nos données en JSON.            

    def create_module(self, sheetName):
            #cette methode permettra de recuperer toutes les infos du module
            #On récupère les modules
            
           df  = self.create_fullYearTeachingDataFrame_from_instructorSheet(sheetName)
           

           liste_de_cours = df[1].unique()

           for cours in liste_de_cours:
                  print(cours)
                  dates = df.index[df[1]==cours]
                  dates_vals = []
                  for date in dates:
                         dates_vals.append(date)
                  print(f"vérification de dates_vals : {dates_vals}")

                  blocks = [[dates_vals[0]]]

                

                  for i in range(1,len(dates_vals)):
                         if dates_vals[i] - dates_vals[i-1] == 1:
                                blocks[-1].append(dates_vals[i])
                         else:
                                blocks.append([])
                                blocks[-1].append(dates_vals[i])
                  print(f"vérification de blocks : {blocks}")
                  
                  for j in range(0, len(blocks)):
                      module_test = Module.Module(df[1].iloc[blocks[0][0]], df[0].iloc[blocks[j][0]], 
                                                  df[0].iloc[blocks[j][-1]],df[2].iloc[blocks[0][0]],"", "")
                      liste_cours_termines_et_futurs =  self.create_list_cours_termines_et_futur(module_test.get_nom_module,sheetName)

                      module_test.set_modules_termines = liste_cours_termines_et_futurs[0]
                      module_test.set_modules_a_venir = liste_cours_termines_et_futurs[1]


                
                      
                      print(module_test.get_nom_module())
                      print(module_test.get_date_debut())
                      print(module_test.get_date_fin())
                  
                #   for index_value in blocks[0]:
                #       print(df[0].iloc[index_value])
                    
     
    def find_session_type(self, session_name):
        

        if session_name.find("ALT") :
            return "Sessions Alternantes"
        elif session_name.find("Hors Cursus"):
            return "Hors Cursus - Atos Générique"
        elif session_name.find("Isitech" or "XEFI"):
            return "Isitech - XEFI"
        else :
            return "Sessions Continues"
        
     
    def get_session_dataframe(self, sheetName): 
         feuille = self.open_worksheet(self.find_session_type(sheetName))
         
         excel_path = os.getenv("ALYFDEVPATH")
         
         #Faire 2 dataframes un avec seulement dates et l'autre présentera les sessions et les combiner par la suite
         df_session_name_and_dates = pd.read_excel(excel_path, sheet_name=sheetName, skiprows=1, nrows=3,  header=None)
         df_session_name_and_dates = df_session_name_and_dates.fillna('')
        
         
         
       #   #print(df.head(1))
       #   df_test = df_session_name_and_dates.head(3)
       #   nom_session = "2iTECH-TSSR-2022 - ALT"
       #   print(df_test)
         
       
       #   print(ind)

         value =  "2iTECH-TSSR-2022 - ALT"

# Extract Column Names
         column_index = df_session_name_and_dates.columns[df_session_name_and_dates.eq(value).any()].tolist()[0]
         print(column_index+1)
         date_debut =df_session_name_and_dates[column_index+1][1]
         date_fin = df_session_name_and_dates[column_index+1][2]
        
         number_of_rows_delta = date_fin - date_debut
         number_of_rows = number_of_rows_delta.days
         
        

         date_debut_str =str(date_debut)
         #date de fin inutile pour l'instant 
         #date_fin_str = str(date_fin)

         df_index_calendrier_sessions = pd.read_excel(excel_path, sheet_name=sheetName, usecols=[0],skiprows=1, header=None)

         index_date_debut_session = list(df_index_calendrier_sessions.index[df_index_calendrier_sessions[0] == datetime.fromisoformat(date_debut_str)])[0]

         df_modules_session = pd.read_excel(excel_path, sheet_name=sheetName, skiprows=index_date_debut_session, nrows=number_of_rows,usecols=[column_index, column_index+1],  header=None)

         return df_modules_session
    
    def create_list_cours_termines_et_futur(self, module_name, sheet_name):
          df = self.get_session_dataframe(sheet_name)
          df = df.fillna("")
          unique_units = list(df[1].unique())
          unique_units = list(filter(len, unique_units))
       
          unique_units.remove("FERIE")
          print("FERIE" in unique_units)
          

          print(unique_units)

          #il faut filtrer certains termes dont férié

        
      
     
                
          index_current_module  = unique_units.index(module_name)
          cours_termines = []
          cours_futurs = []

          for i in range(0,index_current_module):
                cours_termines.append(unique_units[i])
          for j in range(index_current_module,len(unique_units)):
                cours_futurs.append(unique_units[j])
          print(f"cours termines: {cours_termines}, cours_futurs:{cours_futurs}" )
       
         
          
         
      
         
          

        
       

             
       

         
         

   
         


         
         
         
         
         
         
         
         
         
         
         
         
        
        
            
        
                    
               
                
                 
 

   
   
    
    