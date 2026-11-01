<<<<<<< HEAD
# ruleta
=======
# 🎄 Ruleta de Compartir Navideña Futurista 🎅

Aplicación interactiva con diseño navideño futurista para asignar aleatoriamente items/cosas a personas para un evento de compartir.

## ✨ Características Principales

### 🎨 Diseño Visual Impresionante
- **Tema Navideño Futurista**: Colores neón (rojo, verde, cyan, dorado) sobre fondo oscuro espacial
- **Fondo Animado**: 100 estrellas en movimiento continuo que caen como nieve
- **Efectos Visuales**: Partículas brillantes y emojis navideños durante las animaciones

### 🎰 Animación de Ruleta Espectacular
- **Mezcla Visual en Tiempo Real**: Ve cómo las personas y los items se mezclan en pantalla
- **Flechas Giratorias**: Rayos ⚡ que giran conectando personas con items
- **Líneas Parpadeantes**: Conexiones visuales que muestran las posibles asignaciones
- **30 Frames de Animación**: Aceleración progresiva para mayor emoción
- **Celebración Final**: Explosión de emojis navideños 🎄🎁⭐✨🎅❄️

### 📋 Funcionalidad Completa
- **Gestión de Personas**: Agrega y elimina participantes con interfaz futurista
- **Gestión de Items**: Agrega y elimina cosas que llevar
- **Asignaciones Inteligentes**: 
  - Si hay más personas que items: asigna un item por persona
  - Si hay más items que personas: distribuye equitativamente
- **Persistencia de Datos**: Guarda automáticamente en archivo JSON
- **Interfaz Intuitiva**: Presiona Enter para agregar rápidamente

## 🚀 Cómo Usar

1. **Ejecutar la aplicación**:
   ```bash
   python ruleta_compartir.py
   ```

2. **Agrega Personas** (Panel Verde):
   - Escribe un nombre en el campo
   - Presiona Enter o clic en "➕"
   - Ejemplo: Juan, María, Pedro, Ana, Carlos

3. **Agrega Items** (Panel Dorado):
   - Escribe un item en el campo
   - Presiona Enter o clic en "➕"
   - Ejemplos: Refrescos, Platos, Vasos, Pastel, Bocadillos, Servilletas

4. **¡Gira la Ruleta Mágica!**:
   - Clic en el botón "🎰 GIRAR RULETA MÁGICA 🎰"
   - Observa la espectacular animación:
     - Las personas aparecen arriba con círculos de colores neón
     - Los items aparecen abajo con círculos brillantes
     - Las flechas giran conectándolos
     - Las líneas parpadean mostrando conexiones
     - Partículas ✨ vuelan por toda el área
   - ¡Espera la celebración final con emojis navideños!

5. **Ver Resultados**:
   - Las asignaciones aparecen en el panel inferior
   - Formato: 👤 Persona ➜ 🎁 Item(s)

6. **Gestionar Datos**:
   - Selecciona y usa "🗑️ ELIMINAR" para quitar personas o items
   - Usa "🔄 LIMPIAR TODO" para resetear las asignaciones

## 🎨 Paleta de Colores Navideña Futurista

- **Fondo Espacial**: `#0a0e27` (Azul oscuro profundo)
- **Rojo Neón**: `#ff1744` (Navideño brillante)
- **Verde Neón**: `#00e676` (Árbol de Navidad futurista)
- **Cyan Neón**: `#00b8d4` (Hielo brillante)
- **Dorado Neón**: `#ffd600` (Estrellas y regalos)

## 💫 Efectos Especiales

### Durante la Animación:
- 6 parejas persona-item se muestran simultáneamente
- Los rayos ⚡ giran 360° cada frame
- Los colores cambian aleatoriamente cada iteración
- 5 partículas ✨ aparecen en posiciones aleatorias
- Las líneas de conexión parpadean con efecto de guiones
- La velocidad aumenta progresivamente (50ms → 200ms)

### En el Resultado Final:
- Texto gigante "✨ ¡ASIGNACIONES COMPLETADAS! ✨"
- 20 emojis navideños dispersos aleatoriamente
- Colores neón brillantes para cada emoji

## 💾 Persistencia

Los datos se guardan automáticamente en `ruleta_datos.json` y se cargan al iniciar la aplicación.

## 🎯 Ejemplo de Uso

Para un compartir navideño de oficina:

**Personas:** Juan, María, Pedro, Ana, Carlos, Lucía

**Items:** Refrescos, Platos y cubiertos, Vasos, Pastel, Bocadillos, Servilletas, Decoración

Al girar la ruleta, verás una espectacular animación futurista donde personas e items se mezclan visualmente hasta que la magia navideña hace la asignación perfecta! 🎄✨

## 📦 Requisitos

- Python 3.x
- tkinter (incluido en la mayoría de instalaciones de Python)
- Módulos estándar: random, json, os, math

## 🎁 Características Técnicas

- **Resolución**: 1200x850 pixels
- **FPS Animación**: ~20 FPS (50ms por frame)
- **Frames Totales**: 30 frames de mezcla + resultado final
- **Partículas de Fondo**: 100 estrellas en movimiento continuo
- **Duración Animación**: ~2.5 segundos

¡Disfruta organizando tus compartires navideños con esta increíble ruleta futurista! 🎅🎄✨🎁

>>>>>>> d00da77 (Ruleta Web App - Flask glassmorphism app ready for Render)
