# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
#    - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
#    - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա
#      (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։
import math

class Triangle:
    def __init__(self, a,b,c):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError("Not a triangle")
        self.a = a
        self.b = b
        self.c = c

    def koxmer(self):
        return self.a,self.b,self.c

    def p(self):
        return self.a + self.b + self.c

    def s(self):
        return ((self.a + self.b + self.c)*(self.a + self.b)*(self.a + self.c)*(self.b + self.c))**0.5

    def ankanon(self):
        if self.a == self.b == self.c:
            return "havasarakoxm"
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 'havasarasrun'
        return "ankanon"
    def uxxankyun(self):
        return bool(self.a**2 + self.b**2 == self.c**2) or bool(self.a**2 + self.c**2 == self.b**2) or bool(self.c**2 + self.b**2 == self.a**2)

    def ankyunner(self):
        self.cosA = (self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c)
        self.cosB = (self.a**2 + self.c**2 - self.b**2)/(2*self.a*self.c)
        self.cosC = (self.a**2 + self.b**2 - self.c**2)/(2*self.a*self.b)
        self.A = round(math.degrees(math.acos(self.cosA)),3)
        self.B = round(math.degrees(math.acos(self.cosB)),3)
        self.C = round(math.degrees(math.acos(self.cosC)),3)
        return self.A,self.B,self.C



t = Triangle(4,3,4)
print(f'p = {t.p()} \n s = {t.s()} \n {t.ankanon()} \n ankyunnery = {t.ankyunner()}')

