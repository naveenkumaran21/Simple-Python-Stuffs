import xlrd
import xlsxwriter
import tkinter
from tkinter import filedialog

root=tkinter.Tk()
root.geometry("300x300")

File1 = filedialog.askopenfile(mode='r',filetypes=[("Excel","*.xlsx *.xlsm *.ods *.csv *.tsv")])
File2 = filedialog.askopenfile(mode='r',filetypes=[("Excel","*.xlsx *.xlsm *.ods *.csv *.tsv")])
Result = filedialog.askdirectory()

File1,File2 = str(File1),str(File2)

file1 = xlrd.open_workbook(File1[25:-29])
file2 = xlrd.open_workbook(File2[25:-29])

result_book = xlsxwriter.Workbook("{}\Result.xlsx".format(Result))
result = result_book.add_worksheet()

sheet1 = file1.sheet_by_index(0)
sheet2 = file2.sheet_by_index(0)

rows = sheet1.nrows
columns = sheet1.ncols

if sheet1.nrows == sheet2.nrows and sheet1.ncols == sheet2.ncols:
    for row in range(rows):
        check1 = sheet1.row_values(row)
        check2 = sheet2.row_values(row)
        for cell in range (columns):
            result.write(row,cell,(check1[cell] == check2[cell]))
result_book.close()
