# Conversão de Dados em Python

Em Python, é comum a necessidade de converter dados de um tipo para outro. Isso é conhecido como *type casting* ou *conversão de tipo*. Python oferece funções embutidas para facilitar essas conversões.

A seguir, uma breve explicação e exemplos das funções de conversão mais comuns:

## 1. Convertendo para Inteiro (`int()`)

A função `int()` converte um valor para um tipo inteiro. Pode ser usada para converter números de ponto flutuante (truncando a parte decimal) ou strings que representam números inteiros.

**Exemplo:**
```python
# De float para int
numero_float = 10.75
inteiro_convertido = int(numero_float)
print(f"Float {numero_float} convertido para int: {inteiro_convertido}") # Saída: 10

# De string para int
string_numero = "123"
inteiro_da_string = int(string_numero)
print(f"String '{string_numero}' convertida para int: {inteiro_da_string}") # Saída: 123

# Erro ao converter string não numérica
# string_invalida = "abc"
# int(string_invalida) # Isso geraria um ValueError
```

## 2. Convertendo para Ponto Flutuante (`float()`)

A função `float()` converte um valor para um tipo de ponto flutuante. Pode ser usada para converter inteiros ou strings que representam números (inteiros ou decimais).

**Exemplo:**
```python
# De int para float
numero_inteiro = 25
float_convertido = float(numero_inteiro)
print(f"Inteiro {numero_inteiro} convertido para float: {float_convertido}") # Saída: 25.0

# De string para float
string_decimal = "3.14"
float_da_string = float(string_decimal)
print(f"String '{string_decimal}' convertida para float: {float_da_string}") # Saída: 3.14

# string_invalida = "hello"
# float(string_invalida) # Isso geraria um ValueError
```

## 3. Convertendo para String (`str()`)

A função `str()` converte qualquer tipo de dado para sua representação em string. É útil para exibir dados ou concatená-los com outras strings.

**Exemplo:**
```python
# De int para string
idade = 30
idade_str = str(idade)
print(f"Inteiro {idade} convertido para string: '{idade_str}' (Tipo: {type(idade_str)}) ") # Saída: '30'

# De float para string
preco = 49.99
preco_str = str(preco)
print(f"Float {preco} convertido para string: '{preco_str}' (Tipo: {type(preco_str)}) ") # Saída: '49.99'

# De booleano para string
is_verdadeiro = True
boolean_str = str(is_verdadeiro)
print(f"Booleano {is_verdadeiro} convertido para string: '{boolean_str}' (Tipo: {type(boolean_str)}) ") # Saída: 'True'
```

## 4. Convertendo para Booleano (`bool()`)

A função `bool()` converte um valor para um tipo booleano (`True` ou `False`). Em Python, a maioria dos valores é considerada `True` (truthy), exceto alguns valores que são considerados `False` (falsy), como:
- `0` (inteiro zero)
- `0.0` (float zero)
- `False`
- `None`
- Strings vazias (`""`)
- Listas vazias (`[]`)
- Tuplas vazias (`()`)
- Dicionários vazios (`{}`)
- Conjuntos vazios (`set()`)

**Exemplo:**
```python
print(f"bool(1): {bool(1)}") # Saída: True
print(f"bool(0): {bool(0)}") # Saída: False
print(f"bool('hello'): {bool('hello')}") # Saída: True
print(f"bool(''): {bool('')}") # Saída: False
print(f"bool([1, 2]): {bool([1, 2])}") # Saída: True
print(f"bool([]): {bool([])}") # Saída: False
print(f"bool(None): {bool(None)}") # Saída: False
```

## 5. Convertendo para Lista (`list()`)

A função `list()` converte uma sequência (como uma string, tupla ou conjunto) em uma lista.

**Exemplo:**
```python
# De string para lista de caracteres
texto = "Python"
lista_caracteres = list(texto)
print(f"String '{texto}' convertida para lista: {lista_caracteres}") # Saída: ['P', 'y', 't', 'h', 'o', 'n']

# De tupla para lista
minha_tupla = (1, 2, 3)
lista_da_tupla = list(minha_tupla)
print(f"Tupla {minha_tupla} convertida para lista: {lista_da_tupla}") # Saída: [1, 2, 3]

# De conjunto para lista
meu_conjunto = {5, 4, 3}
lista_do_conjunto = list(meu_conjunto)
print(f"Conjunto {meu_conjunto} convertido para lista: {lista_do_conjunto}") # Saída: [3, 4, 5] (ordem pode variar)
```

## 6. Convertendo para Tupla (`tuple()`)

A função `tuple()` converte uma sequência (como uma string, lista ou conjunto) em uma tupla.

**Exemplo:**
```python
# De string para tupla de caracteres
texto = "Data"
tupla_caracteres = tuple(texto)
print(f"String '{texto}' convertida para tupla: {tupla_caracteres}") # Saída: ('D', 'a', 't', 'a')

# De lista para tupla
minha_lista = [10, 20, 30]
tupla_da_lista = tuple(minha_lista)
print(f"Lista {minha_lista} convertida para tupla: {tupla_da_lista}") # Saída: (10, 20, 30)

# De conjunto para tupla
meu_conjunto = {"a", "b", "c"}
tupla_do_conjunto = tuple(meu_conjunto)
print(f"Conjunto {meu_conjunto} convertido para tupla: {tupla_do_conjunto}") # Saída: ('a', 'b', 'c') (ordem pode variar)
```

## 7. Convertendo para Dicionário (`dict()`)

A função `dict()` pode ser usada para criar um dicionário a partir de uma sequência de pares chave-valor (como uma lista de tuplas ou uma lista de listas).

**Exemplo:**
```python
# De lista de tuplas para dicionário
lista_de_pares = [("nome", "Ana"), ("idade", 28)]
dicionario_da_lista = dict(lista_de_pares)
print(f"Lista de pares {lista_de_pares} convertida para dicionário: {dicionario_da_lista}") # Saída: {'nome': 'Ana', 'idade': 28}

# De listas aninhadas para dicionário
lista_aninhada = [["chave1", 1], ["chave2", 2]]
dicionario_aninhado = dict(lista_aninhada)
print(f"Lista aninhada {lista_aninhada} convertida para dicionário: {dicionario_aninhado}") # Saída: {'chave1': 1, 'chave2': 2}
```

## 8. Convertendo para Conjunto (`set()`)

A função `set()` converte uma sequência (como uma string, lista ou tupla) em um conjunto. Duplicatas são automaticamente removidas.

**Exemplo:**
```python
# De string para conjunto de caracteres únicos
texto_duplicado = "banana"
conjunto_caracteres = set(texto_duplicado)
print(f"String '{texto_duplicado}' convertida para conjunto: {conjunto_caracteres}") # Saída: {'b', 'a', 'n'}

# De lista para conjunto (removendo duplicatas)
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto_da_lista = set(lista_com_duplicatas)
print(f"Lista {lista_com_duplicatas} convertida para conjunto: {conjunto_da_lista}") # Saída: {1, 2, 3, 4, 5}

# De tupla para conjunto
minha_tupla = (10, 20, 20, 30)
conjunto_da_tupla = set(minha_tupla)
print(f"Tupla {minha_tupla} convertida para conjunto: {conjunto_da_tupla}") # Saída: {10, 20, 30}
```

Compreender e aplicar a conversão de dados é essencial para manipular e processar informações de forma flexível em Python.

