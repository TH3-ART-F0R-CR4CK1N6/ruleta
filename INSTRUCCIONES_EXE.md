# 🎄 RULETA NAVIDEÑA FUTURISTA 🎅
## Ejecutable Standalone - Sin necesidad de Python

---

## 📦 CONTENIDO DEL PAQUETE

✅ **RuletaNavideña.exe** - Ejecutable independiente (10 MB)
- No requiere Python instalado
- Funciona en Windows 7/8/10/11
- Incluye todas las dependencias

---

## 🚀 INSTRUCCIONES DE USO

### Opción 1: Usar el Ejecutable (.exe)

1. **Ir a la carpeta `dist`**
2. **Ejecutar `RuletaNavideña.exe`**
3. ¡Listo! La aplicación se abrirá automáticamente

### Opción 2: Ejecutar desde Python

```bash
python ruleta_compartir.py
```

---

## 🎨 CARACTERÍSTICAS VISUALES

### 🌟 Fondo Animado Espacial
- 100 estrellas brillantes en movimiento continuo
- Efecto de nieve espacial navideña
- Colores neón: cyan, dorado y blanco

### 🎰 Animación de Ruleta Espectacular
- **30 frames** de animación suave
- **6 parejas** persona-item simultáneas
- **Círculos neón** para personas e items
- **Rayos ⚡ giratorios** (360° de rotación)
- **Líneas parpadeantes** de conexión
- **Partículas ✨** brillantes volando

### 🎉 Celebración Final
- Texto gigante de éxito
- 20 emojis navideños: 🎄🎁⭐✨🎅❄️
- Colores neón aleatorios brillantes

### 🎨 Paleta de Colores Neón
- **Fondo Espacial**: Azul oscuro profundo
- **Rojo Neón**: Navideño brillante
- **Verde Neón**: Árbol de Navidad futurista
- **Cyan Neón**: Hielo brillante
- **Dorado Neón**: Estrellas y regalos

---

## 📝 GUÍA RÁPIDA DE USO

### 1️⃣ Agregar Participantes (Panel Verde)
- Escribe el nombre
- Presiona **Enter** o clic en **➕**
- Ejemplo: Juan, María, Pedro, Ana, Carlos

### 2️⃣ Agregar Items (Panel Dorado)
- Escribe el item que debe llevar
- Presiona **Enter** o clic en **➕**
- Ejemplo: Refrescos, Pastel, Platos, Vasos, Bocadillos

### 3️⃣ ¡Girar la Ruleta Mágica!
- Clic en **🎰 GIRAR RULETA MÁGICA 🎰**
- Observa la espectacular animación:
  - Personas aparecen arriba (círculos de colores)
  - Items aparecen abajo (círculos brillantes)
  - Rayos ⚡ giran conectándolos
  - Líneas parpadean mostrando conexiones
  - Partículas ✨ vuelan por el área
- ¡Espera la celebración final! 🎄✨

### 4️⃣ Ver Resultados
- Panel inferior muestra las asignaciones
- Formato: **👤 Persona ➜ 🎁 Item(s)**

### 5️⃣ Gestionar Datos
- **🗑️ ELIMINAR**: Quitar personas o items
- **🔄 LIMPIAR TODO**: Resetear asignaciones

---

## 💡 ASIGNACIONES INTELIGENTES

El sistema distribuye los items automáticamente:

- **Más personas que items**: Cada persona recibe un item único
- **Más items que personas**: Distribuye equitativamente entre todos
- **Múltiples items**: Una persona puede llevar varios items si es necesario

---

## 💾 DATOS PERSISTENTES

Los datos se guardan automáticamente en `ruleta_datos.json`:
- Lista de personas
- Lista de items
- Últimas asignaciones

Al abrir la aplicación, recupera todo automáticamente.

---

## 🎯 EJEMPLO DE USO

**Para un compartir navideño de oficina:**

**Personas:**
Juan, María, Pedro, Ana, Carlos, Lucía

**Items:**
Refrescos, Platos y cubiertos, Vasos, Pastel, Bocadillos, Servilletas, Decoración

**Resultado:**
La ruleta mágica hará una asignación justa y visual espectacular! 🎄✨

---

## 📦 DISTRIBUCIÓN

### Para compartir con otros:

1. **Copiar el archivo `RuletaNavideña.exe`** de la carpeta `dist`
2. **Enviarlo** por correo, USB, o nube
3. **Ejecutar** directamente - No necesita instalación

### Tamaño del archivo:
- **EXE**: ~10 MB
- Incluye Python + tkinter + todas las dependencias

---

## 🛠️ PARA DESARROLLADORES

### Recompilar el Ejecutable:

```bash
# Opción 1: Usar el script batch
compilar_exe.bat

# Opción 2: Comando directo
pyinstaller --onefile --windowed --name "RuletaNavideña" ruleta_compartir.py
```

### Requisitos para desarrollo:
```bash
pip install pyinstaller
```

### Estructura de archivos:
```
Ruleta/
├── ruleta_compartir.py      # Código fuente principal
├── ruleta_datos.json         # Datos persistentes
├── compilar_exe.bat          # Script de compilación
├── README.md                 # Documentación principal
├── INSTRUCCIONES_EXE.md      # Este archivo
├── dist/
│   └── RuletaNavideña.exe    # Ejecutable compilado
└── build/                    # Archivos temporales de compilación
```

---

## 🎁 CARACTERÍSTICAS TÉCNICAS

- **Resolución**: 1200x850 pixels
- **FPS**: ~20 FPS (50ms por frame)
- **Frames de animación**: 30 frames + celebración final
- **Partículas de fondo**: 100 estrellas animadas
- **Duración animación**: ~2.5 segundos
- **Peso del ejecutable**: 10.1 MB
- **Plataforma**: Windows 7/8/10/11 (64-bit)

---

## 🎅 SOPORTE Y CONTACTO

¿Tienes preguntas o sugerencias?
- El código fuente está en `ruleta_compartir.py`
- Totalmente personalizable y modificable
- Diseñado con Python + tkinter

---

## ⚡ TIPS Y TRUCOS

1. **Atajos de teclado**:
   - Presiona **Enter** en cualquier campo para agregar rápidamente

2. **Múltiples asignaciones**:
   - Si tienes 5 personas y 10 items, cada persona recibirá 2 items

3. **Nombres largos**:
   - La animación muestra solo 8 caracteres
   - Las asignaciones finales muestran el nombre completo

4. **Persistencia**:
   - Cierra y abre la app - tus datos siguen ahí
   - Elimina `ruleta_datos.json` para empezar desde cero

---

## 🎄 ¡DISFRUTA TU COMPARTIR NAVIDEÑO! 🎅✨

**¡Felices fiestas y que la ruleta mágica decida por ti!** 🎁🎉

---

*Versión 1.0 - Noviembre 2026*
*Ruleta Navideña Futurista - Sistema de Asignación Inteligente*
