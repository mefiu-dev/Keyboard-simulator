#!/usr/bin/python3

from tkinter import *
import time
import random
import threading
from PIL import Image, ImageTk
from tkinter.ttk import Radiobutton 
import threading
from tkinter import messagebox
import webbrowser
from tkinter import font

window = Tk()

x = window.winfo_screenwidth() # ширина экрана
y = window.winfo_screenheight() # высота экрана

n = str(x) + "x" + str(y)

w=x
w=w/2
h=y
h=h/2

#window.iconbitmap('logo.ico')
#imgicon = PhotoImage(file='menu.png')
#window.tk.call('wm', 'iconbitmap', window._w, imgicon)
window.iconphoto(True, PhotoImage(file="/usr/share/pixmaps/logo.png")) #Логотип приложения
window.geometry(n)
window.title("Клавиатурный тренажер")
window.resizable(width=False, height=False)
window.bind('<Control-q>', exit)
window.config(cursor='arrow')

ddd=0

r = IntVar()
r.set(1)

pred_a="pip" #Переменная для проверки 

def clicked():  
    windows = Tk()
    windows.geometry('500x300')
    windows.title("О программе")
    windows.resizable(width=False, height=False)
    pppo = Label(windows, text="Клавиатурный тренажер", font=("Arial Bold", 15), fg='#000000') 
    pppo.place(x=20, y=20) 
    ppppo = Label(windows, text="Версия 1.0.0", font=("Arial Bold", 10), fg='#000000') 
    ppppo.place(x=20, y=60) 
    po = Label(windows, text="Обучение печати на клавиатуре", font=("Arial Bold", 10), fg='#000000') 
    po.place(x=20, y=130) 
    ppo = Label(windows, text="© Mefiu, 2020", font=("Arial Bold", 10), fg='#000000') 
    ppo.place(x=20, y=160) 
    link1 = Label(windows, text="http://oskometa.ru", fg="blue",font=("Arial Bold", 10), cursor="hand2")
    link1.place(x=20, y=200)
    link1.bind("<Button-1>", lambda e: webbrowser.get(using='chromium').open_new_tab('http://oskometa.ru'))
    
        
    

def rus_alfavit(): #Функция отвечает за русский алфавит
    global b
    if b2=='Cyrillic_i':
        b='и'
    if b2=='Cyrillic_sha':
        b='ш'    
    if b2=='Cyrillic_io':
        b='ё'
    if b2=='Cyrillic_tse':
        b='ц'        
    if b2=='Cyrillic_softsign':
        b='ь'     
    if b2=='Cyrillic_be':
        b='б'    
    if b2=='Cyrillic_yu':
        b='ю'  
    if b2=='Cyrillic_te':
        b='т'  
    if b2=='Cyrillic_em':
        b='м'   
    if b2=='Cyrillic_es':
        b='с' 
    if b2=='Cyrillic_che':
        b='ч' 
    if b2=='Cyrillic_ya':
        b='я'            
    if b2=='Cyrillic_e':
        b='э'
    if b2=='Cyrillic_zhe':
        b='ж'
    if b2=='Cyrillic_de':
        b='д'   
    if b2=='Cyrillic_el':
        b='л'    
    if b2=='Cyrillic_o':
        b='о' 
    if b2=='Cyrillic_er':
        b='р' 
    if b2=='Cyrillic_pe':
        b='п' 
    if b2=='Cyrillic_a':
        b='а'
    if b2=='Cyrillic_ve':
        b='в'   
    if b2=='Cyrillic_yeru':
        b='ы' 
    if b2=='Cyrillic_ef':
        b='ф' 
    if b2=='Cyrillic_hardsign':
        b='ъ' 
    if b2=='Cyrillic_ha':
        b='х'  
    if b2=='Cyrillic_ze':
        b='з'
    if b2=='Cyrillic_shcha':
        b='щ'  
    if b2=='Cyrillic_ghe':
        b='г'       
    if b2=='Cyrillic_en':
        b='н' 
    if b2=='Cyrillic_ie':
        b='е'   
    if b2=='Cyrillic_ka':
        b='к'  
    if b2=='Cyrillic_u':
        b='у' 
    if b2=='Cyrillic_shorti':
        b='й'    

def rus(): #Функция отвечает за выбор русского алфавита
    global sss
    sss=1
    z = Button(window, image = imge, command=engl, cursor="hand1") #Создание кнопки-картинки на главном меню
    z.place(x=0, y=220) #Появление кнопки-картинки на главном меню  
    zz = Button(window, image = imgf, command=rus, cursor="hand1") #Создание кнопки-картинки на главном меню
    zz.place(x=0, y=185) #Появление кнопки-картинки на главном меню
    zam = Label(window, text="     ", font=("Arial Bold", 50), fg='#808080') #Создание замазки
    zam.place(x=w-40, y=h) #Замазка букв
    massiv()

