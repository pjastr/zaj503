class Building(object):

    def __init__(self, floors):
        self.__floors = [None] * floors

    def __setitem__(self, floor_number, data):
        self.__floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self.__floors[floor_number]


building1 = Building(4)  # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print(building1[2])
