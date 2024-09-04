import Administrateur
#import CalendrierPlanning
import Formateur
import Module
import ExcelFile
import pandas as pd
#import win32com.client
from queue import Queue
from datetime import date
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
# load_dotenv() 

#excel = win32com.client.Dispatch("Excel.Application")

#print(f"{ExcelFile.excel} excel var")


test1 = ExcelFile.ExcelFile()

# new_formateur = Formateur.Formateur(144, "Eleonor","Huyhn", "h@h.fr")
# new_formateur.consulterPlanning()
# print(new_formateur.get_last_name())
# test1.open_worksheet()
# test1.get_formateur_worksheet(new_formateur.get_last_name())

# test2 = ExcelFile.ExcelFile()

# q = Queue()

# q.put(test1)
# q.put(test1.open_worksheet())
# q.put(test1.get_formateur_worksheet("huynh"))
# q.put(test2)
# q.put(test2.open_worksheet())
# q.put(test2.get_formateur_worksheet("lambert"))

#print(test1) # on crée une instance de la classe ExcelFile()
"""test1.open_worksheet()
test2.open_worksheet()
test2.get_formateur_worksheet("lambert")
print(test1.workbook)
test1.get_formateur_worksheet("huynh")"""



# print("\nFull: ", q.full()) 
# print("\nElements retired from the queue")
# print(q.get())
# print(q.get())


excel = ExcelFile.ExcelFile()
#excel.open_worksheet()

# test1.open_worksheet("Sessions Alternantes")

# Module1 = Module.Module("Réseaux - Révision Réseau TCP/IP", date(2022, 9,19),  date(2024, 8, 2), "2iTECH-TSSR-2022 - ALT", [], [] )

# print(Module1.get_nom_module())




#Module1.getInfo()
#Module1.getInfo()



test1.create_fullYearTeachingDataFrame_from_instructorSheet("Sessions Alternantes")

test1.create_module("Sessions Alternantes")


test1.get_session_dataframe("Sessions Alternantes")








