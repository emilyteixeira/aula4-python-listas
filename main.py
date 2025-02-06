# AULA 4 - ESTRUTURAS DE DADOS

# Listas & Tuplas

# Listas

# Lista de nomes
nome = ["Vini", "Marina", "Kleber", "João"]
# Índices:   0        1         2       3

# Lista de notas correspondentes aos nomes
notas = [9.3, 8.8, 3.1, 6.0]

# Exibe as listas completas
print(nome)
print(notas)

# Exibe o primeiro nome e sua nota correspondente
print(nome[0], notas[0])

# Adiciona um novo nome à lista
nome = ["Vini", "Marina", "Kleber", "João", "Joy"]

# Exibe o tipo da variável 'nome' (deve ser uma lista)
print(type(nome))

# Exibe o número de elementos da lista 'nome'
print(len(nome))

# Métodos de listas

# 1. insert(index, item) - Insere um item em uma posição específica

frutas = ['maçā', 'banana' , 'uva' , 'laranja' , 'banana']

frutas.insert(2, 'abacaxi')
print("fruta inserida:", frutas)

# 2. append(item) - Adiciona um item ao final da lista

frutas.append('manga')
print("Após o append:", frutas)

# 3. sort() - Ordena a lista

frutas.sort()
print("Após o sort:", frutas)

# 4. sorted() - Retorna uma cópia ordenada da lista

frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']
frutas_ordenadas = sorted(frutas)
print("Lista original:", frutas)

# 5. remove(item) - Remove o primeiro item da lista cujo valor é igual a item

frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']
frutas.remove('banana')
print("Após o remove:", frutas)

# 6. pop([index]) - Remove o item na posição dada e o retorna. Se nenhum índice for especificado, remove e retorna o último item da lista

frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']
frutas.pop(3)
print("Após o pop:", frutas)

# Tuplas

# São imutáveis
# Guardam valores de tipos diferentes

exemplo_tupla = ("Vini", '1234', 20)
print(exemplo_tupla)

# Retorna o tipo de dado:
print(type(exemplo_tupla))

item = 10, 20, 3, 6
print(item[0:3])

# Comparando valores dentro de uma tupla
print('Vini' in exemplo_tupla) # Retorna True

# Concatenando tuplas
pratos1 = ('lasanha', 'pizza', 'hamburguer')
pratos2 = ('sushi', 'sashimi', 'temaki')
pratos = pratos1 + pratos2
print(pratos)

# Tuplas aninhadas
tupla_aninhada = (1, 2, 3, (4, 5, 6))
print(tupla_aninhada)

# -----------------------------------------------------------

# Vetores

# Vetores são listas de valores numéricos
# São mais eficientes que listas
# São mais rápidos que listas
# Não possuem métodos de listas