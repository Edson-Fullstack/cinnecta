"""
PEP 8 -- Style Guide for Python Resume
pip8 app
"""
from flask import Flask, render_template, url_for, request
# database nosql
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
from datetime import datetime
import string
import random

# esta varialvel e funcão controlam o debug passo a passo no ambiente de testes
# 0=clean compile
# 1=otput de processamentos
# 2=processamento interno
TEST_CONTROL = 0
def tests(controle, mensagem):
    """mensagem a ser exibida no durante testes"""
    if(TEST_CONTROL >= controle):
        print(str(mensagem))

# !supportes
# conecta a um banco de dados
def conectar_bd():
    if(TEST_CONTROL == 0):
        # string de connecção com banco de dados nosql(atlas mongodb)
        client = MongoClient('mongodb+srv://master:668262az@world' +
                             '0-o28vw.gcp.mongodb.net/cinnecta?retry' +
                             'Writes=true&w=majority')
        db = client.cinnecta
        collection = db['words']
        return collection

# inseri os valores de resposta no banco de dados
def inserir_bd(conteudo):
    
    if(TEST_CONTROL == 0):
        key = ''.join(random.sample(string.ascii_lowercase, 12))
        item = {}
        # usando um gerador automatico de keys. Porem o ideal seria utilizar
        # as entradas para formar testes unicos
        # tentar implementar usando time
        # key=datetime.utcnow()
        item['_id'] = ObjectId(b'' + bytes(key, encoding='utf8'))
        item['content'] = str(conteudo)
        collection.insert_one(item)
#mostra os itens adicionados na base de dados ate o momento
def show_db():
    retorno='Nenhum Banco de Dados funcional.'
    if(TEST_CONTROL == 0):
        items=collection.find()
        retorno=str()
        for item in items:
            retorno=retorno+str(item)
    return retorno


collection=conectar_bd()



# verifica se um valor é inteiro
def is_int(valor):
    """valor a ser verificado """
    try:
        int(valor)
        return True
    except ValueError:
        return False
# remove caracteres e retorna toda a string em lower case


def remover_caracteres(old_string, to_remove):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, ' ')
    return new_string.lower()

# tratamento subistituir string priciplamente para '-' de palavras compostas


def substituir_caracteres(old_string, to_remove, to_replace):
    new_string = old_string
    for i in to_remove:
        new_string = new_string.replace(i, to_replace)
    return new_string.lower()

# retorna dicionario contendo os vetores com quantas palavras se repetem
# na analise gramatical 1

# !PRINCIPAIS
def contar_incidencia(vetor, vocabulario):
    """entradas de vetores distitos de palavras e vocabulario formado """
    dicionario = dict()
    for i in range(len(vetor)):
        for item in vocabulario:
            key = str(i + 1) + '-' + vocabulario[item]
            # retorna o valor contado de cada item do vocabulario
            # para cada item do vetor
            dicionario[key] = vetor[i].count(vocabulario[item])
    return dicionario


# retorna dicionario contendo os vetores com quantas palavras
# se repetem na analise gramatical 2
def contar_incidencia2(vetores, vocabulario):
    """entradas de vetores distitos de palavras e vocabulario formado """
    dicionario = dict()
    # para todos os vetores
    for i in range(len(vetores)):
            # não executa ate o ultimo elemento pra evitar misshit em
            # itens que nao existem
        for j in range(len(vetores[i]) - 1):
            for k in vocabulario:
                tests(2, 'vetor:' + vetores[i][j] + ' ' + vetores[i][j + 1])
                tests(2, 'vocabulario:' + vocabulario[k])
                # checa se os elementos sequentes estao no vocabulario
                if(str(vetores[i][j] + ' ' + vetores[i][j+1]) ==
                   str(vocabulario[k])):
                    # gera chave de armazenagem
                    ky = str(i + 1) + '-' + \
                        vetores[i][j] + ' ' + vetores[i][j + 1]
                    tests(2, str(i + 1) + '----->' +
                          str(vocabulario[k]) + 'K' + str(ky))
                    if ky not in dicionario:
                        dicionario[str(ky)] = 1
                        tests(2, "Chave nao existe:-")
                    else:
                        # incrementa o valor caso o item exista
                        value = dicionario[str(ky)]
                        tests(2, "valor Armazenado:" + str(value))
                        if(is_int(value)):
                            value = int(value) + 1
                        else:
                            value = 0
                        tests(2, "valor Tratado:"+str(value))
                        dicionario[str(ky)] = str(value)
                        tests(2, "valor Na Chave:" + str(dicionario[str(ky)]))
    # 0 fill para preencher os itens que não ocoreram na busca acima
    for k in vocabulario:
        for i in range(len(vetores)):
            key = str(i + 1) + '-' + vocabulario[k]
            if key not in dicionario:
                dicionario[key] = 0
    return dicionario


