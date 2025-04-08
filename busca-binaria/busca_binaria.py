def pesquisa_binaria(lista, item):
  baixo = 0
  alto = len(lista) - 1
  print(alto)
  while baixo <= alto:
    meio = int((baixo + alto) / 2)
    print('meio', meio)
    chute = lista[int(meio)]
    print('chute', chute)
  
    if chute == item:
      return meio
    if chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  
  return None

minha_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,171,8,19,20]

print(pesquisa_binaria(minha_lista, 7))
