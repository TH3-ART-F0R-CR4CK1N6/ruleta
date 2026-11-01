from flask import Flask, render_template, jsonify, request
import random
import json
import os

app = Flask(__name__)

# Archivo de datos
DATA_FILE = 'ruleta_datos.json'

def cargar_datos():
    """Cargar datos desde archivo JSON"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {'personas': [], 'items': [], 'asignaciones': {}}

def guardar_datos(datos):
    """Guardar datos en archivo JSON"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    """Obtener todos los datos"""
    return jsonify(cargar_datos())

@app.route('/api/personas', methods=['POST'])
def agregar_persona():
    """Agregar una persona"""
    datos = cargar_datos()
    persona = request.json.get('nombre', '').strip()
    
    if not persona:
        return jsonify({'error': 'Nombre vacío'}), 400
    
    if persona in datos['personas']:
        return jsonify({'error': 'Persona ya existe'}), 400
    
    datos['personas'].append(persona)
    guardar_datos(datos)
    return jsonify({'success': True, 'datos': datos})

@app.route('/api/personas/<nombre>', methods=['DELETE'])
def eliminar_persona(nombre):
    """Eliminar una persona"""
    datos = cargar_datos()
    
    if nombre in datos['personas']:
        datos['personas'].remove(nombre)
        if nombre in datos['asignaciones']:
            del datos['asignaciones'][nombre]
        guardar_datos(datos)
        return jsonify({'success': True, 'datos': datos})
    
    return jsonify({'error': 'Persona no encontrada'}), 404

@app.route('/api/items', methods=['POST'])
def agregar_item():
    """Agregar un item"""
    datos = cargar_datos()
    item = request.json.get('nombre', '').strip()
    
    if not item:
        return jsonify({'error': 'Item vacío'}), 400
    
    if item in datos['items']:
        return jsonify({'error': 'Item ya existe'}), 400
    
    datos['items'].append(item)
    guardar_datos(datos)
    return jsonify({'success': True, 'datos': datos})

@app.route('/api/items/<nombre>', methods=['DELETE'])
def eliminar_item(nombre):
    """Eliminar un item"""
    datos = cargar_datos()
    
    if nombre in datos['items']:
        datos['items'].remove(nombre)
        # Eliminar asignaciones relacionadas
        for persona in list(datos['asignaciones'].keys()):
            if datos['asignaciones'][persona] == nombre:
                del datos['asignaciones'][persona]
        guardar_datos(datos)
        return jsonify({'success': True, 'datos': datos})
    
    return jsonify({'error': 'Item no encontrado'}), 404

@app.route('/api/girar', methods=['POST'])
def girar_ruleta():
    """Girar la ruleta y hacer asignaciones"""
    datos = cargar_datos()
    
    if not datos['personas']:
        return jsonify({'error': 'No hay personas'}), 400
    
    if not datos['items']:
        return jsonify({'error': 'No hay items'}), 400
    
    # Limpiar asignaciones anteriores
    datos['asignaciones'] = {}
    
    # Crear copias y mezclar
    personas = datos['personas'].copy()
    items = datos['items'].copy()
    random.shuffle(personas)
    random.shuffle(items)
    
    # Hacer asignaciones
    if len(items) <= len(personas):
        for i, item in enumerate(items):
            datos['asignaciones'][personas[i]] = item
    else:
        indice = 0
        for item in items:
            persona = personas[indice % len(personas)]
            if persona in datos['asignaciones']:
                if isinstance(datos['asignaciones'][persona], list):
                    datos['asignaciones'][persona].append(item)
                else:
                    datos['asignaciones'][persona] = [datos['asignaciones'][persona], item]
            else:
                datos['asignaciones'][persona] = item
            indice += 1
    
    guardar_datos(datos)
    return jsonify({'success': True, 'asignaciones': datos['asignaciones']})

@app.route('/api/limpiar', methods=['POST'])
def limpiar_asignaciones():
    """Limpiar todas las asignaciones"""
    datos = cargar_datos()
    datos['asignaciones'] = {}
    guardar_datos(datos)
    return jsonify({'success': True, 'datos': datos})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
