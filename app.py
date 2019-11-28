#teste
from flask import Flask
#contar elementos
from collections import Counter
import json
def fatorial(numero):
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)

#remove caracteres e retorna toda a string em lower case
def Remover_Caracteres(old_string, to_remove):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, '')
    return new_string.lower()
def Substituir_Caracteres(old_string, to_remove,to_replace):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, to_replace)
    return new_string.lower()
def Contar_Palavras(vector):
    print(Counter(vector))


app = Flask(__name__)

#home page
@app.route("/")
def cinnecta():
    e1='Falar é fácil. Mostre-me o código.'
    e2='É fácil escrever código. Difícil é escrever código que funcione.'
    e=(e1+' '+e2)
    deletarCaracteres=',!.'
    substituirCaracteres='-',' '
    baseText=Remover_Caracteres(e,deletarCaracteres)
    baseText=Substituir_Caracteres(baseText,substituirCaracteres[0],substituirCaracteres[1])
    #gerar teste com resultados da parte 1//1. falar 2. é 3. fácil 4. mostre 5. me 6. o 7. código 8. escrever 9. difícil 10. que 11. funcione
    baseVector=baseText.split(" ")

    return jsonify(baseText)


if __name__=="__main__":
    app.run()