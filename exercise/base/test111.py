import openpyxl

book = openpyxl.load_workbook(r'D:\ApiAutoTest\exercise\data\data.xlsx')
sheet = (book['Sheet2'])
for i in sheet:
    a = list(i)
    print(a)
