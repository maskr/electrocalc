#   Copyright 2016 David Crespo Romero
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tkinter import *
   
# formula

def results():
    finallevel = Toplevel()
    finallevel.title('Results')
    finallevel.geometry("150x50")
    finallevel.configure(background="black")
    seleccion = titulodiv.index(ACTIVE)
    val1=float(valor1.get())
    val2=float(valor2.get())
    val3=float(valor3.get())

    if seleccion == 0:
        try:
            solution = (val1 * (val3 / (val2 + val3)))
            r = Label (finallevel, width=20, bg="black", fg="red", text="{0:.2f} Volts".format(solution))
        except:
            r = Label (finallevel, width=20, bg="black", fg="red", text="Divide by zero.\n Adjust Values.")
    elif seleccion == 1:
        try:
            resultresistor = val1/val2
            r = Label (finallevel, width=20, bg="black", fg="red", text="{0:.2f} Ohms".format(resultresistor))
        except:
            r = Label (finallevel, width=20, bg="black", fg="red", text="Error.\n Check your settings.")
    elif seleccion == 2:
        try:
            resultvolts = val1*val2
            r = Label (finallevel, width=20, bg="black", fg="red", text="{0:.2f} Volts".format(resultvolts))
        except:
            r = Label (finallevel, width=20, bg="black", fg="red", text="Error.\n Something went wrong")
    elif seleccion == 3:
        try:
            resultcurrent = val1 / val2
            r = Label (finallevel, width=20, bg="black", fg="red", text="{0:.3f} Amps".format(resultcurrent))
        except:
            r = Label (finallevel, width=20, bg="black", fg="red", text="Error.\n Check your entries")
    else:
        r = Label (finallevel, width=20, bg="black", fg="red", text="Unknown problem.\n Inform developer.")
    r.pack()

# New window with info

def about():
    toplevel = Toplevel()
    toplevel.title('About')
    toplevel.focus_set()
    w = Label(toplevel, text = "Copyright 2015 David Crespo Romero")
    w.pack()
    w = Label(toplevel, text = "This program is free software: you can redistribute it and/or modify")
    w.pack()
    w = Label(toplevel, text = "it under the terms of the GNU General Public License as published by")
    w.pack()
    w = Label(toplevel, text = "the Free Software Foundation, either version 3 of the License, or")
    w.pack()
    w = Label(toplevel, text = "(at your option) any later version.")
    w.pack()
    w = Label(toplevel, text = " ")
    w.pack()
    w = Label(toplevel, text = "This program is distributed in the hope that it will be useful,")
    w.pack()
    w = Label(toplevel, text = "but WITHOUT ANY WARRANTY; without even the implied warranty of")
    w.pack()
    w = Label(toplevel, text = "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
    w.pack()
    w = Label(toplevel, text = "GNU General Public License for more details.")
    w.pack()
    w = Label(toplevel, text = " ")
    w.pack()
    w = Label(toplevel, text = "You should have received a copy of the GNU General Public License")
    w.pack()
    w = Label(toplevel, text = "along with this program.  If not, see <http://www.gnu.org/licenses/>.")
    w.pack()

def operationsel():
	seleccion = titulodiv.index(ACTIVE)
	etiquetasel.config(text = operations[seleccion])
	etiqueta1.config(text = etiqueta1sel[seleccion])
	etiqueta2.config(text = etiqueta2sel[seleccion])
	etiqueta3.config(text = etiqueta3sel[seleccion])

# Set the windows and many variables

finestra = Tk()
finestra.wm_title("Electrocalc")
finestra.configure(bg="black")

valor1 = DoubleVar()
valor2 = DoubleVar()
valor3 = DoubleVar()
seleccion = StringVar()

operations = ["Voltage divider", "Resistor Ohm", "Voltage Ohm", "Intensity Ohm"]
etiqueta1sel = ["Vin", "Insert V", "Insert Intensity", "Insert V"]
etiqueta2sel = ["Insert R1 value", "Insert Intensity", "Insert Resistance", "Insert Resistance"]
etiqueta3sel =["Insert R2 value", "Nothing here", "Nothing here", "Nothing here"]

# tell me things about what you know and want to do

titulodiv = Listbox (finestra, height=5, selectbackground="yellow", highlightbackground="black", bg="red", fg="black", selectmode="SINGLE")
for x in range(0, 4):
	titulodiv.insert(x, operations[x])
	titulodiv.pack()
titulodiv.select_set(0)

seleccion = titulodiv.index(ACTIVE)

boton3=Button(finestra, activebackground="red", bg="black", fg="red", text="Ok", command=operationsel)
boton3.config(highlightbackground="black")
boton3.pack()

etiquetasel = Label(finestra, bg="red", fg="black", text = operations[seleccion])
etiquetasel.pack()
etiqueta1 = Label(finestra, bg="black", fg="red", text=etiqueta1sel[seleccion])
etiqueta1.pack()
entrada1=Entry(finestra, highlightbackground="black", bg="red", fg="black", textvar=valor1).pack()

etiqueta2 = Label(finestra, bg="black", fg="red", text=etiqueta2sel[seleccion])
etiqueta2.pack()
entrada2=Entry(finestra, highlightbackground="black", bg="red", fg="black", textvar=valor2).pack()

etiqueta3 = Label(finestra, bg="black", fg="red", text=etiqueta3sel[seleccion])
etiqueta3.pack()
entrada3=Entry(finestra, highlightbackground="black", bg="red", fg="black", textvar=valor3).pack()

# Oh!! It's a button!!

boton1=Button(finestra, activebackground="red", bg="black", fg="red", text="Calculate", command=results)
boton1.config(highlightbackground="black")
boton1.pack(side=RIGHT)

# A new button for information

boton2=Button(finestra, activebackground="red", bg="black", fg="red", text="About", command=about)
boton2.config(highlightbackground="black")
boton2.pack(side=RIGHT)

# Loop
mainloop( )
