import calendar


# #Mon calendrier du mois de Janvier 2025 qui commence un lundi
# c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2025,1)
# print(str)

# #Utilisation des itérateurs (les 0 correspondent aux lundis du mois de décembre et lundi du mois de février)
# for i in c.itermonthdays(2025,4):
#     print(i)
    
# #permet de récupérer tous les mois de l'année
# for name in calendar.month_name:
#     print(name)


# #permet de récupérer les 3 premières lettres de tous les mois de l'année
# for name in calendar.month_abbr:
#     print(name)
    
# #permet de récupérer tous les jours de la semaine
# for name in calendar.day_name:
#     print(name)
    

# #permet de récupérer les 3 premières lettres de tous les jours de la semaine
# for name in calendar.day_abbr:
#     print(name)
    

# for month in range(1,13):
#     mycal = calendar.monthcalendar(2024, month)
#     print(mycal, calendar.month_name[month] )
    
    # week1 = mycal[0]
    # week2 = mycal[1]
    
    # if week1[calendar.MONDAY] != 0:
    #     auditDay = week1[calendar.MONDAY]
    # else:
    #     auditDay = week2[calendar.MONDAY]
        
    # print("%10s %2d" %(calendar.month_name[month], auditDay))
    
# print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# year = calendar.calendar(2025)
# print(year)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")


year2 = calendar.Calendar().yeardayscalendar(2025)
# print(year2)
print(f"semaine 1 de l'année 2025 : {year2[0][0][0]}")
# print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# year3 = calendar.Calendar().yeardays2calendar(2025)
# print(year3)