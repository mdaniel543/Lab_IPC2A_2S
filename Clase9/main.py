from flask import Flask, request, jsonify
from xml.etree import ElementTree as ET
import re
import os

app = Flask(__name__)

XML_FILE = 'Clase9/db.xml'

@app.route('/')
def index():
    return "API de Flask para procesar datos XML. Y retornar un JSON"

@app.route('/process', methods=['POST'])
def process_xml():
    xml_data = request.data
    root = ET.fromstring(xml_data)
    
    # Cargar XML existente
    if os.path.exists(XML_FILE):
        tree = ET.parse(XML_FILE)
        elementos = tree.getroot()
    else:
        elementos = ET.Element("elementos")
        
          
    for dato in root.findall('dato'):
        correo = dato.find('correo').text.strip()
        nombre = dato.find('nombre').text
        alias_ = dato.find('nombre').get('alias')
        correo_valido = is_valid_email(correo)
        obj = {
            'nombre': nombre.split(alias_)[0],
            'alias': nombre.split(alias_)[1],
            'correo': correo,
            'correoValido': correo_valido
        }
        # Comprobar si el alias ya existe en el archivo XML
        if any(elemento.find('alias').text == obj['alias'] for elemento in elementos):
            continue
        # Crear elemento XML
        elemento = ET.SubElement(elementos, "elemento")
        ET.SubElement(elemento, "nombre").text = obj['nombre']
        ET.SubElement(elemento, "alias").text = obj['alias']
        ET.SubElement(elemento, "correo").text = obj['correo']
        ET.SubElement(elemento, "correoValido").text = str(obj['correoValido'])
        
    # Guardar XML
    tree = ET.ElementTree(elementos)
    tree.write(XML_FILE)        
    return jsonify({"message": "Datos procesados correctamente"})

def is_valid_email(email):
    # Expresión regular simple para validar emails
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


@app.route('/get-data', methods=['GET'])
def get_data():
    # Comprobar si el archivo XML existe
    if not os.path.exists(XML_FILE):
        return jsonify({"error": "No hay datos disponibles"}), 404

    # Cargar XML existente
    tree = ET.parse(XML_FILE)
    elementos = tree.getroot()
    result_list = []

    for elemento in elementos.findall('elemento'):
        nombre = elemento.find('nombre').text
        alias_ = elemento.find('alias').text
        correo = elemento.find('correo').text
        correo_valido = elemento.find('correoValido').text == 'True'
        obj = {
            'nombre': nombre,
            'alias': alias_,
            'correo': correo,
            'correoValido': correo_valido
        }
        result_list.append(obj)

    return jsonify(result_list), 200


@app.route('/stats', methods=['GET'])
def get_stats():
    # Comprobar si el archivo XML existe
    if not os.path.exists(XML_FILE):
        return jsonify({"error": "No hay datos disponibles"}), 404

    # Cargar XML existente
    tree = ET.parse(XML_FILE)
    elementos = tree.getroot()

    nombres = []
    correos_validos = 0
    correos_invalidos = 0

    for elemento in elementos.findall('elemento'):
        nombre = elemento.find('nombre').text
        nombres.append(nombre)
        
        if elemento.find('correoValido').text == 'True':
            correos_validos += 1
        else:
            correos_invalidos += 1
            
    nombres_repetidos = len(nombres) - len(set(nombres))

    response = {
        "nombresRepetidos": nombres_repetidos,
        "correosValidos": correos_validos,
        "correosInvalidos": correos_invalidos
    }

    return jsonify(response), 200


def get_data_as_dict():
    # Comprobar si el archivo XML existe
    if not os.path.exists(XML_FILE):
        return None

    # Cargar XML existente
    tree = ET.parse(XML_FILE)
    elementos = tree.getroot()

    result_dict = {}

    for elemento in elementos.findall('elemento'):
        nombre = elemento.find('nombre').text
        alias_ = elemento.find('alias').text
        correo = elemento.find('correo').text
        correo_valido = elemento.find('correoValido').text == 'True'

        obj = {
            'nombre': nombre,
            'alias': alias_,
            'correo': correo,
            'correoValido': correo_valido
        }

        # Usamos el alias como clave
        result_dict[alias_] = obj

    return result_dict

@app.route('/search-by-alias/<alias>', methods=['GET'])
def search_by_alias(alias):
    data_dict = get_data_as_dict()

    if data_dict is None:
        return jsonify({"error": "No hay datos disponibles"}), 404

    if alias in data_dict:
        return jsonify(data_dict[alias]), 200
    else:
        return jsonify({"error": "Alias no encontrado"}), 404




if __name__ == '__main__':
    app.run(debug=True)
