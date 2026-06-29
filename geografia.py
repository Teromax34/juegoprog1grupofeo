import tkinter as tk
from tkinter import messagebox
import random

preguntas = [
{"pregunta":"¿Cuál es la capital de Argentina?","opciones":["Rosario","Buenos Aires","Mendoza","Córdoba"],"respuesta":"Buenos Aires"},
{"pregunta":"¿En qué provincia está el Aconcagua?","opciones":["San Juan","Mendoza","Neuquén","Salta"],"respuesta":"Mendoza"},
{"pregunta":"¿Provincia más austral?","opciones":["Santa Cruz","Chubut","Tierra del Fuego","Río Negro"],"respuesta":"Tierra del Fuego"},
{"pregunta":"¿Qué océano baña Argentina?","opciones":["Pacífico","Atlántico","Índico","Ártico"],"respuesta":"Atlántico"},
{"pregunta":"¿Capital de Córdoba?","opciones":["Villa María","Córdoba","Río Cuarto","San Francisco"],"respuesta":"Córdoba"},
{"pregunta":"¿Cataratas de Misiones?","opciones":["Niágara","Victoria","Iguazú","Moconá"],"respuesta":"Iguazú"},
{"pregunta":"¿Río que separa Argentina de Uruguay?","opciones":["Paraná","Uruguay","Colorado","Pilcomayo"],"respuesta":"Uruguay"},
{"pregunta":"¿Provincia más grande?","opciones":["Buenos Aires","Santa Cruz","Chubut","Mendoza"],"respuesta":"Buenos Aires"},
{"pregunta":"¿Provincia famosa por el vino?","opciones":["Entre Ríos","Misiones","Mendoza","La Pampa"],"respuesta":"Mendoza"},
{"pregunta":"¿Lago más famoso de Bariloche?","opciones":["Argentino","Nahuel Huapi","Puelo","Fagnano"],"respuesta":"Nahuel Huapi"},
]

ventana=None
lbl_pregunta=lbl_puntaje=lbl_numero=None
botones=[]
indice=0
puntaje=0
juego=[]

def cargar():
    global indice
    if indice>=len(juego):
        finalizar()
        return
    p=juego[indice]
    lbl_numero.config(text=f"Pregunta {indice+1} de {len(juego)}")
    lbl_pregunta.config(text=p["pregunta"])
    for i in range(4):
        op=p["opciones"][i]
        botones[i].config(text=op,command=lambda x=op: responder(x))

def responder(op):
    global indice,puntaje
    if op==juego[indice]["respuesta"]:
        puntaje+=1
        messagebox.showinfo("Respuesta","¡Correcto!")
    else:
        messagebox.showerror("Respuesta","Incorrecto.\nLa respuesta correcta era:\n"+juego[indice]["respuesta"])
    lbl_puntaje.config(text=f"Puntaje: {puntaje}")
    indice+=1
    cargar()

def finalizar():
    # Deshabilitar los botones para que no se puedan seguir apretando
    for b in botones:
        b.config(state="disabled", command=lambda: None)
    if puntaje>=7:
        txt=f"¡Ganaste! Puntaje: {puntaje}/10"
    else:
        txt=f"Perdiste. Puntaje: {puntaje}/10"
    print(txt)
    ventana.destroy()

def iniciar_juego():
    global ventana,lbl_pregunta,lbl_puntaje,lbl_numero,indice,puntaje,juego,botones
    indice=0
    puntaje=0
    juego=preguntas.copy()
    random.shuffle(juego)
    botones=[]
    ventana=tk.Tk()
    ventana.title("Trivia Geografía Argentina")
    ventana.geometry("700x500")
    ventana.configure(bg="#d9f4ff")
    ventana.resizable(False,False)
    tk.Label(ventana,text="TRIVIA DE GEOGRAFÍA ARGENTINA",font=("Arial",18,"bold"),bg="#d9f4ff").pack(pady=15)
    lbl_puntaje=tk.Label(ventana,text="Puntaje: 0",font=("Arial",12),bg="#d9f4ff")
    lbl_puntaje.pack()
    lbl_numero=tk.Label(ventana,text="",font=("Arial",12),bg="#d9f4ff")
    lbl_numero.pack()
    lbl_pregunta=tk.Label(ventana,text="",font=("Arial",15),wraplength=600,bg="#d9f4ff")
    lbl_pregunta.pack(pady=20)
    for _ in range(4):
        b=tk.Button(ventana,width=35,height=2,font=("Arial",12))
        b.pack(pady=5)
        botones.append(b)
    cargar()
    ventana.mainloop()
    return puntaje

if __name__=="__main__":
    iniciar_juego()