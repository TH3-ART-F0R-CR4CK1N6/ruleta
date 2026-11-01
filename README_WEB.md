# Aplicación Web Ruleta

Aplicación web moderna para sorteos navideños con diseño profesional y elegante.

## 🌟 Características

- **Diseño Moderno**: Interfaz glassmorphism con gradientes y animaciones
- **Responsive**: Se adapta a cualquier dispositivo
- **Animaciones Elegantes**: Canvas HTML5 con efectos visuales
- **API REST**: Backend Flask con endpoints RESTful
- **Persistencia**: Los datos se guardan automáticamente

## 🚀 Despliegue en Render

### Opción 1: Desde GitHub

1. Sube el código a GitHub
2. Ve a [Render.com](https://render.com) y crea una cuenta
3. Click en "New +" → "Web Service"
4. Conecta tu repositorio de GitHub
5. Configuración:
   - **Name**: ruleta-app (o el nombre que prefieras)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free
6. Click en "Create Web Service"

### Opción 2: Deploy Manual

```bash
# 1. Instalar Render CLI
npm install -g @render/cli

# 2. Login
render login

# 3. Deploy
render deploy
```

## 💻 Desarrollo Local

### Requisitos
- Python 3.8 o superior

### Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📁 Estructura del Proyecto

```
Ruleta/
├── app.py                 # Backend Flask
├── requirements.txt       # Dependencias Python
├── Procfile              # Configuración Render
├── ruleta_datos.json     # Datos persistentes
├── templates/
│   └── index.html        # Interfaz principal
└── static/
    ├── css/
    │   └── styles.css    # Estilos
    └── js/
        └── app.js        # Lógica frontend
```

## 🎨 Características de Diseño

- **Colores**: Tema navideño profesional (rojo #c41e3a, verde #0f5132, dorado #d4af37)
- **Efectos**: Glassmorphism, gradientes, sombras, animaciones
- **Tipografía**: Poppins de Google Fonts
- **Background**: Animación de estrellas

## 🔧 API Endpoints

- `GET /api/datos` - Obtener todos los datos
- `POST /api/personas` - Agregar persona
- `DELETE /api/personas/<nombre>` - Eliminar persona
- `POST /api/items` - Agregar item
- `DELETE /api/items/<nombre>` - Eliminar item
- `POST /api/girar` - Realizar sorteo
- `POST /api/limpiar` - Limpiar asignaciones

## 📝 Uso

1. **Agregar Personas**: Ingresa nombres en el panel izquierdo
2. **Agregar Items**: Ingresa items en el panel derecho
3. **Girar Ruleta**: Click en el botón grande para sortear
4. **Ver Resultados**: Las asignaciones aparecen abajo
5. **Limpiar**: Botón para reiniciar las asignaciones

## 🎄 Versión Desktop

También disponible como aplicación de escritorio con tkinter. Ver `ruleta_compartir.py`

## 📄 Licencia

Uso personal y educativo

---

Desarrollado con ❤️ para sorteos navideños
