from datosEntrada import cargarArchivo
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox

def cargar_archivo():
    # Abre el cuadro de diálogo para seleccionar un archivo
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        archivo_seleccionado.set(archivo)  # Guarda la ruta del archivo en la variable

def enviar_info():
    nombre_archivo = archivo_seleccionado.get()
    algoritmo = opcion_alg.get()

    if not nombre_archivo:
        messagebox.showerror("Error", "Por favor, seleccione un archivo.")
        return

    # Mensaje de confirmación
    messagebox.showinfo("Procesando", f"Archivo: {nombre_archivo}\nAlgoritmo: {algoritmo}")
    cargarArchivo(nombre_archivo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Procesamiento de Encuestas")
ventana.geometry("450x350")
ventana.resizable(False, False)

# Encabezado
frame_encabezado = tk.Frame(ventana, pady=10)
frame_encabezado.pack()
texto_inicial = tk.Label(frame_encabezado, text="Procesamiento de Encuestas", font=("Arial", 16, "bold"))
texto_inicial.pack()
subtexto_inicial = tk.Label(frame_encabezado, text="Complete los campos para procesar la encuesta", font=("Arial", 10))
subtexto_inicial.pack()

# Entrada para cargar archivo
frame_archivo = tk.Frame(ventana, pady=10)
frame_archivo.pack(fill="x", padx=20)
texto_archivo = tk.Label(frame_archivo, text="Seleccione un archivo:", anchor="w")
texto_archivo.pack(fill="x")
archivo_seleccionado = tk.StringVar()
campo_archivo = tk.Entry(frame_archivo, textvariable=archivo_seleccionado, width=40, state="readonly")
campo_archivo.pack(side="left", pady=5, padx=5)
boton_cargar = tk.Button(frame_archivo, text="Cargar Archivo", command=cargar_archivo, bg="#2196F3", fg="white")
boton_cargar.pack(side="left", pady=5, padx=5)

# Selección del algoritmo
frame_algoritmo = tk.Frame(ventana, pady=10)
frame_algoritmo.pack(fill="x", padx=20)
texto_algoritmo = tk.Label(frame_algoritmo, text="Seleccione el algoritmo de procesamiento:", anchor="w")
texto_algoritmo.pack(fill="x")
opcion_alg = tk.StringVar()
combobox_alg = Combobox(frame_algoritmo, textvariable=opcion_alg, state="readonly", values=["Quick Sort", "Insert Sort"])
combobox_alg.current(0)
combobox_alg.pack(pady=5)

# Botón de enviar
frame_boton = tk.Frame(ventana, pady=20)
frame_boton.pack()
boton = tk.Button(frame_boton, text="Obtener Resultados", command=enviar_info, width=20, bg="#4CAF50", fg="white")
boton.pack()

# Iniciar la interfaz
ventana.mainloop()
