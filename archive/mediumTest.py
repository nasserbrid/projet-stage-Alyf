import pandas as pd

# Load data from Excel file
data = pd.read_excel('C:\\Users\\nasse\\projet-stage-Alyf\\alyfDev.xlsx')

# Write data to HTML file with formatting
with open('C:\\Users\\nasse\\projet-stage-Alyf\\test.html', 'w') as f:
    f.write(data.to_html(index=False, classes='table', header='true', border=1, justify='left'))