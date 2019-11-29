#teste
from flask import Flask
from collections import defaultdict
#contar elementos
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
    completeText=Substituir_Caracteres(textoCompleto,substituirCaracteres[0],substituirCaracteres[1])
    completeText=Remover_Caracteres(completeText,deletarCaracteres)
    completeText=completeText.split(' ')
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
            dic[str(i)+str(item)]=vetores[i].count(item)
            #print(str(vetores[i])+'palavra:'+item+str(vetores[i].count(item)))
    return dic

def Formatar_Saida(listaPalavras,vetores,lista):
    i=1
    resultLista=''
    for item in listaPalavras:
        resultLista=resultLista+str(i)+'.'+item+'<br>'
        i+=1
    for i in range(len(vetores)):
        #print('Vetor De Incidencia['+str(i)+']:'+str(vetores[i]))
        retorno='['
        j=0
        for item in listaPalavras:
            retorno=retorno+str(lista[str(i)+str(item)])
            j+=1
            if(j < len(listaPalavras)):
                retorno=retorno+','
        retorno=retorno+']<br>'
        resultLista=resultLista+retorno
    return resultLista

def Gramatica(textos,stopWords):
    listaPalavras,vector=Gerar_Listas_Simples(textos)
    #gerar teste com resultados da parte 1// 
    contagem=Contar_E_Ignorar(vector,listaPalavras,stopWords)
    saida=Formatar_Saida(listaPalavras,vector,contagem)
    return saida 
app = Flask(__name__)

#home page
@app.route("/")
def cinnecta():
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    stopWords='',''
    return Gramatica(e,stopWords)


if __name__=="__main__":
    app.run()