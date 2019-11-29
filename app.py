#teste
from flask import Flask
from flask import jsonify
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

def Gerar_Listas_Simples(textos):
    deletarCaracteres=',!.'
    substituirCaracteres='-',' '
    textoCompleto=str()
    vector={}
    index=0
    for texto in textos:
        textoCompleto=textoCompleto+' '+texto
        vector[index]=Remover_Caracteres(texto,deletarCaracteres)
        vector[index]=Substituir_Caracteres(vector[index],substituirCaracteres[0],substituirCaracteres[1])
        vector[index]=vector[index].split(' ')
        index+=1
    completeText=Remover_Caracteres(textoCompleto,deletarCaracteres)
    completeText=Substituir_Caracteres(completeText,substituirCaracteres[0],substituirCaracteres[1])
    completeText=completeText.split(' ')
    
    #for item in stopWords:
    #    if item in completeText:
    #        completeText.remove(item)
    listaPalavras=set(completeText)
    if '' in listaPalavras:
        listaPalavras.remove('')
    return listaPalavras,vector

def Contar_E_Ignorar(vetores,listaPalavras,stopWords):
    dic=dict()
    listas={}
    for i in range(len(vetores)):
        for item in listaPalavras:
            if item in stopWords:
                continue
            dic[item]=vetores[i].count(item)
        listas[i]=dic
    return listas
def Formatar_Saida(listaPalavras,vetores,lista):
    print('Lista'+str(len(listaPalavras))+':'+str(listaPalavras))
    for i in range(len(vetores)):
        print('Vetor De Incidencia['+str(i)+']:'+str(vetores[i]))
        print('Lista De Contagem['+str(i)+']:'+str(lista[i]))


def Gramatica(textos,stopWords):
    listaPalavras,vector=Gerar_Listas_Simples(textos)
    #gerar teste com resultados da parte 1// 
    listas=Contar_E_Ignorar(vector,listaPalavras,stopWords)
    Formatar_Saida(listaPalavras,vector,listas)
    return 
app = Flask(__name__)

#home page
@app.route("/")
def cinnecta():
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    stopWords='',''
    Gramatica(e,stopWords);
    return ''


if __name__=="__main__":
    app.run()