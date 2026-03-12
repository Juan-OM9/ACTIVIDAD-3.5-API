# Importamos las herramientas de Flask
from flask import Flask, request, jsonify

# Inicializamos la aplicación
app = Flask(__name__)

# -----------------------------------------
# ENDPOINT 1: Ruta raíz (GET)
# -----------------------------------------
@app.route('/')
def root():
    return "Home"

# -----------------------------------------
# ENDPOINT 2: Obtener usuario por ID (GET)
# -----------------------------------------
@app.route('/users/<user_id>')
def get_user(user_id):
    # Simulamos un usuario en la base de datos
    user = {
        "id": user_id,
        "name": "test",
        "phone": "999 666 333"
    }
    
    # Verificamos si mandaron un parámetro extra en la URL (query)
    query = request.args.get('query')
    if query:
        user['query'] = query
        
    # Devolvemos los datos en formato JSON y un código 200 (Éxito)
    return jsonify(user), 200

# -----------------------------------------
# ENDPOINT 3: Crear un usuario (POST)
# -----------------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    # Obtenemos la información que nos envían desde Postman
    data = request.json
    
    # Le agregamos un mensaje de estado a esos datos
    data['status'] = 'user created'
    
    # Devolvemos los datos actualizados y un código 201 (Creado)
    return jsonify(data), 201

# -----------------------------------------
# INICIAR EL SERVIDOR
# -----------------------------------------
if __name__ == '__main__':
    # debug=True permite que el servidor se reinicie solo si guardas cambios
    app.run(debug=True)