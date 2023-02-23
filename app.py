from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    data = request.get_json()
    num1 = data["num1"]
    num2 = data["num2"]
    return f"Os valores selecionados foram {num1} e {num2}, e sua soma é {num1 + num2}"
        
if __name__ == '__main__':
    app.run(debug=True)

