class Duona():
    def __init__(self, title = "", weight = 0, price = 0, square = 0):
        self.Title = title
        self.Weight = weight
        self.Price = price
        self.Square = square
    def __str__(self):
        return f' Duona: {self.Title}, svoris: {self.Weight} g., kaina {self.Price} eur, plotas {self.Square} kv.cm.'

    def shelfSquare (self, quantity):
        return self.Square * quantity / 10000

    def totalWeight(self, quantity):
        return self.Weight * quantity / 1000

