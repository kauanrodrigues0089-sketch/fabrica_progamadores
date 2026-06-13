#Autor:Kauan Pietro
#projeto:listas

#listas
penta = ['Brasil','paraguay','chile']
tetra = ['Brasil','Italia','Alemanha']
tri = ['Brasil','Argentina','Italia','Alemanha']

#imprimindo os nomes
print('---campeos do mundo---')

#excluindo por posicao
#exmplo excluir o chile
print(penta)
del penta[2]
print(penta)

# excluindo por nome
print(penta)
penta.remove('paraguay')
print(penta)