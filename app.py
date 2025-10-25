from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello, World!",
        "version": "1.0",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "uptime": "running"
    }), 200

@app.route("/api/multiply/<int:a>/<int:b>")
def multiply(a, b):
    result = a * b
    return jsonify({
        "operand1": a,
        "operand2": b,
        "result": result,
        "operation": "multiply"
    }), 200

@app.route("/api/info")
def info():
    return jsonify({
        "app_name": "Flask Matrix Calculator",
        "endpoints": [
            "/",
            "/health",
            "/api/multiply/<int:a>/<int:b>",
            "/api/info"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)