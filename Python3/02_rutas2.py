from flask import Flask

app = Flask(__name__)

@app.route('/api/temperatura/<grados_c>', methods=['GET'])
def temperatura(grados_c: str) -> str:
    # Convertir a float
    grados_c = float(grados_c)
    farenheit: float = (grados_c * 9/5) + 32
    
    return f"Grados: {grados_c} | Fahrenheit: {farenheit}"

if __name__ == '__main__':
    app.run(debug=True)
