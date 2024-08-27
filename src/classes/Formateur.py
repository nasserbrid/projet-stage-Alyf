
import ExcelFile

class Formateur:
    def __init__(self,id, first_name, last_name, email):
        self.__id = id
        self.__first_name = first_name 
        self.__last_name = last_name 
        self.__email = email 
    
   
    #def isConnect(self):
        
    #Getter
    def get_last_name(self):
        return self.__last_name
    
    #Setter
    def set_last_name(self, name):
        self.__last_name = name


    def consulter_planning(self):
        file = ExcelFile.ExcelFile()
        file.open_worksheet()
        file.get_formateur_worksheet(self.get_last_name())

        
        


    