from flask import Flask,render_template,request

app = Flask (__name__)

@app.route('/') # A "/" signifa pagina principal!
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    
    user = request.form.get('user')
    password = request.form.get('password')

    if user == "Murillo" and password == "1234":
        return "Acesso liberado 👌"
    else:
        return "Acesso negado ❌"
    
if __name__ == '__main__':
    app.run("0.0.0.0", port=8000) #A DNS 0.0.0.0 permique com que todos possam acessar!