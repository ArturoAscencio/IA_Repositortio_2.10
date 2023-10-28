pip install nltk

import nltk
from nltk.corpus import treebank

# Descargar el corpus Penn Treebank si no lo tienes
nltk.download("treebank")

# Crear una lista de oraciones etiquetadas con POS
sentences = treebank.parsed_sents()

# Crear una PCFG a partir de las oraciones etiquetadas
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [0.9] | VP [0.1]
    NP -> Det N [0.7] | N [0.3]
    VP -> V NP [0.4] | V [0.6]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'dog' [0.6] | 'cat' [0.4]
    V -> 'chased' [0.8] | 'ate' [0.2]
""")

# Crear un analizador sintáctico basado en la PCFG
parser = nltk.ViterbiParser(pcfg_grammar)

# Oración para analizar
sentence = "the dog chased the cat".split()

# Realizar análisis sintáctico de la oración
for tree in parser.parse(sentence):
    tree.pretty_print()
