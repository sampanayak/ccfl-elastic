import os
import pyodbc
from openpyxl import load_workbook


source = "C:\Users\snayak\Desktop\Nfocus\N-Focus2018"
output = "C:\Users\snayak\Desktop\Output_NFcous"

dir_list = os.listdir(source)

for xlfile in dir_list:
    strfile = os.path.join(source, xlfile)

    if strfile.endswith('.xlsx') or strfile.endswith('.xls'):
        # CONNECT TO WORKBOOK
        conn = pyodbc.connect(r'Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};' + \
                               'DBQ={};'.format(strfile), autocommit=True)
        # RETRIEVE WORKBOOK SHEETS
        sheets = load_workbook(filename = strfile, use_iterators = True).get_sheet_names()

        # ITERATIVELY EXPORT SHEETS TO CSV IN OUTPUT FOLDER
        for s in sheets:
            outfile = os.path.join(output, '{0}_{1}.csv'.format(xlfile.split('.')[0], s))
            if os.path.exists(outfile): os.remove(outfile)

            strSQL = " SELECT * " + \
                     " INTO [text;HDR=Yes;Database={0};CharacterSet=65001].[{1}]" + \
                     " FROM [{2}$]"            
            conn.execute(strSQL.format(output, os.path.basename(outfile, s))
            conn.commit()
            conn.close()
