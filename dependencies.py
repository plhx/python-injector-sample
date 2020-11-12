import injector
import animal


class Dependency:
    def __init__(self):
        self.injector = injector.Injector(self.__class__.configure)

    @classmethod
    def configure(self, binder):
        binder.bind(animal.Animal, to=animal.Cat)
        #binder.bind(
        #    animal.EnhancedAnimal,
        #    to=lambda: animal.EnhancedAnimal.fromanimal(animal.Cat())
        #)

_dependency = Dependency()


def resolve(klass):
    return _dependency.injector.get(klass)
