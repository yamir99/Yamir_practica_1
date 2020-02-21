import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
def vacio(variable):
    if variable != "":
        return True
    else:
        return False
def im_datos_per():
    bandera = False
    if vacio(Nombre.get()) and vacio(apellidop.get()) and vacio(apellidom.get()) and vacio(direccion.get()) and vacio(colonia.get()) and vacio(municipio.get()):
        texto_f= "Nombre: "+Nombre.get()+"\nApellido paterno: "+apellidop.get()+"\nApellido materno: "+apellidom.get()+"\nDireccion: "+direccion.get()+"\nColonia: "+colonia.get()+"\nCiudad: "+ciudad.get()+"\nMunicipio: "+municipio.get()
        mBox.showinfo('datos personales',texto_f)
        #print (materno.get())
        #accion.configure(text = "si funciono")
    else: 
        mBox.showinfo('datos personales',"Llena todos los datos")
def im_datos_extr():
    bandera=False
    texto_final = "Tus pasatiempos favoritos son: "
    if opcion_1.get() ==1:
        bandera = True
        texto_final = texto_final + "\n-Leer"
    if opcion_2.get() == 1:
        bandera = True
        texto_final = texto_final + "\n-Tocar guitarra"
    if opcion_3.get() == 1:
        bandera = True
        texto_final = texto_final + "\n-Jugar videojuegos"
    if opcion_4.get() == 1:
        bandera = True
        texto_final = texto_final + "\n-Dibujar"
    if opcion_5.get() == 1:
        bandera = True
        texto_final = texto_final +"\n-Patinar"
    if bandera == False:
        texto_final = texto_final +"\n-No tienes pasatiempos favoritos"
    texto_final = texto_final + "\nSu estado es: \n-"+ opcion.get()+"\n"
    mBox.showinfo('Datos extras',texto_final)
def datos_imp():
    mBox.showinfo('Datos extras','Nombre: Yamir Alejandro\nApellido: Garcia Padilla\nSemestre: 4º\nCarrera: ISC')
def imp_todo():
    txt = (str)caja.get()
    texto_final = "Tus pasatiempos favoritos son: "
    if vacio(Nombre.get()) and vacio(apellidop.get()) and vacio(apellidom.get()) and vacio(direccion.get()) and vacio(colonia.get()) and vacio(municipio.get()):
        texto_final= "Nombre: "+Nombre.get()+"\nApellido paterno: "+apellidop.get()+"\nApellido materno: "+apellidom.get()+"\nDireccion: "+direccion.get()+"\nColonia: "+colonia.get()+"\nCiudad: "+ciudad.get()+"\nMunicipio: "+municipio.get()+"\n"
        #mBox.showinfo('datos personales',texto_f)
        #print (materno.get())
        #accion.configure(text = "si funciono")
        bandera=False
        if opcion_1.get() ==1:
            bandera = True
            texto_final = texto_final + "\n-Leer"
        if opcion_2.get() == 1:
            bandera = True
            texto_final = texto_final + "\n-Tocar guitarra"
        if opcion_3.get() == 1:
            bandera = True
            texto_final = texto_final + "\n-Jugar videojuegos"
        if opcion_4.get() == 1:
            bandera = True
            texto_final = texto_final + "\n-Dibujar"
        if opcion_5.get() == 1:
            bandera = True
            texto_final = texto_final +"\n-Patinar"
        if bandera == False:
            texto_final = texto_final +"\n-No tienes pasatiempos favoritos"
        texto_final = texto_final + "\nSu estado es: \n-"+ opcion.get()+"\n"
        mBox.showinfo('Datos',texto_final)
    else: 
        mBox.showinfo('datos personales',"Llena todos los datos")
ventana = tk.Tk()
ventana.geometry('+450+100')
ventana.title("Registro alumnos")
#crear menu
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)
#agregar opcines al menu
opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label="Imprimir",command = imp_todo)
opciones_menu.add_separator()
opciones_menu.add_command(label= "Salir",command = funcion_salir)
barra_menu.add_cascade(label="Sistema",menu=opciones_menu)

menu_ayuda = Menu(barra_menu)
menu_ayuda.add_command(label="Acerca de",command = datos_imp)
barra_menu.add_cascade(label="Ayuda",menu= menu_ayuda)

#agregar pestaña
tabcontrol = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text = 'Datos personales')
tabcontrol.grid(column=0,row=0)


