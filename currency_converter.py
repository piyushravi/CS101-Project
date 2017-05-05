from yahoo_finance import Currency

file= open("Currency_update.txt", 'r')
x=file.readlines()



for y in x:
    L=map(str, y.split())
    res=''
    for z in L[:-1]:
        res+=z+' '
    print '%30s %s'%(res,L[-1])
    
first_currency=raw_input("enter first currency: ")
second_currency=raw_input("enter second currency: ")
conversion=first_currency+second_currency
eur_pln = Currency(conversion)
print eur_pln.get_bid()

