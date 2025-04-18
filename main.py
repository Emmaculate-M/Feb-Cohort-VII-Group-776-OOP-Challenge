from pet import Pet

# Create a pet object
my_pet = Pet(name="Luna", pet_type="🐾")

# Test all methods
my_pet.get_status()

my_pet.eat()
my_pet.get_status()

my_pet.sleep()
my_pet.get_status()

my_pet.play()
my_pet.get_status()

my_pet.train("roll over")
my_pet.train("play dead")
my_pet.train("roll over")  # test duplicate

my_pet.show_tricks()
my_pet.get_status()

