from datosEntrada import cargarArchivo
import tkinter as tk

def enviar_info():
    nombre_archivo = archivo_seleccionado.get()
    algoritmo = opcion_alg.get()
    cargarArchivo(nombre_archivo)


ventana = tk.Tk()
ventana.title("Procesamiento de encuestas")

texto_inicial = tk.Label(ventana, text="Bienvenido, por favor complete los compos para procesar la encuesta")
texto_inicial.pack()

#Para obtener el nombre del archivo
texto_archivo = tk.Label(ventana, text="Nombre del archivo")
texto_archivo.pack()
archivo_seleccionado = tk.Entry(ventana, width=30)
archivo_seleccionado.pack()

#Para obtener el algoritmo de procesamiento 
opcion_alg = tk.StringVar(value="1")
tk.Radiobutton(ventana, text="Quick Sort", variable=opcion_alg, value="1").pack()
tk.Radiobutton(ventana, text="Insert Sort", variable=opcion_alg, value="2").pack()

boton = tk.Button(ventana, text="Obtener resultados", command=enviar_info)
boton.pack()



# Iniciar la interfaz
ventana.mainloop()