from __future__ import annotations
import abc
import injector


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError()


class Cat(Animal):
    def name(self) -> str:
        return self.__class__.__name__


class EnhancedAnimal:
    @injector.inject
    def __init__(self, animal: Animal):
        self.animal = animal

    @classmethod
    @injector.inject
    def fromanimal(cls, animal: Animal) -> EnhancedAnimal:
        return cls(animal)

    def name(self) -> str:
        return 'Enhanced {}'.format(self.animal.name())