def engl(): #Функция отвечает за выбор английского алфавита
    global sss
    sss=2
    z = Button(window, image = imge, command=rus, cursor="hand1") #Создание кнопки-картинки на главном меню
    z.place(x=0, y=185) #Появление кнопки-картинки на главном меню  
    zz = Button(window, image = imgf, command=engl, cursor="hand1") #Создание кнопки-картинки на главном меню
    zz.place(x=0, y=220) #Появление кнопки-картинки на главном меню
    zam = Label(window, text="     ", font=("Arial Bold", 50), fg='#808080') #Создание замазки
    zam.place(x=w-40, y=h) #Замазка букв
    massiv()    

def massiv(): #Функция отвечает за начало программы
    global alfa
    global ralfa
    if sss==2:
        ralfa=['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'q', 'w', 'r', 't', 'y', 'u', 'i', 'o', 'p', 's', 'j', 'k', 'l', 'z', 'x', 'v', 'n', 'm']  #Масив с английским алфавитом
        alfa=random.choice(ralfa) #Случайный выбор буквы из английского алфавита, 1 ступень
    if sss==1:    
        ralfa=['ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'] #Масив с русским алфавитом
        alfa=random.choice(ralfa) #Случайный выбор буквы из английского алфавита, 1 ступень
    init()    

def exit(): #Функция отвечает за разрушение окна
    window.destroy() #Разрушение окна

def aq(): #Случайный выбор буквы из английского алфавита, 2 ступень
    global a
    global sl
    global pred_a
    a=random.choice(ralfa)
    print("Pred:",pred_a,"___  Now:",a)
    if a==pred_a:
        aq()
    else:    
        pred_a=a
        print(a)
        sl = Label(window, text=a, font=("Arial Bold", 50), fg='#808080') 
        sl.place(x=w-35, y=h)

def init(): #Функция отвечает за считывание клавиши нажатой на клавиатуре и изменение случайной буквы
    aq() #Переход на функцию для изменения случайной буквы
    window.bind('<Key>',fun) #Считывание нажатой клавиши на клавиатуре

def fun(event): #Функция отвечает за обработку и сравнение нажатой на клавиатуре клавиши и случайно выбранной буквы
    global b #Оъявляем переменную b глобальной
    global l
    global b2, ddd
    b = event.keysym #Переменная b будет содержать нажатую клавишу
    b2 = event.keysym #Переменная b2 будет содержать нажатую клавишу
    rus_alfavit()
    print(b,'-',a)
    window.unbind('<Key>') # Отключить обработку других клавиш
    if b==a and ddd==1: #Сравнение нажатой на клавиатуре клавиши и случайно выбранной буквы, если они равны, то это обозначается, если нет, то нужно повторить нажатие
        ll = Label(window, text=a, font=("Arial Bold", 50), fg='#000000') #Создание зачеркивателя
        ll.place(x=w-35, y=h) #Зачеркивание правильной буквы
        l.place(x=w-300, y=h-300) #Появление надписи "Правильно!"
        t = threading.Timer(0.5, extimer) #Таймер, после 0.5 секунды запустится функция extimer
        t.start() #Старт таймера
    if b!=a and ddd==1:
        ln.place(x=w-300, y=h-300) #Появление надписи "Не правильно!"
        t = threading.Timer(0.5, extimer_no) #Таймер, после 0.5 секунды запустится функция extimer_no
        t.start() #Старт таймера
        #extimer_no() #Переход к функции extimer_no

def extimer(): #Функция отвечает за объявление правильного ответа
    global ddd
    print('molodes')
    print('---------------')
    if ddd==0:
        sl = Label(window, text="     ", font=("Arial Bold", 50), fg='#808080') 
        sl.place(x=w-40, y=h)
    else:    
        l.place(x=-1000, y=h-300) #Скрытие надписи "Правильно!"
        sl = Label(window, text="     ", font=("Arial Bold", 50), fg='#808080') 
        sl.place(x=w-40, y=h)
        init() #Переход к функции init

def extimer_no(): #Функция отвечает за объявление не правильного ответа
    print('Net')
    print('---------------')
    ln.place(x=-100000, y=h-300) #Скрытие надписи "Не правильно!"
    window.bind('<Key>',fun) # Включить обратно обработку клавиш, когда сработает таймер

def nad_menu(): #Функция отвечает за верхнее меню
    mainmenu = Menu(window) 
    window.config(menu=mainmenu) 
 
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Выход Ctrl+Q", font=("Arial Bold", 10), command=exit)
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="О программе", font=("Arial Bold", 10), command=clicked)
    mainmenu.add_cascade(label="Файл", menu=filemenu, font=("Arial Bold", 10))
    mainmenu.add_cascade(label="Справка", menu=helpmenu, font=("Arial Bold", 10))

def menu_yes(): #Функция отвечает за появление меню
    global ph
    global pho
    global o
    ph=w-200
    pho=h-300
    o = Button(window, image = img, command=menu_no, cursor="hand1") #Создание кнопки-картинки на главном меню
    o.place(x=ph, y=pho-50) #Появление кнопки-картинки на главном меню
    ppp.place(x=ph, y=h-100) #Появление надписи "Алфавит"
    al = Label(window, text=' ', font=("Arial Bold", 50), fg='#000000') #Создание зачеркивателя
    al.place(x=w-35, y=h) #Зачеркивание буквы

