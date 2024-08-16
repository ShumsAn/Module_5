class House:
    def __init__(self,name,number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for j in range(1,new_floor+1):
                print(j)
        else:
            print('"Такого этажа не существует"')

# Говорящий лифт xD отступ от задания
    def go_to_new(self,):
        guest = input(f'Добрый день как к вам можно обращаться ')
        new_floor = int(input(f'{guest}! добро пожаловать в {self.name} Выберите пожалуйста Этаж '))
        while new_floor < 1 or new_floor > self.number_of_floors:
            new_floor = int(input(f'{guest}! У нас {self.number_of_floors} этажей попробуйте выбрать существующй Этаж '))
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for j in range(1, new_floor + 1):
                if j < new_floor:
                    print(j)
                if j == new_floor:
                    print(f'{new_floor} этаж Вы приехали')





h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h1.go_to_new()

