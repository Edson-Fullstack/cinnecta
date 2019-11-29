from flask import Flask


#remove caracteres e retorna toda a string em lower case
def Remover_Caracteres(old_string, to_remove):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, '')
    return new_string.lower()

#tratamento para - de palavras compostas
def Substituir_Caracteres(old_string, to_remove,to_replace):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, to_replace)
    return new_string.lower()

#a partir do vetor contendo os textos retorna o vocabulario e os vetores contendo as palavras da frase
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
    completeText=sorted(completeText.split(' '))
    vocabulario=set(completeText)
    if '' in vocabulario:
        vocabulario.remove('')
    return vocabulario,vector

#conta os elementos e armazena em um dicionario 
#!utiliza como indice uma concatenação entre o indice do vetor e o item ao qual se esta procurando
def Contar_E_Ignorar(vetores,listaPalavras,stopWords):
    dic=dict()
    listas={}
    for i in range(len(vetores)):
        for item in listaPalavras:
            #ignora palavras inseridas no vetor de StopWords
            if item in stopWords:
                continue
            dic[str(i)+str(item)]=vetores[i].count(item)
            #print pra facilitar a vizualização dos elementos em produção
            #print(str(vetores[i])+'palavra:'+item+str(vetores[i].count(item)))
    return dic

#Formata a saida para mostra o vocabulario e os vetores de incidencia
def Formatar_Saida(listaPalavras,vetores,lista):
    i=1
    resultLista='Vocabulário:<br>'
    for item in listaPalavras:
        resultLista=resultLista+str(i)+'.'+item+'<br>'
        i+=1
    for i in range(len(vetores)):
        #print pra facilitar a vizualização dos elementos em produção
        #print('Vetor De Incidencia['+str(i)+']:'+str(vetores[i]))
        retorno='texto '+str(i)+' :['
        j=0
        for item in listaPalavras:
            retorno=retorno+str(lista[str(i)+str(item)])
            j+=1
            if(j < len(listaPalavras)):
                retorno=retorno+','
        retorno=retorno+']<br>'
        resultLista=resultLista+retorno
    return resultLista

#função principal para execução da primeira parte do exercicio
def Gramatica(textos,stopWords):
    listaPalavras,vector=Gerar_Listas_Simples(textos)
    #gerar teste com resultados da parte 1// 
    contagem=Contar_E_Ignorar(vector,listaPalavras,stopWords)
    saida=Formatar_Saida(listaPalavras,vector,contagem)
    return saida 
app = Flask(__name__)

#home page
@app.route("/gram")
def cinnecta():
    #entrada esperada
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    #StopWords adicionadas em um vetor
    stopWords='',''
    return Gramatica(e,stopWords)

@app.route("/gram2")
def cinnecta2():
    #entrada esperada
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    #StopWords adicionadas em um vetor
    stopWords='',''
    return Gramatica(e,stopWords)


if __name__=="__main__":
    app.run()