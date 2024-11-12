
class Kepykla():
    def __init__(self, bakery_name = "", quantity_kvietinė = 0, quantity_rūginė = 0, quantity_pilno_grūdo = 0, car_space = 0):
        self.Bakery_name = bakery_name
        self.Quantity_kvietinė = quantity_kvietinė
        self.Quantity_rūginė = quantity_rūginė
        self.Quantity_pilno_grūdo = quantity_pilno_grūdo
        self.Car_space = car_space

    def __str__(self):
        return f' Kepykla: {self.Bakery_name}, kiekis kvietinės: {self.Quantity_kvietinė}, kiekis rūginės {self.Quantity_rūginė}, kiekis pilno grūdo {self.Quantity_pilno_grūdo} vnt.'

    def totalWeight(self,duona1,duona2,duona3):
        total_weight = (duona1.totalWeight(self.Quantity_kvietinė) + duona2.totalWeight(self.Quantity_rūginė) + duona3.totalWeight(self.Quantity_pilno_grūdo))
        return total_weight

    def carSpace (self):
        return self.totalWeight() / self.Car_space
