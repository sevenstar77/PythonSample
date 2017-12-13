import openpyxl
work = openpyxl.Workbook()
sheet = work.active

sheet["A2"] = '수입'
sheet["B2"] = '수출'
sheet["A1"] = "2017 결산 보고"
sheet.merge_cells("A1:D1")
sheet["A1"].font = openpyxl.styles.Font(size=20, color="FF0010")
work.save("2017report.xlsx")