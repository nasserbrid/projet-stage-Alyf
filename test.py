# def returnsheet(s):
 
#     alternance_syn = ["alt", "ALT"]
#     hors_cursus_syn = ["HC", "HORS CURSUS", "hors cursus", "horscursus", "ATOS", "atos"]
#     isitech_xefi_syn = ["isi", "ISI", "isitech", "xefi", "XEFI"]
 
 
#     for value in alternance_syn:
#         if value in s:
#             return "SESSION ALTERNANTE"
   
#     for value in hors_cursus_syn:
#         if value in s:
#             return "HORS CURSUS"
       
       
#     for value in isitech_xefi_syn:
#         if value in s:
#             return "ISITECH"
   
#     return "CONTINUE"
 
 
# print(returnsheet("dsfhdsjf xefi dsflsqld"))
 
 
def returnsheet(s):
    # Define a dictionary with keywords as keys and corresponding session names as values
    keywords = {
        "SESSION ALTERNANTE": ["hilt", "alt", "alt"],
        "HORS CURSUS": ["HC", "HORS CURSUS", "hors cursus", "horscursus", "ATOS", "atos"],
        "ISITECH": ["isi", "ISI", "isitech", "xefi", "XEFI"]
    }
 
    # Check if any keyword from the lists is in the input string
    for key, values in keywords.items():
        if (value in s for value in values):
            return key
 
    # Default return value if no match is found
    return "CONTINUE"
 
 
print(returnsheet("dkfjdskf dd alt dsldlk"))
 

    





    
   
    
    