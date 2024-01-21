from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Phaeton Project!'

if __name__ == '__main__':
    # Nastavení host na '0.0.0.0' umožní přístup k aplikaci z vnější sítě
    # Výchozí port je 5000, můžete ho změnit podle potřeby
    app.run(host='0.0.0.0', port=5000, debug=True)