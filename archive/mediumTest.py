import pandas as pd

# Load data from Excel file
data = pd.read_excel('C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\Test-fichier-excel\\alyfDev.xlsx')

# Write data to HTML file with formatting
with open('C:\\Users\\iggdu\\Downloads\\Test-fichier-excel\\test.html', 'w') as f:
    f.write(data.to_html(index=False, classes='table', header='true', border=1, justify='left'))