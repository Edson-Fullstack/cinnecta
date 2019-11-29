from flask import Flask , render_template

#esta varialvel e funcão controlam o debug passo a passo no ambiente de testes
TEST_CONTROL=1
def tests(controle,mensagem):
    """mensagem a ser exibida no durante testes"""
    if(TEST_CONTROL>=controle):
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



#conta os elementos e armazena em um dicionario 
#!utiliza como indice uma concatenação entre o indice do vetor e o item ao qual se esta procurando
def contar(vetores,vocabulario,gramatica):
    dicionario=dict()
    if(gramatica=='gram1'):
        for i in range(len(vetores)):
            for item in vocabulario:
                dicionario['texto'+str(i+1)+vocabulario[item]]=vetores[i].count(vocabulario[item])
    if(gramatica=='gram2'):
        for i in range(len(vetores)):
            for item in range(len(vetores[i])-1):
                analise=vetores[i][item]+' '+vetores[i][item+1]
                #print(vocabulario)
                for j in vocabulario:
                    print(vocabulario[j])
                    if(vocabulario[j]==analise):
                        key={vetores[i][item]+vetores[i][item+1]}
                        dicionario[key]+=1

                tests(1,analise)
    
    tests(1,'Dicionario:'+str(dicionario)) 
    return 

#a partir do vetor contendo os textos retorna o vocabulario e os vetores contendo as palavras da frase
def gerar_listas_simples(textos,stop_words,gramatica):
    apagar_caracteres=',.!?-_%&#'
    textoCompleto=str()
    vector={}
    tests(1,textos)
    vocabulario_set=set()
    vocabulario={}
    j=0
    for i in range(len(textos)):
        #remove caracteres e tratamento de texto
        vector[i]=remover_caracteres(textos[i],apagar_caracteres).split(' ')
        #j representa o indice para a lista de vocabulario
        #retirar elementos vazios do vetor
        while('' in vector[i]):
            vector[i].remove('')
        if(gramatica=="gram1"):
            alterar=0
        if(gramatica=="gram2"):
            alterar=-1
        for item in range(len(vector[i])+alterar):
            if(gramatica=="gram1"):
                analise=vector[i][item]
            if(gramatica=="gram2"):
                analise=vector[i][item]+' '+vector[i][item+1]
            tests(2,'Analise:'+analise)
            #tratamento para eliminar stopwords e adicionar os elementos que nao se repetem
            if (analise in stop_words):
                tests(2,'Remove(stopword):'+analise)
                continue
            elif (analise not in vocabulario_set):
                tests(2,'Add:'+analise)
                vocabulario_set.add(analise)
                vocabulario[j]=analise
                j=j+1
            else:
                tests(2,'Remove:'+vector[i][item])
    tests(1,'Vocabulario'+gramatica+'['+str(len(vocabulario))+']:'+str(vocabulario))
    
    return vocabulario,vector

#função principal para execução da primeira parte do exercicio
def processar_texto(textos,stop_words,gramatica):
    vocabulario,vector=gerar_listas_simples(textos,stop_words,gramatica)
    #gerar teste com resultados da parte 1// 
    contagem=contar(vector,vocabulario,gramatica)
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
    vocabulario=processar_texto(e,stop_words,'gram1')

    return render_template('lista.html')
        
@myapp.route("/gram2")
def gramatica2():
    #entrada esperada
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    #StopWords adicionadas em um vetor
    stop_words='',''
    vocabulario=processar_texto(e,stop_words,'gram2')

    return render_template('lista.html')


if __name__=="__main__":
    myapp.run()