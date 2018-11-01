# import car class here
from car import Car

class Person:

    _all = []

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        Person._all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def occupation(self):
        return self._occupation
    @occupation.setter
    def occupation(self, new_occupation):
        self._occupation = new_occupation

    @classmethod
    def has_oldest_car(cls):
        oldest_year = sorted(list(map(lambda x:x.year,Car._all)))[0]
        for i in Car._all:
            if i.year == oldest_year:
                return i.owner.name

    @classmethod
    def drives_a(cls, car_make):
        object_list = list(filter(lambda x:x.make==car_make,Car._all))
        DA = []
        for i in object_list:
            DA.append(i.owner.name)
        return DA

    def drives_same_make_as_me(self):
        jims_make = []
        for i in Car._all:
            if i.owner.name==self.name:
                jims_make.append(i.make)
        all_makes = Person.drives_a(jims_make[0])
        return list(filter(lambda x: self.name != x,all_makes))
