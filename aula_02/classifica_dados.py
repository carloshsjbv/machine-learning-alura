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

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(X,Y)

resultado = modelo.predict(X)
resultado = modelo.predict(Y)