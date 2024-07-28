class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors =  number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __str__(self):
        return self.name 

    def __len__(self):
        return self.number_of_floors






h1 = House('ЖК Рубин', 20)
h2 = House('Домик в деревне', 3)
h1.go_to(5)
h2.go_to(10)

print(len(h1))
print(len(h2))

print(h1)
print(h2)