# conta os elementos e armazena em um dicionario
# !utiliza como indice uma concatenação entre o indice do vetor e o
# item ao qual se esta procurando


def contar(vetores, vocabulario, gramatica):
    """divide a execução dependendo do tipo de gramatica """
    dicionario = dict()
    if(gramatica == 'gram1'):
        dicionario = contar_incidencia(vetores, vocabulario)
    if(gramatica == 'gram2'):
        dicionario = contar_incidencia2(vetores, vocabulario)
    if(gramatica == 'gram3'):
        dicionario = contar_incidencia3(vetores, vocabulario)

    tests(1, 'Incidencia-[' + str(len(dicionario)) + ']:' + str(dicionario))
    return dicionario

# conta os elementos e armazena em um dicionario
# !utiliza como indice uma concatenação entre o indice do vetor e o
# item ao qual se esta procurando
# a partir do vetor contendo os textos retorna o vocabulario e os vetores
# contendo as palavras da frase


def gerar_listas_simples(textos, stop_words, gramatica):
    apagar_caracteres = ',.!?-_%&#[(<>)]'
    vector = {}
    tests(1, 'textos:'+str(textos))
    vocabulario_set = set()
    vocabulario = dict()
    j = 0
    for i in range(len(textos)):
        # remove caracteres e tratamento de texto
        vector[i] = remover_caracteres(textos[i], apagar_caracteres).split(' ')
        # j representa o indice para a lista de vocabulario
        # retirar elementos vazios do vetor
        while('' in vector[i]):
            vector[i].remove('')
        # dado tipo de gramatica alterar ate onde do vetor se ira percorer
        # para evitar misscheck em possições fora do vetor
        if(gramatica == "gram1"):
            alterar = 0
        if(gramatica == "gram2"):
            alterar = -1
        # dado o tipo de gramatica altera a forma de pegar as posições
        # da lista de vocabulario
        for item in range(len(vector[i]) + alterar):
            if(gramatica == "gram1"):
                analise = vector[i][item]
            if(gramatica == "gram2"):
                analise = vector[i][item] + ' ' + vector[i][item + 1]
            tests(2, 'Analise:' + analise)
            # tratamento para eliminar stopwords e adicionar os elementos
            # que nao se repetem
            if (analise in stop_words):
                tests(2, 'Remove(stopword):'+analise)
                continue
            # tratamento para nao permitir itens dobrados no vocabulario e
            # manter a ordem
            #
            # caso usar apenas o Set os itens mudam de ordem e ao aplicar
            # .short a ordem fica crescente e a ordem apresentada foi ordem de
            # aparição
            elif (analise not in vocabulario_set):
                tests(2, 'Add:' + analise)
                vocabulario_set.add(analise)
                vocabulario[j] = analise
                j = j + 1
            else:
                tests(2, 'Remove:' + vector[i][item])
    tests(1, 'Vocabulario-' + gramatica + '[' + str(len(vocabulario)) +
          ']:' + str(vocabulario))

    return vocabulario, vector

