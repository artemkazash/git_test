class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
def oldest_cat(*args):
    return sorted([cat for cat in args], key= lambda x: x.age)[-1]
def oldest_cats(*args):
    return [cat for cat in args if cat.age==max([i.age for i in args])]
cat1=Cat('Nissi', 15)
cat2=Cat('Fissi', 15)
cat3=Cat('Gissi', 6)

print(oldest_cats(cat1, cat2, cat3))
