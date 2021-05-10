from tkinter import *
from math import sqrt


root = Tk()
root.iconbitmap('favicon.ico')

root.title("Kalkulator")
wys = Entry(root, width=20,borderwidth=5,font=("Calibri",26))
wys.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def przy_klik(cyfra):
    stala = wys.get()
    wys.delete(0,END)
    wys.insert(0,str(stala) + str(cyfra))
    
def przy_usu():
    stala = str(wys.get())
    wys.delete(0,END)
    nstala = stala[:-1]
    wys.insert(0,nstala)
    
def przy_czy():
    wys.delete(0,END)

def przy_dodaj():
    try:
        global znak
        znak = "+"
        liczba1 = wys.get()
        global l_num
        l_num = float(liczba1)
        wys.delete(0,END)
    except ValueError:
        None
    
def przy_ode():
    try:
        global znak
        znak = '-' 
        liczba1 = wys.get()
        global l_num
        l_num = float(liczba1)
        wys.delete(0,END)
    except ValueError:
        None
        
def przy_mno():
    try:   
        global znak
        znak = '*' 
        liczba1 = wys.get()
        global l_num
        l_num = float(liczba1)
        wys.delete(0,END)
    except ValueError:
        None
    
def przy_dzi():
    try: 
        global znak
        znak = '/' 
        liczba1 = wys.get()
        global l_num
        l_num = float(liczba1)
        wys.delete(0,END)
    except ValueError:
        None
def przy_kro():
    stala = str(wys.get())
    wys.delete(0,END)
    spr = stala.find('.')
    if (spr != -1):
        wys.insert(0,stala)
    else:
        wys.insert(0,stala + '.')
    
def przy_zna():
    liczba = str(wys.get())
    try:
        if liczba[0] == '-':
            wys.delete(0,END)
            wys.insert(0,liczba[1:])
    
        if not liczba[0] == '-':
            liczba = '-' + liczba
            wys.delete(0,END)
            wys.insert(0,liczba)
    except IndexError:
        None

    
def przy_sum():
    liczba2 = wys.get()
    wys.delete(0,END)
    if znak == "+":
        wys.insert(0,l_num + float(liczba2))
               
    if znak == '-':
        wys.insert(0,l_num - float(liczba2))
        
    if znak == '*':
        wys.insert(0,l_num * float(liczba2))
        
    if znak == '/':
        try:
            wys.insert(0,l_num / float(liczba2))
        except ZeroDivisionError:
            wys.insert(0,0)
            
            
def przy_pie():
    try:
        liczba = float(wys.get())
        wys.delete(0,END)
        wys.insert(0,sqrt(liczba))
    except ValueError:
        None
      
#przyciski
p1 = Button(root,text=1,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda: przy_klik(1))
p2 = Button(root,text=2,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(2))
p3 = Button(root,text=3,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(3))
p4 = Button(root,text=4,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(4))
p5 = Button(root,text=5,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(5))
p6 = Button(root,text=6,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(6))
p7 = Button(root,text=7,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(7))
p8 = Button(root,text=8,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(8))
p9 = Button(root,text=9,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(9))
p0 = Button(root,text=0,padx=30,pady=20,bg='#000000',fg='#FFFFFF',command=lambda:przy_klik(0))
pdod = Button(root,text='+',padx=30,pady=20,bg='#666666',fg='#FFFFFF',command=przy_dodaj)
psum = Button(root,text='=',padx=30,pady=20,bg='#666666',fg='#FFFFFF',command=przy_sum)
pczy = Button(root,text='clear',padx=21,pady=20,bg ='#990000',fg='#FFFFFF',command=przy_czy)
pode = Button(root,text='-',padx=30,pady=20,bg='#666666',fg='#FFFFFF',command=przy_ode)
pdzi = Button(root,text='/',padx=30,pady=20,bg='#666666',fg='#FFFFFF',command=przy_dzi)
pmno = Button(root,text='*',padx=30,pady=20,fg='#FFFFFF',bg='#666666',command=przy_mno)
pusu = Button(root,text='del',padx=27,pady=20,fg='#FFFFFF',bg='#FF6666',command=przy_usu)
pkro = Button(root,text='.',padx=30,pady=20,bg='#666666',fg='#FFFFFF',command=przy_kro)
pzna = Button(root,text='+/-',padx=26,pady=20,bg='#666666',fg='#FFFFFF',command=przy_zna)
ppie = Button(root,text='√',padx=30,pady=20,bg='#666666',fg='#FFFFFF',command=przy_pie)


#pakowanie na ekran
p1.grid(row=4,column=0,pady=10,padx=1)
p2.grid(row=4,column=1,pady=10)
p3.grid(row=4,column=2,pady=10)
p4.grid(row=3,column=0,pady=10)
p5.grid(row=3,column=1,pady=10)
p6.grid(row=3,column=2,pady=10)
p7.grid(row=2,column=0,pady=10)
p8.grid(row=2,column=1,pady=10)
p9.grid(row=2,column=2,pady=10)
p0.grid(row=5,column=1,pady=10)
pdod.grid(row=2,column=3,pady=10)
psum.grid(row=1,column=3,pady=10)
pczy.grid(row=1,column=0,pady=10)
pode.grid(row=3,column=3,pady=10)
pmno.grid(row=4,column=3,pady=10)
pdzi.grid(row=5,column=3,pady=10)
pusu.grid(row=1,column=1,pady=10)
pkro.grid(row=5,column=2,pady=10)
pzna.grid(row=5,column=0,pady=10)
ppie.grid(row=1,column=2,pady=10)


root.mainloop()