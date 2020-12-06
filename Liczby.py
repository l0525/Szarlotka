'''
liczby_plik = open("liczby.txt", "r")
lista = []
for liczby in liczby_plik.readlines():
    lista.append(liczby)
liczby_plik.close()
print(lista)
'''
lista = []
def odczyt():
    with open("liczby.txt", "r") as f:
        for line in f:
            lista.append(int(line))
def zadanie_pierwsze():
    odczyt()
    licznik = 0
    for i in range(len(lista)):
        l = str(lista[i])
        zera = 0
        jedynki = 0
        for o in range(len(l)):
            if l[o] == '0':
                zera += 1
            else:
                jedynki += 1
        if zera > jedynki:
            licznik += 1
    print(licznik)
def zadanie_drugie():
    semki = 0
    wojki = 0
    odczyt()
    for i in range(len(lista)):
        tmp = int(str(lista[i]),2)
        lista[i] = tmp
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            wojki += 1
        if lista[i]%8 == 0:
            semki += 1
    print("Ilość dwójek: " + str(wojki))
    print("Ilość ósemek: " + str(semki))
def zadanie_trzecie():
    odczyt()
    maks = 0
    minn = 0
    for i in range(len(lista)):
        tmp = int(str(lista[i]),2)
        lista[i] = tmp
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            if lista[i] > lista[maks]:
                maks = i
        if lista[i] < lista[i-1]:
            if lista[i] < lista[minn]:
                minn = i
    print("Najmniejsza w wierszu: " + str(minn + 1))
    print("Najwieksza w wierszu: " + str(maks + 1))
