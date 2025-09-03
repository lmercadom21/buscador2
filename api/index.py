import tkinter as tk


palabras = [
    "moto nkd","moto nkd 125","moto nkd 150"
]

def sugerenciass(event):
    texto = buscar.get().lower()
    lista_sugerencias.delete(0, tk.END)
    
    if texto:  
        sugerencias = [p for p in palabras if texto in p.lower()]
        for sugerencia in sugerencias[:3]:  
            lista_sugerencias.insert(tk.END, sugerencia)



ventana= tk.Tk()
ventana.title=("Buscador")
ventana.geometry("250x250")

buscar = tk.Entry()
buscar.pack()
buscar.bind("<KeyRelease>", sugerenciass)


lista_sugerencias= tk.Listbox(ventana)
lista_sugerencias.pack()

ventana.mainloop()

#Referencias :
# https://docs.python.org/es/3.13/library/tkinter.html
#https://pythonguides.com/python-tkinter-search-box/
#https://www.youtube.com/watch?v=hkuT5swd9jI
