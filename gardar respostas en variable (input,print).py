
cursor = '> '

print('cal é o teu nome?')
nome = input(cursor)

print("Vou preguntarte varias cousas")
print("Gustas deste programa, {}?".format(nome))
gusto = input(cursor)

print("Onde vives, {}?".format(nome))
vila = input(cursor)

print("Que tipo de SO estás a usar?")
SO = input(cursor)

print("""
Entón, dixeches {} acerca do programa.
Vives en {}.
E usas {}. Mola.
""".format(gusto,vila,SO))
