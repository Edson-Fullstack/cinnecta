from flask import Flask
def fatorial(numero):
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)
    
app = Flask(__name__)

#home page
@app.route("/")
def cinnecta():
    return "Hello World"

if __name__=="__main__":
    app.run()