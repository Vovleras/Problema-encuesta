from solucion_listas.datos_listas import calcular_tiempo_ejecucion
#from datos_pilas import funcion_entrada_quick DESCOMENTAR
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox

# Variable global para almacenar la ruta del archivo generado
archivo_generado = None

def cargar_archivo():
    # Abre el cuadro de diálogo para seleccionar un archivo
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        archivo_seleccionado.set(archivo)  # Guarda la ruta del archivo en la variable
        return archivo  # Retorna la ruta del archivo seleccionado
    return None

def enviar_info():
    global archivo_generado
    nombre_archivo = archivo_seleccionado.get()

    if not nombre_archivo:
        messagebox.showerror("Error", "Por favor, seleccione un archivo.")
        return

    try:
        # Obtener la estructura de datos seleccionada
        estructura_datos = opcion_alg.get()

        # Procesar el archivo usando la lógica del programa
        if estructura_datos == "Listas":
            archivo_generado = calcular_tiempo_ejecucion(nombre_archivo)
        elif estructura_datos == "Pilas":
           # archivo_generado = funcion_entrada_quick(nombre_archivo) #DESCOMENTAR
           archivo_generado = calcular_tiempo_ejecucion(nombre_archivo)
        else:
            messagebox.showerror("Error", "Estructura de datos no válida.")
            return

        if archivo_generado:
            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Éxito",
                "El procesamiento fue exitoso. Ahora puedes descargar el archivo."
            )
        else:
            messagebox.showerror("Error", "No se generó ningún archivo.")
    except Exception as e:
        # Mostrar mensaje de error en caso de fallo
        messagebox.showerror(
            "Error",
            f"Ocurrió un error al procesar el archivo: {str(e)}"
        )

def descargar_resultados():
    global archivo_generado

    if not archivo_generado:
        messagebox.showerror("Error", "No hay resultados para descargar. Procesa un archivo primero.")
        return

    try:
        # Abrir el archivo generado para leer su contenido
        with open(archivo_generado, "r") as archivo:
            contenido = archivo.read()

        # Abrir el cuadro de diálogo para guardar el archivo
        archivo_guardar = filedialog.asksaveasfile(
            mode="w",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if archivo_guardar:
            archivo_guardar.write(contenido)  # Escribir el contenido en la nueva ubicación
            archivo_guardar.close()
            messagebox.showinfo("Éxito", "Archivo descargado exitosamente.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo generado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al descargar el archivo: {str(e)}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Procesamiento de Encuestas")
ventana.geometry("450x400")
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

# Selección de estructura de datos
frame_algoritmo = tk.Frame(ventana, pady=10)
frame_algoritmo.pack(fill="x", padx=20)
texto_algoritmo = tk.Label(frame_algoritmo, text="Seleccione la estructura de datos:", anchor="w")
texto_algoritmo.pack(fill="x")
opcion_alg = tk.StringVar()
combobox_alg = Combobox(frame_algoritmo, textvariable=opcion_alg, state="readonly", values=["Listas", "Pilas"])
combobox_alg.current(0)
combobox_alg.pack(pady=5)

# Botón de procesar archivo
frame_boton = tk.Frame(ventana, pady=10)
frame_boton.pack()
boton = tk.Button(frame_boton, text="Obtener Resultados", command=enviar_info, width=20, bg="#4CAF50", fg="white")
boton.pack()

# Botón de descargar resultados
boton_descargar = tk.Button(frame_boton, text="Descargar Resultados", command=descargar_resultados, width=20, bg="#FFC107", fg="black")
boton_descargar.pack(pady=10)

# Iniciar la interfaz
ventana.mainloop()
    