# [e gordinho?, tem perninha curta?, faz auau? ]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]

cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1] 

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [1, 0, 1]

marcacoes_teste = [-1, 1, 1]
teste = [misterioso1, misterioso2, misterioso3]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

# modelo, se adeque aos dados e marcacoes
modelo.fit(dados, marcacoes)

# modelo, preveja se...
resultado = modelo.predict(teste)
print(resultado)

diferenca = resultado - marcacoes_teste
print(diferenca)

acertos = [dif for dif in diferenca if dif == 0]
print(acertos)

total_acertos = len(acertos)
print(total_acertos)
total_elementos = len(teste)
print(total_elementos)

taxa_acerto = 100.0 * total_acertos / total_elementos
print(taxa_acerto)