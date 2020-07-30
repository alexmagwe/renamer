'''
the program renames files of any type in the folder provided
usage:choose directory from the file dialog box tha thas appeared
choose which format the names will be,either letters or digits(for the future ,machine learning is to be implemented to automatically give the files meaningful and short names )

Enjoy
'''



import os,sys
import tkinter.filedialog
import string
fpath=tkinter.filedialog.askdirectory(title='where are them files')
type_=input('ENTER n TO SAVE THE NAMES AS DIGITS OR l FOR LETTERS{l/n} ')
letters=" "+string.ascii_lowercase
# fpath=os.path.join(cwd,ftrnm)

def images(fpath):
    for _,_,images in os.walk(fpath):
        return images
def renamer(*args):
    list_=images(fpath)
    if type_=='l':
        if len(list_)>len(letters):
            print('we cant use letters as there are lots of images and there are just not enough  letters\nI can rename with digits if thats ok with you?')
            x=input('(y/n):')
            if x=='y':
                d_namer(list_)
            else:
                return
        else:
            l_namer(list_,letters)                
    elif type_=='n':
        d_namer(list_)
    print(images(fpath))  

# renamer(images(fpath))
def l_namer(l,letters):
    for index,name in enumerate(l):
        path=os.path.join(fpath,name)
        _,ext=os.path.splitext(path)
        os.rename(f"{path}",f"{fpath}/{letters[index]}{ext}")
def d_namer(l):
    for index,name in enumerate(l):
        path=os.path.join(fpath,name)    
        _,ext=os.path.splitext(path)
        os.rename(f"{path}",f"{fpath}/{index+1}{ext}")
    
if __name__=='__main__':
    renamer(letters,images,fpath,type_)
