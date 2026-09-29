from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "JARVIS ONLINE 24/7"

@app.route('/jarvis', methods=['POST'])
def jarvis():
    data = request.json
    mensaje = data.get('mensaje', '')
    
    respuesta = f"Jarvis recibio: {mensaje} a las {datetime.datetime.now()}"
    
    return jsonify({
        "respuesta": respuesta,
        "status": "online"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
