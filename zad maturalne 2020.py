with open('pary.txt', 'r') as f: lines = [x.rstrip().split(' ')[0] for x in f]
def pierwsza(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        else:
            return True
for liczba in lines:
    if int(liczba)%2 == 0:
        for i in range(2 ,int(liczba)):
            if pierwsza(i) and pierwsza(int(liczba)-i):
                print(liczba, i, int(liczba)-i)
                break
