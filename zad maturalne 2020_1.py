# with open('pary.txt', 'r') as f: lines = [x.rstrip().split(' ')[1] for x in f]
# x = [(max(slowo, key=lambda x: slowo.count(x)), slowo.count(max(slowo, key=lambda x: slowo.count(x)))) for slowo in lines]
# print(max(x, key=lambda x: x[1]))

with open('pary.txt', 'r') as f: lines = [x.rstrip().split(' ')[1] for x in f]
psort =[]
for slowo in lines:
    lista = []
    wynik = []
    for i in range(len(slowo)-1):
        if slowo[i+1] == slowo[i]:
            lista.append(slowo[i])
        else:
            lista.append(slowo[i])
            wynik.append((len(lista), lista[0]))
            lista.clear()
    psort.append(sorted(wynik, key=lambda x: x[0], reverse=True)[0])
for x,z in psort:
    print(''.join(z*x), x)