import animal
import dependencies


if __name__ == '__main__':
    animal = dependencies.resolve(animal.EnhancedAnimal)
    print(animal.name())