tab2 = ttk.Notebook(tabcontrol)
tab2.pack()
tabcontrol.add(tab2, text='Datos extras')
ttk.Label(tab1, text="Nombre:").grid(pady = 10,padx = 10,column=0,row=0)
ttk.Label(tab1, text="Apellido paterno: ").grid(pady = 10,padx = 10,column=0,row=1)
ttk.Label(tab1, text="Apellido materno: ").grid(pady = 10,padx = 10,column=0,row=2)
#nombre
Nombre= tk.StringVar()
Nombrecapturado = ttk.Entry(tab1, width=20,textvariable= Nombre)
Nombrecapturado.grid(pady = 10,column = 1,row=0)
#apellido paterno
apellidop= tk.StringVar()
apellidopcapturado = ttk.Entry(tab1, width=20,textvariable= apellidop)
apellidopcapturado.grid(pady = 10,column = 1,row=1)
#appeli materno
apellidom= tk.StringVar()
apellidomcapturado = ttk.Entry(tab1, width=20,textvariable= apellidom)
apellidomcapturado.grid(pady = 10,column = 1,row=2)
#direccion
ttk.Label(tab1, text = "Direccion: ").grid(column=0, row=3)
direccion = tk.StringVar()
direccionCapturado = ttk.Entry(tab1, width=20,textvariable= direccion)
direccionCapturado.grid(pady = 10,column = 1,row=3)
#lista de colonia
ttk.Label(tab1, text="Colonia").grid(column=0,row=4)
colonia = tk.StringVar()
coloniaSeleccionado = ttk.Combobox(tab1,width=20,textvariable=colonia)
coloniaSeleccionado['values']=("La huerta","Torremolinos","El realito")
coloniaSeleccionado.grid(pady = 10,column=1,row=4)
coloniaSeleccionado.configure(state = 'readonly')
coloniaSeleccionado.current(0)
#ciudad
ttk.Label(tab1, text="Ciudad").grid(column=0,row=5)
ciudad = tk.StringVar()
ciudadSeleccionado = ttk.Combobox(tab1,width=20,textvariable=ciudad)
ciudadSeleccionado['values']=("Morelia","Patzcuaro","Zamora")
ciudadSeleccionado.grid(pady = 10,column=1,row=5)
ciudadSeleccionado.configure(state = 'readonly')
ciudadSeleccionado.current(0)
#Municipio
ttk.Label(tab1, text="Municipio").grid(pady = 10,padx = 10,column=0,row=6)
municipio = tk.StringVar()
ciudadSeleccionado = ttk.Combobox(tab1,width=20,textvariable=municipio)
ciudadSeleccionado.configure(background = "yellow")
ciudadSeleccionado['values']=("Morelia","Patzcuaro","Zamora")
ciudadSeleccionado.grid(pady = 10,column=1,row=6)
ciudadSeleccionado.configure(state = 'readonly')
ciudadSeleccionado.current(0)
#boton para imprimir datos personales
accion = tk.Button(tab1, text = "Imprimir datos personales",activebackground = 'BLUE',cursor = 'hand2',command = im_datos_per)
accion.grid(pady = 10,column=0,row=7,columnspan=3)

#########3
#check botton
ttk.Label(tab2, text="Pasatiempos").grid(pady = 10,padx = 10,column=0,row=0,columnspan=3)
opcion_1 = tk.IntVar()
casilla_1 = tk.Checkbutton(tab2, text= "Leer", variable = opcion_1)
#casilla_1.select()
casilla_1.grid(pady = 10,padx=10, column=0,row=1,sticky=tk.W)

opcion_2 = tk.IntVar()
casilla_2 = tk.Checkbutton(tab2, text = "Tocar guitarra", variable = opcion_2)
casilla_2.grid(pady = 10,padx=10,column=1, row =1,sticky=tk.W)

opcion_3 = tk.IntVar()
casilla_3 = tk.Checkbutton(tab2,text= "Jugar videojuegos", variable = opcion_3)
casilla_3.grid(pady=10,padx=10,column=2,row=2,sticky = tk.W)

opcion_4 = tk.IntVar()
casilla_4 = tk.Checkbutton(tab2,text= "Dibujar", variable = opcion_4)
casilla_4.grid(pady=10,padx=10,column=0,row=2,sticky = tk.W)
opcion_5 = tk.IntVar()
casilla_5 = tk.Checkbutton(tab2,text= "Patinar", variable = opcion_5)
casilla_5.grid(pady=10,padx=10,column=1,row=2,sticky = tk.W)

#Radio button
ttk.Label(tab2, text="Escoge tu estado").grid(pady = 10,padx = 10,column=0,row=3,columnspan=3)
opcion = tk.StringVar()
radio1 = tk.Radiobutton(tab2,text = "Soltero", variable = opcion, value="Soltero",)
radio1.grid(pady =10,padx=10,column =0, row = 4, sticky = tk.W)
radio1.select()
radio2 = tk.Radiobutton(tab2,text = "Casado", variable = opcion, value="casado")
radio2.grid(pady =10,padx=10,column =1, row = 4, sticky = tk.W)
radio3 = tk.Radiobutton(tab2,text = "Viudo", variable = opcion, value="viudo")
radio3.grid(pady =10,padx=10,column =2, row = 4, sticky = tk.W)
radio4 = tk.Radiobutton(tab2,text = "Divorsiado", variable = opcion, value="divorsiado")
radio4.grid(pady =10,padx=10,column =0, row = 5, sticky = tk.W)
radio5 = tk.Radiobutton(tab2,text = "Union libre", variable = opcion, value="union libre")
radio5.grid(pady =10,padx=10,column =1, row = 5, sticky = tk.W)

#boton imprimir datos extras
accion2 = tk.Button(tab2, text = "Imprimir datos",command = im_datos_extr)
accion2.grid(pady = 10,padx=10,column=0,row=8,columnspan=3)

#agregar la caja de texto
ttk.Label(tab2, text="Objetivo de vida").grid(pady = 10,padx = 10,column=0,row=6,columnspan=3)
caja = scrolledtext.ScrolledText(tab2, width = '45', height= '3',wrap = tk.WORD)
caja.grid(column = 0,row = 7,columnspan = 3,padx = 10)
ventana.mainloop()