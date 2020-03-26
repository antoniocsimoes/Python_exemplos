usuarios_data_science = [ 15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = []

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print(len(assistiram))
print(set(assistiram)) #conjunto, não tem indice, não tem ordem 

#conjuntos

usuarios_data_sciences = {15, 23, 43, 56}
usuarios_machine_learnings = {13, 23, 56, 42}

print(usuarios_data_sciences | usuarios_machine_learnings) #união
print(usuarios_data_sciences & usuarios_machine_learnings) #intersecção
print(usuarios_data_sciences - usuarios_machine_learnings) #
print(usuarios_data_sciences ^ usuarios_machine_learnings) #ou exclusivo

usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))
usuarios = frozenset(usuarios) #congela o conjunto de usuários

print(usuarios)