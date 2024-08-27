import ExcelFile
import pandas as pd
from datetime import datetime 


class Module:
    def __init__(self, nom_module, date_debut, date_fin,  session, modules_termines, modules_a_venir):
         self.__nom_module = nom_module
         self.__date_debut = date_debut
         self.__date_fin = date_fin
         self.__session = session
         self.__modules_termines = modules_termines
         self.__modules_a_venir = modules_a_venir
                   


    def get_nom_module(self):
            return self.__nom_module
        
    def get_date_debut(self):
            return self.__date_debut
        
    def get_date_fin(self):
             return self.__date_fin
        
    def get_session(self):
            return self.__session
        
    def get_modules_termines(self):
             return self.__modules_termines
        
    def get_modules_a_venir(self):
             return self.__modules_a_venir
    
    
    def set_nom_module(self, value):
            self.__nom_module = value
        
    def set_date_debut(self, value):
            self.__date_debut = value
        
    def set_date_fin(self, value):
            self.__date_fin = value
        
    def set_session(self, value):
            self.__session = value
        
    def set_modules_termines(self, value):
             self.__modules_termines = value
        
    def set_modules_a_venir(self, value):
             self.__modules_a_venir = value
    
    
    

    #Définir une méthode qui permet d'utiliser le dataframe et qui va récupérer des sessions dans "DEV WEB"
    def get_module_from_dataframe(self):
           
           excel_path = "C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\alyfDev.xlsm"

           try:
                  df1 = pd.read_excel(excel_path, sheet_name="DEV WEB", header=None,  usecols=[0,1,2], skiprows=2, index_col=None)

                  df2 = pd.read_excel(excel_path, sheet_name="DEV WEB", header=None, usecols=[3,4,5], skiprows = 2, index_col=None)

           except FileNotFoundError:
                   print("Le fichier Excel est introuvable.")
                   exit(1)
           except ValueError:
              print('La feuille "DEV WEB" est introuvable.')
              exit(1)

           df1 = df1.fillna('')
           df2 = df2.fillna('')



           def convert_dates(value):
                if isinstance(value, datetime):
                    return value.strftime("%Y-%m-%d %H:%M:%S")
                return value


           df1 = df1.map(convert_dates)
           df2 = df2.map(convert_dates)

        #    df1.set_index(df1[0])
        #    df2.set_index(df1[0])

        #    merged = pd.merge(df1, df2, on=df1[0])

        #    print(merged)

        #    df1 = pd.DataFrame(df1, index=[0,1,2])
        #    df2 = pd.DataFrame(df2, index=[3,4,5])

           frames = [df1,df2]
           result = pd.concat(frames, ignore_index=True)
           

           #concated = pd.concat([df1, df2],axis = 1, join="outer" )
           print(result)
                    
          
                
    
                         

           
           
           

           
        


    def create_module():
            #cette methode permettra de recuperer toutes les infos du module
        return 
           


    def getInfo(self):
        print(f"Le module est {self.get_nom_module()}, \n  la date de debut est {self.get_date_debut()}, \n la date de fin est {self.get_date_fin()}, \n il a appartient a la session {self.get_session()} \n il etait précédé de {self.get_modules_termines()} \n et sera suivi de {self.get_modules_a_venir()}") 

                  
        