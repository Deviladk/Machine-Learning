import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#///   Fetching External Data into DAta Frame
 
try:
    print("Reading data from Ms-Excel Workbook...")
    df=pd.read_excel('E:\\training\\ML\\Online.xlsx')
except:
    print("File Error!!!")

print(df)

#    /////  factorizing the country columns
df1=df.copy()






