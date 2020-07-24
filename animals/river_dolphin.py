from animals.animal import Animal
from traits.freshwater import Freshwater
from identifiable import Identifiable


class RiverDolphin(Animal, Freshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        Animal.__prey = {"Trout", "Mackarel", "Salmon", "Sardine"}
        self.minimum_age_in_months = 13

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey} ')

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
