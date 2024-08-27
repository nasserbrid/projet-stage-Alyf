import pandas as pd
df = pd.read_excel('alyfDev.xlsm')
with open('spreadsheet.html', 'w') as fo:
    fo.write(df.to_html())