def menu_no(): #Функция отвечает за скрытие меню
    global sss
    o.place(x=-1000, y=pho) #Скрытие кнопки-меню на главном меню
    ppp.place(x=-1000, y=h-100) #Скрытие надписи "Алфавит"
    init_grafica_yes() #Создание графики
    sss=1 #Оъявляем переменную sss=1 для начала с русского алфавита
    massiv() #Начало основной программы

def init_grafica_yes(): #Функция отвечает за создание графики
    global bt, ddd
    ddd=1
    lbl.place(x=10, y=10) #Появление надписи "Найдите на клавиатуре нужный символ"
    bt = Button(window, text='МЕНЮ', font=("Arial Bold", 16), bd=1, foreground='#808080', activeforeground='#000000', command=init_grafica_no, cursor="hand1") #Создание кнопки "МЕНЮ"
    bt.place(x=10, y=100) #Появление кнопки "МЕНЮ"
    z = Button(window, image = imge, command=engl, cursor="hand1") #Создание кнопки-картинки на главном меню
    z.place(x=0, y=220) #Появление кнопки-картинки на главном меню  
    zz = Button(window, image = imgf, command=rus, cursor="hand1") #Создание кнопки-картинки на главном меню
    zz.place(x=0, y=185) #Появление кнопки-картинки на главном меню
    lbll.place(x=35, y=180) #Появление радио кнопки
    lbbl.place(x=35, y=220) #Появление радио кнопки
    #rad1.place(x=10, y=200) #Появление радио кнопки
    #rad2.place(x=10, y=220) #Появление радио кнопки 

def init_grafica_no(): #Функция отвечает за скрытие графики
    global ln, ddd
    ddd=0
    window.unbind('<Key>') # Отключить обработку других клавиш
    al = Label(window, text=' ', font=("Arial Bold", 50), fg='#000000') #Создание зачеркивателя
    al.place(x=w-35, y=h) #Зачеркивание буквы
    l.place(x=-100000000, y=h-300) #Скрытие надписи "правильно"
    ln.place(x=-10000000, y=h-300) #Скрытие надписи "Не правильно"
    lbl.place(x=-10000, y=10) #Скрытие надписи "Найдите на клавиатуре нужный символ"
    bt.place(x=-10000, y=100) #Скрытие кнопки "МЕНЮ"
    lbll.place(x=-10000, y=180) #Скрытие подписи радио кнопки
    lbbl.place(x=-10000, y=220) #Скрытие подписи радио кнопки
    zam = Label(window, text="     ", font=("Arial Bold", 50), fg='#808080') #Создание замазки
    zam.place(x=w-40, y=h) #Замазка букв
    zzam = Label(window, text="     ", font=("Arial Bold", 10), fg='#808080') #Создание замазки
    zzam.place(x=0, y=185) #Замазка кнопок
    zzzam = Label(window, text="     ", font=("Arial Bold", 10), fg='#808080') #Создание замазки
    zzzam.place(x=0, y=210) #Замазка кнопок
    zzzzam = Label(window, text="     ", font=("Arial Bold", 10), fg='#808080') #Создание замазки
    zzzzam.place(x=0, y=230) #Замазка кнопок
    #rad1.place(x=-1000, y=200) #Скрытие радио кнопки
    #rad2.place(x=-1000, y=220) #Скрытие радио кнопки 
    menu_yes() #Появлие главного меню
    
    

img = ImageTk.PhotoImage(Image.open("/usr/share/pixmaps/menu.png")) #Переменная отвечает за изображение на главном меню
ppp = Label(window, text='Aлфавит', font=("Arial Bold", 40), fg='black') #Переменная отвечает за надпись под 1 изображением на главном меню
lbl = Label(window, text="Найдите на клавиатуре нужный символ", font=("Arial Bold", 30)) #Переменная отвечает за надпись "Найдите на клавиатуре нужный символ"
l = Label(window, text='Правильно!', font=("Arial Bold", 50), fg='#19ff19') #Создание надписи "Правильно!"
ln = Label(window, text='Не правильно!', font=("Arial Bold", 50), fg='#ff0000') #Создание надписи "Не правильно!"
#Radiobutton(window,text='Русский', value=1, variable=r, command=rus)
#rad1 = Radiobutton(window,text='Русский', value=1, variable=r, command=rus)  
#rad2 = Radiobutton(window,text='Английский', value=2, variable=r, command=engl)



lbll = Label(window, text="Русский", font=("Arial Bold", 15)) #Переменная отвечает за подпись радио кнопки
lbbl = Label(window, text="Английский", font=("Arial Bold", 15)) #Переменная отвечает за подпись радио кнопки
imge = ImageTk.PhotoImage(Image.open("/usr/share/pixmaps/circle30px.png")) #Переменная отвечает за изображение радио кнопки
imgf = ImageTk.PhotoImage(Image.open("/usr/share/pixmaps/circleb30px.png")) #Переменная отвечает за изображение радио кнопки


nad_menu() #Создание верхнего меню
menu_yes() #Создание главного меню
    

window.mainloop()
