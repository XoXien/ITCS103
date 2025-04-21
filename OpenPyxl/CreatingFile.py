from openpyxl import Workbook

# Create a new Excel workbook
WB = Workbook()
WS = WB.active  # Get the active sheet

# Write data into cells

# 1st row of data
WS['A1'] = 'Name'
WS['B1'] = 'Math'
WS['C1'] = 'Science'
WS['D1'] = 'English'
WS['E1'] = 'PathFit'

# 2nd row of data
WS['A2'] = 'Owen'
WS['B2'] = '89'
WS['C2'] = '89'
WS['D2'] = '89'
WS['E2'] = '89'

# 3rd row of data

WS['A3'] = 'Angel'
WS['B3'] = '89'
WS['C3'] = '89'
WS['D3'] = '89'
WS['E3'] = '89'

# Save the workbook
WB.save("Grades.xlsx")
print("Excel file created successfully!")