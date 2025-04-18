class Pet:
    def __init__(self, name, pet_type="🐾"):
        self.name = name
        self.pet_type = pet_type
        self.fullness = 5   
        self.rest = 5         
        self.mood = 5         
        self.tricks = []

    def eat(self):
        self.fullness = min(10, self.fullness + 3)
        self.mood = min(10, self.mood + 1)
        print(f"{self.pet_type} {self.name} is eating. Yum!")

    def sleep(self):
        self.rest = min(10, self.rest + 5)
        print(f"{self.pet_type} {self.name} is sleeping. Zzz...")

    def play(self):
        if self.rest >= 2:
            self.rest -= 2
            self.mood = min(10, self.mood + 2)
            self.fullness = max(0, self.fullness - 1)
            print(f"{self.pet_type} {self.name} is playing. Whee!")
        else:
            print(f"{self.pet_type} {self.name} is too tired to play!")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.pet_type} {self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"\n--- {self.name}'s Tricks ---")
            for trick in self.tricks:
                print(f"- {trick}")
            print("-----------------------\n")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Fullness: {self.fullness}/10")
        print(f"Rest: {self.rest}/10")
        print(f"Mood: {self.mood}/10")        
        
        if self.fullness <= 2:
            print("Your pet is very hungry!")
        if self.rest <= 2:
            print("Your pet is very tired!")
        if self.mood <= 2:
            print("Your pet is feeling sad!")

        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")
        else:
            print("No tricks learned yet.")
        print("-------------------------\n")
