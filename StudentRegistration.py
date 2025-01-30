from tkinter import *
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl , xlrd
from openpyxl import Workbook
import pathlib

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"
root=Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

root.mainloop()



file=pathlib.Path('Student_data.xlsx')
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Class"
    sheet['D1']="DOB"
    sheet['E1']="Date of Registration"
    sheet['F1']="Religion"
    sheet['G1']="Skill"
    sheet['H1']="Father Name"
    sheet['I1']="Mother Name"
    sheet['J1']="Father Occupation"
    sheet['K1']="Mother Occupition "

    file.save('Student_data.xlsx')


    #top frames
    Label(root,text="Email: sordillamike@gmail.com", width=10,height=3,bg="#f0687c",anchor='e').pack(side=TOP,fill=X)