from flask import Flask , render_template

#esta varialvel e funcão controlam o debug passo a passo no ambiente de testes
TEST_CONTROL=1
def tests(controle,mensagem):
    """mensagem a ser exibida no durante testes"""
    if(TEST_CONTROL>=controle):
        print(str(mensagem))

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
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


def contar_incidencia(vetor,vocabulario):
    dicionario=dict()
    for i in range(len(vetor)):
        for item in vocabulario:
            key=str(i+1)+'-'+vocabulario[item]
            dicionario[key]=vetor[i].count(vocabulario[item])
    return dicionario

def contar_incidencia2(vetores,vocabulario):
    dicionario=dict()
    cont={}
    for i in range(len(vetores)):
           for j in range(len(vetores[i])-1):
                for k in vocabulario:
                    tests(2,'vetor:'+vetores[i][j]+' '+vetores[i][j+1])
                    tests(2,'vocabulario:'+vocabulario[k])
                    if(str(vetores[i][j]+' '+vetores[i][j+1])==str(vocabulario[k])):
                        ky=str(i+1)+'-'+vetores[i][j]+' '+vetores[i][j+1]
                        tests(2,str(i+1)+'----->'+str(vocabulario[k])+'K'+str(ky));
                        #dicionario[key]+=1
                        if ky not in dicionario: 
                            dicionario[str(ky)]=1
                            tests(2,"Chave nao existe:-")
                        else:
                            value=dicionario[str(ky)]
                            tests(2,"valor Armazenado:"+str(value))
                            if(is_int(value)):
                                value=int(value)+1
                            else:
                                value=0
                            tests(2,"valor Tratado:"+str(value))
                            
                            dicionario[str(ky)]=str(value)
                            tests(2,"valor Na Chave:"+str(dicionario[str(ky)]))
    for k in vocabulario:
        for i in range(len(vetores)):
            key=str(i+1)+'-'+vocabulario[k]
            if key not in dicionario:
                dicionario[key]=0                          
    return dicionario
def contar_incidencia3(vetores,vocabulario):
    dicionario=dict()
    for i in range(len(vocabulario)):
            itens=vocabulario[i].split(' ')
            k=vocabulario[i].replace(' ', '-')
            tests(2,'loop:'+str(i))
            for ii in range(len(vetores)):
                for j in range(len(itens)):
                    key=str(k)+'-'+str(ii+1)
                    if(i==0):
                        tests(2,"key:"+str(key))
                    #tests(0,"vocabulario:"+str(vocabulario[i]))
                    tests(2,'vetor:'+str(ii)+':'+str(vetores[ii]))
                    tests(2,"item:"+str(itens[j]));
                    #tests(0,'item'+str(j)+':'+str(itens[j]))
                    tests(2,"valor Encontrado:"+str(vetores[ii].count(itens[j])))
                    if key not in dicionario: 
                        dicionario[str(key)]=vetores[ii].count(itens[j])
                        tests(2,"valor Na Chave:0")
                    else:
                        value=dicionario.get(key)
                        tests(2,"valor Armazenado:"+str(value))
                        value=int(value)+vetores[ii].count(itens[j])
                        dicionario[str(key)]=str(value)
                        tests(2,"valor Na Chave:"+str(value))
                    #tests(0,"Incidencia:"+str(dicionario))
                    tests(2,"valor Total:"+str(dicionario[str(key)]))
    return dicionario
#conta os elementos e armazena em um dicionario 
#!utiliza como indice uma concatenação entre o indice do vetor e o item ao qual se esta procurando
def contar(vetores,vocabulario,gramatica):

    dicionario=dict()
    if(gramatica=='gram1'):
        dicionario=contar_incidencia(vetores,vocabulario)
    if(gramatica=='gram2'):
        dicionario=contar_incidencia2(vetores,vocabulario)
    if(gramatica=='gram3'):
        dicionario=contar_incidencia3(vetores,vocabulario)
    
    tests(1,'Incidencia-['+str(len(dicionario))+']:'+str(dicionario)) 
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
        if(gramatica=="gram3"):
            alterar=-1
        for item in range(len(vector[i])+alterar):
            if(gramatica=="gram1"):
                analise=vector[i][item]
            if(gramatica=="gram2"):
                analise=vector[i][item]+' '+vector[i][item+1]
            if(gramatica=="gram3"):
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
    tests(1,'Vocabulario-'+gramatica+'['+str(len(vocabulario))+']:'+str(vocabulario))
    
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

@myapp.route("/gram3")
def gramatica3():
    #entrada esperada
    e=['Falar é fácil. Mostre-me o código.','É fácil escrever código. Difícil é escrever código que funcione.']
    #StopWords adicionadas em um vetor
    stop_words='',''
    vocabulario=processar_texto(e,stop_words,'gram3')

    return render_template('lista.html')

if __name__=="__main__":
    myapp.run()