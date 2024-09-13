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

import CalendrierPlanning
# loading variables from .env file
# load_dotenv() 

#excel = win32com.client.Dispatch("Excel.Application")

#print(f"{ExcelFile.excel} excel var")




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


# excel = ExcelFile.ExcelFile()
# #excel.open_worksheet()

# test1.open_worksheet("Sessions Alternantes")

# Module1 = Module.Module("Réseaux - Révision Réseau TCP/IP", date(2022, 9,19),  date(2024, 8, 2), "2iTECH-TSSR-2022 - ALT", [], [] )

# print(Module1.get_nom_module())


# Module1 = Module.Module("Virtualisation", date(2024, 8, 31),  date(2024, 10, 10), "PRF Orly", ["linux", "windows server"], ["python"," java"]  )


# #Module1.getInfo()
# #Module1.getInfo()

# test1.open_worksheet("DEV WEB")

# test1.create_fullYearTeachingDataFrame_from_instructorSheet("DEV WEB")

# test1.create_module("DEV WEB")



# test1.get_session_dataframe("Sessions Alternantes")
# # test1.create_list_cours_termines_et_futur("Réseaux - Révision Réseau TCP/IP","Sessions Alternantes")


# test1 = ExcelFile.ExcelFile()


# test1.open_worksheet("DEV WEB")


# test1.get_formateur_worksheet("HUYNH")
# #print(test1.worksheet.__dir__)

# print(test1.create_module())


# SOUKEINA = Formateur.Formateur(id =1, first_name="Soukeina", last_name="BEN CHIKHA", email="soukeina.benchikha@alyfpro.fr")

# SOUKEINA.consulter_planning("DEV WEB")

excel_file = ExcelFile.ExcelFile()
excel_file.open_worksheet("DEV WEB")
#Soukeina_excel_file.create_fullYearTeachingDataFrame_from_instructorSheet()
excel_file.get_formateur_worksheet('huynh')
dico = excel_file.create_modules()
# print(dico)

# #print(excel_file.find_session_type('dffl ALT'))

# test_calendar = CalendrierPlanning.Calendar(2024)

# dico_calendrier = excel_file.create_module()

#pseudocode idea for adding modules to calendar
# for value in dico_calendrier:
#     dates = value.extract_module_dates()
#     calendrier.add_module_to_calendrier(modulename,dates )
# test_calendar.add_event(10, 7,"module")


# # test_calendar._yearmonthday_to_index(10)

# dico = {}
# testModule = Module.Module("blue", date(2024,5,6), date(2024,6,6), "pink","","")

# testModule_1 = Module.Module("yellow", date(2024,4,6), date(2024,7,6), "red","","")

# testModule_2 = Module.Module("green", date(2024,2,10), date(2024,3,10), "yellow","","")

# dico = {"1": testModule, "2": testModule_1, "3": testModule_2}


# calendrier_test = CalendrierPlanning.Calendar(2024)


# dates_test = dico.extract_module_dates()
#calendrier_test.add_module_to_calendrier(dico)
# calendrier_test.add_module_to_calendrier(testModule)

#print(calendrier_test.get_events_for_day(6,5))

# calendrier_test.dictionaries_module_to_calendar(dico)



# dictioTest = {"coursdemath":{0:Module.Module("cours1","2024-10-03","2024-10-04", "sessiontest","","")},1:Module.Module("cours2","2024-11-03","2024-11-04", "sessiontest","","")}
# dico.extract_module_dates()
# calendrier_test.dictionaries_module_to_calendar(dico)

#print(testModule.get_id_module())

# test_calendar.displayevents(10,7)



# calendrier_test.displayevents(4,7)

# print(enumerate(test_calendar.yearcal).__repr__())


