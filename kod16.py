class Model:

    def __init__(self, dane, wynik, nazwa):
        self.dane = dane
        self.wynik = wynik
        self.nazwa = nazwa

    def __repr__(self):
        return f"{self.nazwa}: {self.dane}, {self.wynik}."

    def __add__(self, other):
        if isinstance(other, Model):
            nowe_dane = self.dane + other.dane
            nowy_wynik = self.wynik + other.wynik
            nowa_nazwa = self.nazwa + other.nazwa
            return Model(nowe_dane, nowy_wynik, nowa_nazwa)
        if isinstance(other, int):
            nowe_dane = [i+other for i in self.dane]
            return Model(nowe_dane, self.wynik, self.nazwa)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            nowy_wynik = self.wynik+other
            return Model(self.dane, nowy_wynik, self.nazwa)
        return NotImplemented


m1 = Model([3, 9, 2, 0], 3.4, "model1")
print(m1)
m2 = Model([-4,-9], 1000, "model2")
print(m2)
m3 = m1 + m2
print(m3)
print(m1)
print(m2)
m4 = m1 + 4
print(m4)
m5 = 8 + m1
print(m5)