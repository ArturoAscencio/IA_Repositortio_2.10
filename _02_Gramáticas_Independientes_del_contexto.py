pip install nltk

import nltk

# Definir un PCFG
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | N [0.3]
    VP -> V [0.5] | V NP [0.3] | V S [0.2]
    Det -> 'the' [1.0]
    N -> 'cat' [0.4] | 'dog' [0.6]
    V -> 'chased' [0.7] | 'ate' [0.3]
""")

# Crear un analizador sintáctico basado en el PCFG
parser = nltk.ViterbiParser(pcfg_grammar)

# Oración para analizar
sentence = "the cat chased the dog".split()

# Realizar análisis sintáctico de la oración
for tree in parser.parse(sentence):
    tree.pretty_print()
