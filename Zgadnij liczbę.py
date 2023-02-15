from random import randint

los=randint(1,10)
odp=-1
i=0
print('Zgadnij liczbę z przedziału od 1 do 10:')

while odp != los:
    i+=1
    odp= int(input('Podaj liczbę: '))
    if odp>los:
        print('Niestety, wylosowana liczba jest mniejsza od Twojej.')
    elif odp<los:
        print('Niestety, wylosowana liczba jest większa od Twojej.')
print('Brawo! Odgadłeś/aś za ', i, 'razem.')

