from openpyxl import load_workbook

# Load the existing Excel workbook
WB = load_workbook("Grades.xlsx")
WS = WB.active  # Get the active sheet

# Read data from the first row (header)
header = [cell.value for cell in WS[1]]
print("Header:", header)

#Changing the specific cell value
WS['A1'] = 'Student Name' 

# Save the workbook after making changes
WB.save("Grades.xlsx")
print("Excel file updated successfully!")