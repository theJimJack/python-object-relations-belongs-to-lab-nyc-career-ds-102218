
class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

    @classmethod
    def all(cls):
        return Car._all

    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, new_make):
        self._make = new_make
    @make.deleter
    def make(self):
        del self._make

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, new_model):
        self._model = new_model
    @model.deleter
    def model(self):
        del self._model

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, new_year):
        self._year = new_year
    @year.deleter
    def year(self):
        del self._year

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner
    @owner.deleter
    def owner(self):
        del self._owner

    @classmethod
    def cars_driven_by(cls, title):
        selected_objects = []
        for car in cls._all:
            if car.owner.name == title:
                selected_objects.append(car)
        return selected_objects
        # from person import Person
        # return list(filter(lambda x:x.occupation==title,Person._all))
