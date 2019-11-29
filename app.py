from flask import Flask , render_template

#esta varialvel e funcão controlam o debug passo a passo no ambiente de testes
TEST_CONTROL=True
def tests(mensagem):
    """mensagem a ser exibida no durante testes"""
    if(TEST_CONTROL):
        print(str(mensagem))
#remove caracteres e retorna toda a string em lower case
def remover_caracteres(old_string, to_remove):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, ' ')
    return new_string.lower()

#tratamento para '-' de palavras compostas
def substituir_caracteres(old_string, to_remove,to_replace):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, to_replace)
    return new_string.lower()

#!fora de ordem porem 
#a partir do vetor contendo os textos retorna o vocabulario e os vetores contendo as palavras da frase
def gerar_listas_simples(textos,stop_words):
    apagar_caracteres=',.!?-_%&#'
    textoCompleto=str()
    vector={}
    tests(textos)
    vocabulario={}
    j=0
    for i in range(len(textos)):
        #remove caracteres e tratamento de texto
        vector[i]=remover_caracteres(textos[i],apagar_caracteres).split(' ')
        #j representa o indice para a lista de vocabulario
        tests(vector[i])
        for item in range(len(vector[i])):
            #tratamento para eliminar stopwords e adicionar os elementos que nao se repetem
            if (vector[i][item] in stop_words):
                tests('Remove(stopword):'+vector[i][item])
                continue
            if(vector[i][item] in vocabulario):
                tests('Remove(na lista):'+vector[i][item])
                continue
            else:
                tests('Add:'+vector[i][item])
                vocabulario[j]=vector[i][item]
                j=j+1
    tests('Vocabulario '+str(len(vocabulario))+':'+str(vocabulario))
    
    #return vocabulario,vector
def gerar_listas_2gram(textos,stop_words):
    apagar_caracteres=',.!?-_%&#'
    textoCompleto=str()
    vector={}
    tests(textos)
    vocabulario={}
    for i in range(len(textos)):
        vector[i]=remover_caracteres(textos[i],apagar_caracteres).split(' ')
        j=0
        for item in range(len(vector[i])):
            if (vector[i][item] in stop_words):
                tests('Remove:'+vector[i][item])
                continue
            else:
                tests('Add:'+vector[i][item])
                vocabulario[j]=vector[i][item]
                j+=1
    tests('Vocabulario '+str(len(vocabulario))+':'+str(vocabulario))

    #return vocabulario,vector

#conta os elementos e armazena em um dicionario 
#!utiliza como indice uma concatenação entre o indice do vetor e o item ao qual se esta procurando
def contar_e_ignorar(vetores,listaPalavras,stop_words):
    dic=dict()
    listas={}
    for i in range(len(vetores)):
        for item in listaPalavras:
            #ignora palavras inseridas no vetor de StopWords
            if item in stop_words:
                continue
            dic[str(i)+str(item)]=vetores[i].count(item)
            #print pra facilitar a vizualização dos elementos em produção
            #print(str(vetores[i])+'palavra:'+item+str(vetores[i].count(item)))
    return dic

#Formata a saida para mostra o vocabulario e os vetores de incidencia
def formatar_saida(listaPalavras,vetores,lista):
    #dicionario que armazenara o retorno
    dic=dict()
    resultLista=''
    i=1
    for item in listaPalavras:
        resultLista=resultLista+str(i)+'.'+item+' '
        i+=1
    i=0
    dic['vocabulario']=resultLista
    for i in range(len(vetores)):
        #print pra facilitar a vizualização dos elementos em produção
        #print('Vetor De Incidencia['+str(i)+']:'+str(vetores[i]))
        index='texto'+str(i+1)
        retorno=index+' :['
        j=0
        for item in listaPalavras:
            retorno=retorno+str(lista[str(i)+str(item)])
            j+=1
            if(j < len(listaPalavras)):
                retorno=retorno+','
        retorno=retorno+']'
        dic[index]=retorno
    return dic
#função principal para execução da primeira parte do exercicio
def processar_texto(textos,stop_words):
    #listaPalavras,vector=
    gerar_listas_simples(textos,stop_words)
    #gerar teste com resultados da parte 1// 
    #contagem=Contar_E_Ignorar(vector,listaPalavras,stop_words)
    #formatado=Formatar_Saida(listaPalavras,vector,contagem)
    #return formatado 
def processar_texto2(textos,stop_words):
    #listaPalavras,vector=
    #gerar_listas_2gram(textos,stop_words)
    #gerar teste com resultados da parte 1// 
    #contagem=Contar_E_Ignorar(vector,listaPalavras,stop_words)
    #formatado=Formatar_Saida(listaPalavras,vector,contagem)
    return  

    
myapp = Flask(__name__)

#home page
@myapp.route("/")
def cinnecta():
    return render_template('index.html')
@myapp.route("/manual")
def manual():
    return render_template('manual.html')

@myapp.route("/gram1")
def gramatica1():
    #entrada esperada
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    #StopWords adicionadas em um vetor
    stop_words='',''
    vocabulario=processar_texto(e,stop_words)

    return render_template('lista.html',format=vocabulario)
        
@myapp.route("/gram2")
def gramatica2():
    #entrada esperada
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    #StopWords adicionadas em um vetor
    stop_words='',''
    vocabulario=processar_texto2(e,stop_words)

    return render_template('lista.html',format=vocabulario)


if __name__=="__main__":
    myapp.run()