# -*- coding: utf-8 -*-

###############################################################
########################## AULA 02 ############################
###############################################################

##########################################################################################
#  Classificação em PYTHON:                                                              #
#     - Um array para os dados (home, como_funciona, contato)    #                             
#     - Um array para as marcações (comprou)                                             #
#                                                                                        #
#  X = Dados que eu tenho                                                                #
#  Y = Dados que eu quero prever                                                         #
#                                                                                        #
##########################################################################################

from dados import carregar_acessos

X, Y = carregar_acessos()

# Separar as 90 primeiras linhas do array para treino
treino_dados = X[:90]
treino_marcacoes = Y[:90]

# Separar as 9 últimas para teste
teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)
