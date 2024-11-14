class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    return Pet(name, species, year_of_birth)

# Example of creating a new Pet object using the new_pet function
my_pet = new_pet(name="Buddy", species="Dog", year_of_birth=2018)

print(f"Pet: {my_pet.name}, Species: {my_pet.species}, Year of Birth: {my_pet.year_of_birth}")
