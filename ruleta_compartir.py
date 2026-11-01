import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import math

class RuletaCompartir:
    def __init__(self, root):
        self.root = root
        self.root.title(" Ruleta de Compartir Navideña ")
        self.root.geometry("1200x850")
        
        # Colores tema navideño futurista
        self.colores = {
            'fondo': '#0a0e27',
            'acento1': '#ff1744',
            'acento2': '#00e676',
            'acento3': '#00b8d4',
            'acento4': '#ffd600',
            'texto': '#ffffff',
            'panel': '#1a1f3a'
        }
        
        self.root.configure(bg=self.colores['fondo'])
        
        # Datos
        self.personas = []
        self.items = []
        self.asignaciones = {}
        self.animacion_activa = False
        self.particulas = []
        self.estrellas = []
        
        # Cargar datos
        self.cargar_datos()
        
        # Crear interfaz
        self.crear_interfaz()
        
        # Animar fondo
        self.crear_estrellas()
        self.animar_fondo()
    
    def crear_estrellas(self):
        """Crear estrellas para el fondo"""
        for _ in range(100):
            x = random.randint(0, 1200)
            y = random.randint(0, 850)
            size = random.randint(1, 3)
            speed = random.uniform(0.1, 0.5)
            self.estrellas.append({'x': x, 'y': y, 'size': size, 'speed': speed})
    
    def animar_fondo(self):
        """Animar estrellas de fondo"""
        try:
            self.canvas_fondo.delete('estrella')
            
            for estrella in self.estrellas:
                estrella['y'] += estrella['speed']
                if estrella['y'] > 850:
                    estrella['y'] = 0
                    estrella['x'] = random.randint(0, 1200)
                
                color = random.choice([self.colores['acento3'], self.colores['acento4'], '#ffffff'])
                self.canvas_fondo.create_oval(
                    estrella['x'], estrella['y'],
                    estrella['x'] + estrella['size'], estrella['y'] + estrella['size'],
                    fill=color, outline='', tags='estrella'
                )
            
            self.root.after(50, self.animar_fondo)
        except:
            pass
    
    def crear_interfaz(self):
        """Crear interfaz gráfica"""
        # Canvas de fondo
        self.canvas_fondo = tk.Canvas(
            self.root, bg=self.colores['fondo'],
            highlightthickness=0, width=1200, height=850
        )
        self.canvas_fondo.place(x=0, y=0)
        
        # Frame principal
        frame_contenedor = tk.Frame(self.root, bg=self.colores['fondo'])
        frame_contenedor.place(relx=0.5, rely=0.02, anchor='n', relwidth=0.95)
        
        # Título
        titulo = tk.Label(
            frame_contenedor, text="🎄 RULETA NAVIDEÑA FUTURISTA 🎅",
            font=("Impact", 36, "bold"), bg=self.colores['fondo'], fg=self.colores['acento1']
        )
        titulo.pack(pady=10)
        
        subtitulo = tk.Label(
            frame_contenedor, text="✨ Sistema de Asignación Inteligente ✨",
            font=("Arial", 14, "italic"), bg=self.colores['fondo'], fg=self.colores['acento3']
        )
        subtitulo.pack()
        
        # Frame personas e items
        frame_principal = tk.Frame(frame_contenedor, bg=self.colores['fondo'])
        frame_principal.pack(pady=15)
        
        self.crear_panel_personas(frame_principal)
        self.crear_panel_items(frame_principal)
        self.crear_area_ruleta(frame_contenedor)
        self.crear_panel_asignaciones(frame_contenedor)
        
        self.actualizar_listas()
        self.actualizar_asignaciones()
    
    def crear_panel_personas(self, parent):
        """Panel de personas"""
        frame = tk.LabelFrame(
            parent, text="👥 PARTICIPANTES", font=("Arial", 14, "bold"),
            bg=self.colores['panel'], fg=self.colores['acento2'],
            borderwidth=3, relief=tk.GROOVE, padx=15, pady=15
        )
        frame.grid(row=0, column=0, sticky="nsew", padx=10)
        
        # Entrada
        fe = tk.Frame(frame, bg=self.colores['panel'])
        fe.pack(fill=tk.X, pady=8)
        
        self.entrada_persona = tk.Entry(
            fe, font=("Arial", 13), width=20, bg='#2d3250',
            fg=self.colores['texto'], insertbackground=self.colores['acento2'],
            relief=tk.FLAT, borderwidth=2
        )
        self.entrada_persona.pack(side=tk.LEFT, padx=5, ipady=6)
        self.entrada_persona.bind('<Return>', lambda e: self.agregar_persona())
        
        tk.Button(
            fe, text="➕", command=self.agregar_persona, bg=self.colores['acento2'],
            fg='black', font=("Arial", 16, "bold"), cursor="hand2", relief=tk.FLAT, width=3
        ).pack(side=tk.LEFT, padx=5)
        
        # Lista
        fl = tk.Frame(frame, bg=self.colores['panel'])
        fl.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = tk.Scrollbar(fl)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lista_personas = tk.Listbox(
            fl, font=("Consolas", 12), yscrollcommand=scrollbar.set, height=8,
            bg='#2d3250', fg=self.colores['acento2'],
            selectbackground=self.colores['acento2'], selectforeground='black', relief=tk.FLAT
        )
        self.lista_personas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_personas.yview)
        
        tk.Button(
            frame, text="🗑️ ELIMINAR", command=self.eliminar_persona,
            bg=self.colores['acento1'], fg='white', font=("Arial", 11, "bold"),
            cursor="hand2", relief=tk.FLAT
        ).pack(pady=8, ipady=5, ipadx=15)
    
    def crear_panel_items(self, parent):
        """Panel de items"""
        frame = tk.LabelFrame(
            parent, text="🎁 ITEMS PARA LLEVAR", font=("Arial", 14, "bold"),
            bg=self.colores['panel'], fg=self.colores['acento4'],
            borderwidth=3, relief=tk.GROOVE, padx=15, pady=15
        )
        frame.grid(row=0, column=1, sticky="nsew", padx=10)
        
        # Entrada
        fe = tk.Frame(frame, bg=self.colores['panel'])
        fe.pack(fill=tk.X, pady=8)
        
        self.entrada_item = tk.Entry(
            fe, font=("Arial", 13), width=20, bg='#2d3250',
            fg=self.colores['texto'], insertbackground=self.colores['acento4'],
            relief=tk.FLAT, borderwidth=2
        )
        self.entrada_item.pack(side=tk.LEFT, padx=5, ipady=6)
        self.entrada_item.bind('<Return>', lambda e: self.agregar_item())
        
        tk.Button(
            fe, text="➕", command=self.agregar_item, bg=self.colores['acento4'],
            fg='black', font=("Arial", 16, "bold"), cursor="hand2", relief=tk.FLAT, width=3
        ).pack(side=tk.LEFT, padx=5)
        
        # Lista
        fl = tk.Frame(frame, bg=self.colores['panel'])
        fl.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = tk.Scrollbar(fl)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lista_items = tk.Listbox(
            fl, font=("Consolas", 12), yscrollcommand=scrollbar.set, height=8,
            bg='#2d3250', fg=self.colores['acento4'],
            selectbackground=self.colores['acento4'], selectforeground='black', relief=tk.FLAT
        )
        self.lista_items.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_items.yview)
        
        tk.Button(
            frame, text="🗑️ ELIMINAR", command=self.eliminar_item,
            bg=self.colores['acento1'], fg='white', font=("Arial", 11, "bold"),
            cursor="hand2", relief=tk.FLAT
        ).pack(pady=8, ipady=5, ipadx=15)
    
    def crear_area_ruleta(self, parent):
        """Área de ruleta con animación visual"""
        frame = tk.Frame(parent, bg=self.colores['panel'], relief=tk.RIDGE, borderwidth=3)
        frame.pack(pady=15, padx=20, fill=tk.X)
        
        # Botón de girar
        self.btn_girar = tk.Button(
            frame, text="🎰 GIRAR RULETA MÁGICA 🎰",
            command=self.girar_ruleta, bg=self.colores['acento1'],
            fg='white', font=("Impact", 20, "bold"), cursor="hand2",
            relief=tk.RAISED, borderwidth=4, padx=40, pady=15
        )
        self.btn_girar.pack(pady=15)
        
        # Canvas para animación
        self.canvas_ruleta = tk.Canvas(
            frame, width=700, height=120, bg=self.colores['fondo'],
            highlightthickness=0
        )
        self.canvas_ruleta.pack(pady=10)
    
    def crear_panel_asignaciones(self, parent):
        """Panel de asignaciones"""
        frame = tk.LabelFrame(
            parent, text="📋 ASIGNACIONES FINALES", font=("Arial", 14, "bold"),
            bg=self.colores['panel'], fg=self.colores['acento3'],
            borderwidth=3, relief=tk.GROOVE, padx=15, pady=15
        )
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Texto
        ft = tk.Frame(frame, bg=self.colores['panel'])
        ft.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(ft)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.texto_asignaciones = tk.Text(
            ft, font=("Consolas", 11), height=6, yscrollcommand=scrollbar.set,
            wrap=tk.WORD, state=tk.DISABLED, bg='#2d3250', fg=self.colores['texto'],
            relief=tk.FLAT
        )
        self.texto_asignaciones.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.texto_asignaciones.yview)
        
        tk.Button(
            frame, text="🔄 LIMPIAR TODO", command=self.limpiar_asignaciones,
            bg=self.colores['acento3'], fg='black', font=("Arial", 11, "bold"),
            cursor="hand2", relief=tk.FLAT
        ).pack(pady=8, ipady=5, ipadx=15)
    
    def agregar_persona(self):
        """Agregar persona"""
        nombre = self.entrada_persona.get().strip()
        if nombre:
            if nombre not in self.personas:
                self.personas.append(nombre)
                self.actualizar_listas()
                self.guardar_datos()
                self.entrada_persona.delete(0, tk.END)
            else:
                messagebox.showwarning("⚠️", "Esta persona ya está en la lista")
        else:
            messagebox.showwarning("⚠️", "Por favor ingresa un nombre")
    
    def eliminar_persona(self):
        """Eliminar persona"""
        sel = self.lista_personas.curselection()
        if sel:
            persona = self.personas[sel[0]]
            if persona in self.asignaciones:
                del self.asignaciones[persona]
                self.actualizar_asignaciones()
            self.personas.pop(sel[0])
            self.actualizar_listas()
            self.guardar_datos()
        else:
            messagebox.showwarning("⚠️", "Selecciona una persona")
    
    def agregar_item(self):
        """Agregar item"""
        item = self.entrada_item.get().strip()
        if item:
            if item not in self.items:
                self.items.append(item)
                self.actualizar_listas()
                self.guardar_datos()
                self.entrada_item.delete(0, tk.END)
            else:
                messagebox.showwarning("⚠️", "Este item ya está en la lista")
        else:
            messagebox.showwarning("⚠️", "Por favor ingresa un item")
    
    def eliminar_item(self):
        """Eliminar item"""
        sel = self.lista_items.curselection()
        if sel:
            item = self.items[sel[0]]
            for persona in list(self.asignaciones.keys()):
                if self.asignaciones[persona] == item:
                    del self.asignaciones[persona]
            self.items.pop(sel[0])
            self.actualizar_listas()
            self.actualizar_asignaciones()
            self.guardar_datos()
        else:
            messagebox.showwarning("⚠️", "Selecciona un item")
    
    def actualizar_listas(self):
        """Actualizar listas"""
        self.lista_personas.delete(0, tk.END)
        for persona in self.personas:
            self.lista_personas.insert(tk.END, f"  👤 {persona}")
        
        self.lista_items.delete(0, tk.END)
        for item in self.items:
            self.lista_items.insert(tk.END, f"  🎁 {item}")
    
    def girar_ruleta(self):
        """Girar ruleta con animación visual"""
        if not self.personas:
            messagebox.showwarning("⚠️", "Agrega al menos una persona")
            return
        if not self.items:
            messagebox.showwarning("⚠️", "Agrega al menos un item")
            return
        if self.animacion_activa:
            return
        
        self.asignaciones.clear()
        self.animacion_activa = True
        self.btn_girar.config(state=tk.DISABLED)
        
        self.animar_mezcla(0)
    
    def animar_mezcla(self, contador):
        """Animación de mezcla visual"""
        if contador < 30:
            self.canvas_ruleta.delete('all')
            
            # Crear efecto de mezcla visual
            num_elementos = min(6, max(len(self.personas), len(self.items)))
            for i in range(num_elementos):
                persona = random.choice(self.personas) if self.personas else "?"
                item = random.choice(self.items) if self.items else "?"
                
                x_persona = 50 + (i * 110)
                x_item = x_persona
                y_persona = 20
                y_item = 70
                
                color_p = random.choice([self.colores['acento2'], self.colores['acento3']])
                color_i = random.choice([self.colores['acento4'], self.colores['acento1']])
                
                # Dibujar persona
                self.canvas_ruleta.create_oval(
                    x_persona-5, y_persona-5, x_persona+5, y_persona+5,
                    fill=color_p, outline=''
                )
                self.canvas_ruleta.create_text(
                    x_persona, y_persona+15, text=persona[:8],
                    fill=color_p, font=("Arial", 9, "bold")
                )
                
                # Flecha giratoria
                angulo = (contador * 30 + i * 60) % 360
                x_flecha = x_persona + 10 * math.cos(math.radians(angulo))
                y_flecha = (y_persona + y_item) / 2 + 10 * math.sin(math.radians(angulo))
                self.canvas_ruleta.create_text(
                    x_flecha, y_flecha, text="⚡",
                    fill=self.colores['acento4'], font=("Arial", 16)
                )
                
                # Dibujar item
                self.canvas_ruleta.create_oval(
                    x_item-5, y_item-5, x_item+5, y_item+5,
                    fill=color_i, outline=''
                )
                self.canvas_ruleta.create_text(
                    x_item, y_item+15, text=item[:8],
                    fill=color_i, font=("Arial", 9, "bold")
                )
                
                # Línea conexión
                if contador % 2 == 0:
                    self.canvas_ruleta.create_line(
                        x_persona, y_persona, x_item, y_item,
                        fill=random.choice([color_p, color_i]), width=2, dash=(2, 2)
                    )
            
            # Partículas
            for _ in range(5):
                x = random.randint(50, 650)
                y = random.randint(20, 100)
                color = random.choice([
                    self.colores['acento1'], self.colores['acento2'],
                    self.colores['acento3'], self.colores['acento4']
                ])
                self.canvas_ruleta.create_text(x, y, text="✨", fill=color, font=("Arial", 12))
            
            delay = 50 + contador * 5
            self.root.after(delay, lambda: self.animar_mezcla(contador + 1))
        else:
            self.hacer_asignaciones()
    
    def hacer_asignaciones(self):
        """Hacer asignaciones finales"""
        personas_disp = self.personas.copy()
        items_disp = self.items.copy()
        
        random.shuffle(personas_disp)
        random.shuffle(items_disp)
        
        if len(items_disp) <= len(personas_disp):
            for i, item in enumerate(items_disp):
                self.asignaciones[personas_disp[i]] = item
        else:
            indice = 0
            for item in items_disp:
                persona = personas_disp[indice % len(personas_disp)]
                if persona in self.asignaciones:
                    if isinstance(self.asignaciones[persona], list):
                        self.asignaciones[persona].append(item)
                    else:
                        self.asignaciones[persona] = [self.asignaciones[persona], item]
                else:
                    self.asignaciones[persona] = item
                indice += 1
        
        self.mostrar_resultado_final()
    
    def mostrar_resultado_final(self):
        """Mostrar resultado final con animación"""
        self.canvas_ruleta.delete('all')
        
        # Texto de éxito
        self.canvas_ruleta.create_text(
            350, 60, text="✨ ¡ASIGNACIONES COMPLETADAS! ✨",
            fill=self.colores['acento4'], font=("Impact", 20, "bold")
        )
        
        # Efectos visuales
        for _ in range(20):
            x = random.randint(0, 700)
            y = random.randint(0, 120)
            emoji = random.choice(['🎄', '🎁', '⭐', '✨', '🎅', '❄️'])
            color = random.choice([
                self.colores['acento1'], self.colores['acento2'],
                self.colores['acento3'], self.colores['acento4']
            ])
            self.canvas_ruleta.create_text(x, y, text=emoji, fill=color, font=("Arial", 14))
        
        self.actualizar_asignaciones()
        self.guardar_datos()
        self.animacion_activa = False
        self.btn_girar.config(state=tk.NORMAL)
    
    def actualizar_asignaciones(self):
        """Actualizar texto de asignaciones"""
        self.texto_asignaciones.config(state=tk.NORMAL)
        self.texto_asignaciones.delete(1.0, tk.END)
        
        if self.asignaciones:
            for persona, item in sorted(self.asignaciones.items()):
                if isinstance(item, list):
                    items_texto = ", ".join(item)
                    self.texto_asignaciones.insert(tk.END, f"  👤 {persona} ➜ 🎁 {items_texto}\n\n")
                else:
                    self.texto_asignaciones.insert(tk.END, f"  👤 {persona} ➜ 🎁 {item}\n\n")
        else:
            self.texto_asignaciones.insert(tk.END, "  No hay asignaciones. ¡Gira la ruleta mágica!")
        
        self.texto_asignaciones.config(state=tk.DISABLED)
    
    def limpiar_asignaciones(self):
        """Limpiar asignaciones"""
        if self.asignaciones:
            if messagebox.askyesno("🔄", "¿Limpiar todas las asignaciones?"):
                self.asignaciones.clear()
                self.canvas_ruleta.delete('all')
                self.actualizar_asignaciones()
                self.guardar_datos()
    
    def guardar_datos(self):
        """Guardar datos en JSON"""
        datos = {
            'personas': self.personas,
            'items': self.items,
            'asignaciones': self.asignaciones
        }
        try:
            with open('ruleta_datos.json', 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error al guardar: {e}")
    
    def cargar_datos(self):
        """Cargar datos desde JSON"""
        if os.path.exists('ruleta_datos.json'):
            try:
                with open('ruleta_datos.json', 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    self.personas = datos.get('personas', [])
                    self.items = datos.get('items', [])
                    self.asignaciones = datos.get('asignaciones', {})
            except Exception as e:
                print(f"Error al cargar: {e}")

def main():
    root = tk.Tk()
    app = RuletaCompartir(root)
    root.mainloop()

if __name__ == "__main__":
    main()