#formata a saida para o formato desejado retornando o vocabulario
#e os vetores concatenados
def formatar_saida(vocabulario,vector,dicionario,gramatica):
    vet=''
    voc=''
    for i in range(len(vector)):
        voc='Vocabulario '+':['
        vet=vet+'texto '+str(i+1)+':['
        for k in vocabulario:
            voc=voc+str(k+1)+'.'+str(vocabulario[k])+ ' '
            key = str(i + 1) + '-' + vocabulario[k]
            vet=vet+str(dicionario[key])
            if(k<len(vocabulario)-1):
                vet=vet+','
            else:
                vet=vet+']'
    if(gramatica == "gram2"):
        voc=voc+']'
    return voc,vet

# função principal para execução da primeira parte do exercicio
def processar_texto(textos, stop_words, gramatica):
    vocabulario, vector = gerar_listas_simples(textos, stop_words, gramatica)
    tests(1,'vocabulario:'+str(vocabulario))
    # gerar teste com resultados da parte 1
    dicionario = contar(vector, vocabulario, gramatica)
    tests(1,'vetores:'+str(vector))
    final={}
    final['vocabulario'],final['vetor']=formatar_saida(vocabulario,vector,dicionario,gramatica)
    tests(1,'Final:'+str(final))

    inserir_bd(final)
    return final

myapp = Flask(__name__)


# home page
@myapp.route("/")
def home():
    return render_template('index.html')

# home page
@myapp.route("/prova")
def prova():
    return render_template('prova.html')

# manual de uso
@myapp.route("/manual")
def manual():
    return render_template('manual.html')

@myapp.route("/db")
def db():
    texto=dict()
    texto['db']=show_db()
    return render_template('database.html',texto=texto)


# execução de gramatica 1
# entrada como uma string onde as frases sao divididas por ,
# utilizar outro dvisor para nao quebra sentidos de frases diferentes(|)
@myapp.route("/gram1", defaults={"enter": 'Falar é fácil. Mostre-me o ' +
                                            'código.|É fácil escrever código' +
                                            '. Difícil é escrever código que' +
                                            ' funcione.'})
@myapp.route("/gram1<enter>")
def gramatica1(enter, methods=['GET', 'POST']):
    # entrada esperada
    # testes efeturado para evitar erro e=[''] e='' e=['',''] todos passam
    # e=False gera erro entao qualque entrada de dados que nao for puder ser
    # mensurada provavelmente ira gerar erro
    if request.method == 'GET':
        e=request.args['enter']
    if len(e)==0:
        e ='Falar é fácil. Mostre-me o código.|É fácil escrever código. Difícil é escrever código que funcione.'
    e = e.split('|')
    # StopWords adicionadas em um vetor
    stop_words = '', ''
    textos = processar_texto(e, stop_words, 'gram1')
    return render_template('lista.html',resultado=textos)


# execução de gramatica 2
@myapp.route("/gram2", defaults={'entrada': 'Falar é fácil. Mostre-me o ' +
                                 'código.|É fácil escrever código. Difícil é' +
                                 ' escrever código que funcione.'})
@myapp.route("/gram2<entrada>")
def gramatica2(entrada):
   # entrada esperada
    # testes efeturado para evitar erro e=[''] e='' e=['',''] todos passam
    # e=False gera erro entao qualque entrada de dados que nao for puder ser
    # mensurada provavelmente ira gerar erro
    if request.method == 'GET':
        e=request.args['enter']
    if len(e)==0:
        e ='Falar é fácil. Mostre-me o código.|É fácil escrever código. Difícil é escrever código que funcione.'
    e = e.split('|')
    # StopWords adicionadas em um vetor
    stop_words = '', ''
    textos = processar_texto(e, stop_words, 'gram2')
    return render_template('lista.html',resultado=textos)


if __name__ == "__main__":
    # rodar app no local host(host='0.0.0.0', port=80,debug=True)
    # ter apenas 1 servidor respodendo na porta 80
    myapp.run(debug=True)