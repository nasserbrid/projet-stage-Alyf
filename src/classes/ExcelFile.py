import win32com.client
import time




class ExcelFile:
    EXCEL = win32com.client.Dispatch("Excel.Application")
    def __init__(self, workbook= None , worksheet= None, macro = None):
        self.workbook = workbook
        self.worksheet = worksheet 
        self.macro = macro
        

    def open_worksheet(self):
           
           # self.EXCEL.Visible = True 
            ExcelFile.EXCEL.Visible = True
           # if self.EXCEL.Visible == True :
            if ExcelFile.EXCEL.Visible == True:
                   print("excel is visible")
                  
                   
               
                   try:
                        
                       
                       # self.workbook = self.EXCEL.Workbooks.Open("C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\alyfData.xlsm")
                       
                        self.workbook = ExcelFile.EXCEL.Workbooks.Open("C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\alyfData.xlsm")
                        print(self.workbook)
                
                        self.worksheet = self.workbook.Sheets("DEV WEB")
                        

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
       
          self.workbook.SaveAs("C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\alyfDev.xlsm")
          
          self.workbook.Close(SaveChanges=True)
        
          #self.EXCEL.Quit()
          

          ExcelFile.EXCEL.Quit()
               
                
                 
 

   
   
    
    