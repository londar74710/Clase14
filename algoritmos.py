def ordenarBurbuja(lista):

    ultimaposicion = len(lista) - 1

    for pos1 in range(ultimaposicion, 0, -1):
        for pos2 in range(pos1):
            if lista[pos2] > lista[pos2+1]:
                lista[pos2], lista[pos2+1] = lista[pos2+1], lista[pos2]
    return lista

def busquedaSecuencial(lista, numero):
    pos = 0
    existe = False
    while pos < len(lista) and not existe:
        if lista[pos] == numero:
            existe = True
        else:
            pos += 1
    return existe

def busquedaBinaria(lista, numero):
    indice1 = 0
    indiceUltimo = len(lista) - 1
    existe = False

    while indice1 <= indiceUltimo and not existe:
        mitad = (indice1 + indiceUltimo) // 2
        if lista[mitad] == numero:
            existe = True
        else:
            if numero < lista[mitad]:
                indiceUltimo = mitad - 1
            else:
                indice1 = mitad + 1
    return existe

if __name__ == '__main__':
    lista = [27, 24, 26, 23, 25, 22, 21]
    #l = ordenarBurbuja(lista)
    #print(l)

    numero = 25

    print(lista)
    print('BUSQUEDA SECUENCIAL: ¿existe el numero ' + str(numero) + '?: ' + str(busquedaSecuencial(lista, numero)))

    print()

    ordenarBurbuja(lista)

    print(lista)
    print('BUSQUEDA BINARIA: ¿existe el numero ' + str(numero) + '?: ' + str(busquedaBinaria(lista, numero)))



