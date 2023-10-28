import nltk
from nltk import bigrams, FreqDist

# Ejemplo de un corpus (puedes usar un corpus más grande)
corpus = "Este es un ejemplo de un corpus de texto. Es un ejemplo simple de un corpus."

# Tokenización y creación de bigramas
tokens = nltk.word_tokenize(corpus.lower())
bigramas = list(bigrams(tokens))

# Cálculo de frecuencias de bigramas
frecuencia_bigramas = FreqDist(bigramas)

# Función para calcular la probabilidad condicional de un bigrama
def probabilidad_condicional(bigram):
    return frecuencia_bigramas[bigram] / tokens.count(bigram[0])

# Ejemplo de cálculo de probabilidad condicional para un bigrama
bigrama_ejemplo = ('es', 'un')
prob = probabilidad_condicional(bigrama_ejemplo)
print(f'Probabilidad de "{bigrama_ejemplo[1]}" después de "{bigrama_ejemplo[0]}": {prob:.4f}')
