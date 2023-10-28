pip install nltk

import nltk
from nltk.translate import AlignedSent
from nltk.translate.ibm1 import IBMModel1
from nltk.translate.ibm2 import IBMModel2
from nltk.translate import PhraseTable

# Datos de entrenamiento
frases_fuente = ["I like to eat pizza with tomato sauce",
                "He prefers to drink tea with lemon"]
frases_objetivo = ["J'aime manger de la pizza avec de la sauce tomate",
                   "Il préfère boire du thé avec du citron"]

# Tokenización
frases_fuente = [nltk.word_tokenize(frase) for frase in frases_fuente]
frases_objetivo = [nltk.word_tokenize(frase) for frase in frases_objetivo]

# Crear oraciones alineadas
oraciones_alineadas = [AlignedSent(fuente, objetivo) for fuente, objetivo in zip(frases_fuente, frases_objetivo)]

# Entrenar el modelo IBM Model 2
modelo_ibm2 = IBMModel2(oraciones_alineadas, 5)

# Realizar traducción
frase_para_traducir = "I want to go to the beach"
tokens = nltk.word_tokenize(frase_para_traducir)

# Traducir usando el modelo IBM Model 2
traduccion = modelo_ibm2.translate(tokens)
print("Traducción:", " ".join(traduccion))
