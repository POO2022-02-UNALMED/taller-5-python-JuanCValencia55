from zooAnimales.animal import Animal
from zooAnimales.anfibio import Anfibio

if __name__ == "__main__":
    a = Animal()
    rana = Anfibio().crarRana("juan", 20, "M")
    print(rana.getHabitat())