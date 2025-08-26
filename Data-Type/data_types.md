# Tipos de Dados em Python

Python possui diversos tipos de dados embutidos para armazenar diferentes tipos de valores. Compreender esses tipos é fundamental para escrever código eficaz e correto.

A seguir, uma breve explicação e exemplos dos tipos de dados mais comuns:

## 1. String (`str`)

Strings são sequências de caracteres, usadas para armazenar texto. Podem ser definidas usando aspas simples (`'...'`), aspas duplas (`"..."`) ou aspas triplas (`'''...'''` ou `"""..."""`) para strings de múltiplas linhas.

**Exemplo:**
```python
nome = "Alice"
mensagem = 'Olá, mundo!'
paragrafo = """Este é um parágrafo
com múltiplas linhas.
"""
print(nome)
print(mensagem)
print(paragrafo)
```

## 2. Inteiro (`int`)

Inteiros são números inteiros, positivos ou negativos, sem casas decimais. Não há limite para o tamanho de um inteiro em Python, além da memória disponível.

**Exemplo:**
```python
idade = 30
quantidade = -100
numero_grande = 12345678901234567890
print(idade)
print(quantidade)
print(numero_grande)
```

## 3. Ponto Flutuante (`float`)

Pontos flutuantes são números reais, ou seja, números com casas decimais. São usados para representar valores que podem ter frações.

**Exemplo:**
```python
altura = 1.75
preco = 19.99
pi = 3.14159
print(altura)
print(preco)
print(pi)
```

## 4. Booleano (`bool`)

Booleanos representam um dos dois valores: `True` (verdadeiro) ou `False` (falso). São amplamente utilizados em operações lógicas e estruturas de controle de fluxo.

**Exemplo:**
```python
is_ativo = True
tem_permissao = False
print(is_ativo)
print(tem_permissao)
print(10 > 5) # Saída: True
print(5 == 5) # Saída: True
print(5 != 5) # Saída: False
```

## 5. Lista (`list`)

Listas são coleções ordenadas e mutáveis de itens. Podem conter itens de diferentes tipos de dados e são definidas usando colchetes (`[]`).

**Exemplo:**
```python
frutas = ["maçã", "banana", "cereja"]
numeros = [1, 2, 3, 4, 5]
mista = ["texto", 10, True, 3.14]
print(frutas)
print(numeros[0]) # Acessa o primeiro elemento
frutas.append("laranja") # Adiciona um elemento
print(frutas)
```

## 6. Tupla (`tuple`)

Tuplas são coleções ordenadas e imutáveis de itens. Uma vez criadas, os elementos de uma tupla não podem ser alterados. São definidas usando parênteses (`()`).

**Exemplo:**
```python
coordenadas = (10.0, 20.0)
dias_semana = ("Segunda", "Terça", "Quarta")
print(coordenadas)
print(dias_semana[1]) # Acessa o segundo elemento
# coordenadas.append(30.0) # Isso geraria um erro, pois tuplas são imutáveis
```

## 7. Dicionário (`dict`)

Dicionários são coleções não ordenadas e mutáveis de pares chave-valor. Cada chave deve ser única e imutável (geralmente strings ou números), e os valores podem ser de qualquer tipo de dado. São definidos usando chaves (`{}`).

**Exemplo:**
```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
print(pessoa)
print(pessoa["nome"]) # Acessa o valor pela chave
pessoa["idade"] = 26 # Altera um valor
pessoa["profissao"] = "Engenheiro" # Adiciona um novo par chave-valor
print(pessoa)
```

## 8. Conjunto (`set`)

Conjuntos são coleções não ordenadas de itens únicos e imutáveis. São úteis para remover duplicatas de uma lista ou para realizar operações de conjunto como união, interseção e diferença. São definidos usando chaves (`{}`) ou a função `set()`.

**Exemplo:**
```python
numeros_unicos = {1, 2, 3, 4, 5, 5, 4}
letras = set(["a", "b", "c", "a"])
print(numeros_unicos)
print(letras)
letras.add("d") # Adiciona um elemento
print(letras)
```


