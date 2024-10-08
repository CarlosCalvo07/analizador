from flask import Flask, request, render_template
from lexico2 import lexico
from sintactico2 import sintactico

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        
        # Realizar el análisis léxico
        tokens = lexico(text)
        
        # Realizar el análisis sintáctico
        sintactico_result = sintactico(text)
        
        return render_template('virtual.html', tokens=tokens, text=text, sintactico_result=sintactico_result)
    
    return render_template('virtual.html', tokens=None, text=None, sintactico_result=None)

if __name__ == '__main__':
    app.run(debug=True)