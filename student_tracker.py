from openpyxl import load_workbook
workbook=load_workbook('student_records.xlsx')
sheet=workbook.active
print("connected to sheet:",sheet.title)
