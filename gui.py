# Comienza aporte Kevin Ibarra
import tkinter as tk
from tkinter import filedialog
from analizador_semantico_gui import *
import sys
from io import StringIO
class IDE_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RubyCompiler")
        self.root.configure(bg="#cb3234")
         # Dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calcular las dimensiones de la ventana
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        
        # Calcular la posición x,y para centrar la ventana
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Configurar la geometría
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        #  menú
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        
        # Menú Archivo
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_command(label="Nuevo Documento", command=self.nuevo_documento)
        menu_bar.add_command(label="Abrir", command=self.abrir_archivo)
        menu_bar.add_command(label="Guardar", command=self.guardar_archivo)
        menu_bar.add_command(label="Guardar Como", command=self.guardar_como)
        menu_bar.add_separator()
        menu_bar.add_command(label="Salir", command=root.destroy)

        # principal
        main_frame = tk.Frame(root, bg="#cb3234")  
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=90)
        # Botón Ejecutar
        execute_button = tk.Button(main_frame, text="Ejecutar", command=self.ejecutar_codigo, bg="#ffffff")  
        execute_button.pack(pady=10)

        # Frame contenedor para los subframes
        container_frame = tk.Frame(main_frame, bg="#cb3234")
        container_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Subframe para el área de código
        a_frame = tk.Frame(container_frame, bg="#282c34")
        a_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))


        # Área de texto para números de línea
        self.linenumbers = tk.Text(a_frame, width=2, bg="#282c34", fg="white", bd=0, wrap=tk.NONE)
        self.linenumbers.pack(side=tk.LEFT, fill=tk.Y)


        # Área de texto
        self.code_text = tk.Text(a_frame, wrap=tk.WORD, bg="#1e1e1e", fg="white", insertbackground="white")
        self.code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        y_scroll_bar = tk.Scrollbar(a_frame, command=self.on_scroll)
        y_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.code_text.config(yscrollcommand=y_scroll_bar.set)


        # subframe2
        subframe2 = tk.Frame(container_frame, bg="#282c34")
        subframe2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

        # Área de resultados
        self.resultados_text = tk.Text(subframe2, wrap=tk.WORD, bg="#1e1e1e", fg="white", insertbackground="white")
        self.resultados_text.pack(fill=tk.BOTH, expand=True)
        self.resultados_text.config(state=tk.DISABLED)

        # Ruta del archivo actual
        self.file_path = None


        # Configurar la actualización de los números de línea
        self.actualizar_numeros_de_linea()

        self.code_text.bind('<Configure>', self.actualizar_numeros_de_linea)
        self.code_text.bind('<KeyRelease>', self.actualizar_numeros_de_linea)


    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Abrir archivo", ".rb"), ("Todos los archivos", ".*")])

        if file_path:
            self.file_path = file_path
            with open(file_path, "r") as file:
                content = file.read()
                self.code_text.delete(1.0, tk.END)
                self.code_text.insert(tk.END, content)
                self.actualizar_numeros_de_linea()



    def guardar_archivo(self):
        if self.file_path:
            content = self.code_text.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
            self.actualizar_numeros_de_linea()
        else:
            self.guardar_como()


    def guardar_como(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", ".txt"), ("Todos los archivos", ".*")])

        if file_path:
            self.file_path = file_path
            content = self.code_text.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.actualizar_numeros_de_linea()


    def nuevo_documento(self):
        self.file_path = None
        self.code_text.delete(1.0, tk.END)
        self.actualizar_numeros_de_linea()

    def ejecutar_codigo(self):
        self.limpiar_resultados()
        codigo_fuente = self.code_text.get("1.0", tk.END)
        resultado = analizar_codigo(codigo_fuente)
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.insert(tk.END, resultado)
        self.resultados_text.config(state=tk.DISABLED)

    def limpiar_resultados(self):
        # Limpiar el contenido del área de resultados
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.config(state=tk.DISABLED)

    def on_scroll(self, *args):
        self.code_text.yview_moveto(args[0])
        self.linenumbers.yview_moveto(args[0])


    def actualizar_numeros_de_linea(self, event=None):
        lines = self.code_text.get(1.0, tk.END).count('\n')
        linenumbers_string = '\n'.join(str(i) for i in range(1, lines + 2))
        self.linenumbers.config(state=tk.NORMAL)
        self.linenumbers.delete(1.0, tk.END)
        self.linenumbers.insert(tk.END, linenumbers_string)
        self.linenumbers.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    ide = IDE_GUI(root)
    root.mainloop()
#Termina aporte Kevin Ibarra