# 2․ Գրել ծրագիր, որը․
#    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները,
#      իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
#    օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
#    պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:



# def f(d1):
#     d2 = {}
#     for i in d1.values():
#         d2[i] = len(i)
#     return d2
#
#
#
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print(f(dict_1))

# ================================================================

# 3. Գրել ֆունկցիա, որը․
#    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
#    - կվերադարձնի ստացված dictionary-ն,
#    օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
#    պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:


# def f(d1):
#     d2 = {}
#     for i in d1.keys():
#         d2[i] = [j for j in d1[i] if j%2 == 1]
#     return d2
#
#
#
# dict1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
#
# print(f(dict1))

# ===========================================================================


class Car:
    mileage = 0
    def __init__(self, company = None, mark = None, year = None):
        self.company = company
        self.mark = mark
        self.year = year

    def description(self):
        print(f"{self.company} {self.mark} is made in {self.year} and has {self.mileage} mileage")




