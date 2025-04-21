from openpyxl import Workbook, load_workbook

# Load the existing Excel workbook
WB = Workbook()
WS = WB.active  
WS.title = "BSIT"

WS.append(['BSIT','1B','MASARAP','MASARAP'])
WS.append(['BSIT','1B','MASARAP','MASARAP'])
WS.append(['BSIT','1B','MASARAP','MASARAP'])
WS.append(['BSIT','1B','MASARAP','MASARAP'])
WS.append(['End'])

WB.save("BSIT.xlsx")
print("Excel file updated successfully!")

