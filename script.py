class Fraction:
    def __init__(self, num, den):
        self.__num=num
        self.den=den
        
    def __str__(self):
        return str(self.__num)+'/'+str(self.den)
    
    def __add__(self, other: 'Fraction'):
        return Fraction(self.__num+other.num,self.den)
    
a=Fraction(1,2)
a.__num=4
a.den=3
print(a)