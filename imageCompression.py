import os
from PIL import Image, ImageFilter
from tkinter import filedialog,ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename

directory=""
file1=""
dir1=""
#  -----------------Operative functions---------------------------------#
def selectFolder():

    global file1
    global dir1
    dir1=True
    file1=False
    global directory
    directory= filedialog.askdirectory()

def selectImage():
    global file1
    global dir1
    global directory
    dir1 = False
    file1 = True
    directory= askopenfilename()  # show an "Open" dialog box and return the path to the selected fill

def compress(filepath,folderpath=''):
    # print(filepath+'check 1')
    img = Image.open(filepath)
    x, y = (img.size)

    change = int(compression_ratio.get())
    x = int((x * change) / 100)
    y = int((y * change) / 100)

    new_image = img.resize((x, y))
    f = os.path.basename(open(filepath).name)
    # print(f.split('.')[0] + '_new.' + f.split('.')[1])
    if file1:
        new_image.save(f.split('.')[0] + '_new.' + f.split('.')[1])
    elif dir1:

        print(folderpath+f.split('.')[0] + '_new.' + f.split('.')[1])
        new_image.save(folderpath+f.split('.')[0] + '_new.' + f.split('.')[1])
        

def compressing():
    global  directory
    if file1:
        print(directory)
        directory=""
        # compress(dirctory)

    elif dir1:
        compressFolder=(directory+'/'+'compressed')
        os.mkdir(compressFolder)
        print("file generated")
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                compress(os.path.join(directory, filename),directory+'/compressed/')
            else:
                continue
        directory=''

def AppExit():
    exit()

 # --------------------GUI-------------------------------------------#

#App Initialization
win=tk.Tk()
win.title('Image Compressor')

#Lable
name_lable=ttk.Label(win,text='Select a folder ')
name_lable.grid(row=0,column=0)

#Select Image
browser=ttk.Button(win,text='Select image', command=selectImage)
browser.grid(row=0,column=1)

name_lable=ttk.Label(win,text=' or ')
name_lable.grid(row=0,column=2)

#Path Button
browser=ttk.Button(win,text='Select Folder', command=selectFolder)
browser.grid(row=0,column=3)

#Compressor Button
browser=ttk.Button(win,text='Compress', command=compressing)
browser.grid(row=1,column=3)

#exit Button
browser=ttk.Button(win,text='Exit', command=AppExit)
browser.grid(row=2,column=1)

# compression_Ratio
compression_ratio=(tk.StringVar())
compression_box=ttk.Combobox(win,width=14, textvariable=compression_ratio, state='readonly')
compression_box['values']=(10,20,30,40,50,60,70,80,90)
compression_box.current(0)
compression_box.grid(row=1,column=1)

win.mainloop()


# Need some changes here 
