class CSVreader():
    def __init__(self,dane=[]):
        #self.plik=plik
        #self.separator=separator
       self.dane=dane
       
    def __len__(self):
        return len(self.dane)
    
    def __getitem__(self, idx):
        try:
            return self.dane[idx]
        except IndexError:
            return "Na tym miejscu nic nie ma"
        
    def __setitem__(self, idx, val):
        if len(self.dane[0])!= len(val):
            return "Wiersz składa sie ze złej ilosci elementow"
        elif len(self.dane[0])== len(val):
            self.dane[idx]=val
    def wczytaj(self,plik, separator=','):
        with open(plik, 'rt') as f:
            linie = f.readlines() 
            dane = [] # lista do wpisywania odczytanych danych
            for linia in linie:
                if linia[0] == '#': #komentarz - do pominiecia
                    continue 
                wiersz = linia.strip().split(sep=separator) #strip() - pozbycie sie znaku konca linii (i innych bialych znakow)
                dane.append(wiersz)
                if len(dane[0]) != len(wiersz):
                    raise ValueError('niepoprawny format danych - rozna liczba wartosci w wierszach')
        self.dane=dane
        
    def zapisz(self,nazwa,separator=','):
        with open(nazwa, 'wt') as f:
            for wiersz in self.dane:
                if len(wiersz) > 0:
                    f.write(wiersz[0]) 
                    for d in wiersz[1:]:
                        f.write(separator+d)
                    f.write('\n')
    
   
if __name__=="__main__":
    p=CSVreader()
    p.wczytaj('prosty.csv')
    #print(p.wczytaj('prosty.csv'))   
    print(p.dane)
    p.zapisz('test','x')
    print(len(p))
    print(p[6])
    p[1]=['adam','musial']
    p.zapisz('test2')    