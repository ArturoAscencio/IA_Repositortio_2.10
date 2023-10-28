import nltk
from nltk import bigrams, FreqDist

# Ejemplo de un corpus (puedes usar un corpus m�s grande)
corpus = "Este es un ejemplo de un corpus de texto. Es un ejemplo simple de un corpus."

# Tokenizaci�n y creaci�n de bigramas
tokens = nltk.word_tokenize(corpus.lower())
bigramas = list(bigrams(tokens))

# C�lculo de frecuencias de bigramas
frecuencia_bigramas = FreqDist(bigramas)

# Funci�n para calcular la probabilidad condicional de un bigrama
def probabilidad_condicional(bigram):
    return frecuencia_bigramas[bigram] / tokens.count(bigram[0])

# Ejemplo de c�lculo de probabilidad condicional para un bigrama
bigrama_ejemplo = ('es', 'un')
prob = probabilidad_condicional(bigrama_ejemplo)
print(f'Probabilidad de "{bigrama_ejemplo[1]}" despu�s de "{bigrama_ejemplo[0]}": {prob:.4f}')
