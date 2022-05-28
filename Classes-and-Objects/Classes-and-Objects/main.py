class Student:
    # Class constructor
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    # Setter Method
    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = int(age)

    def add_track(self, value):
        self.tracks.append(value)

    # Getter Method
    def get_score(self):
        return self.score

    # Print the whole details of the object
    def show_details(self):
        details = f"Name: {self.name}\nAge: {self.age}\nTracks: {self.tracks}\nScore: {self.score}"
        return details


# Bob Object
Bob = Student("Bob", 26, ["FE"], 20.90)

print("********************")
print(Bob.show_details())

Bob.change_name("Sample")
Bob.change_age(30)
Bob.add_track("Backend")

print("********************")
print(Bob.show_details())


# Tom Object
Tom = Student("Tom Sample", 16, ["BE"], 50)

print("********************")
print(Tom.show_details())

Tom.change_name("Sample Tom")
Tom.change_age(20)
Tom.add_track("UI/UX")

print("********************")
print(Tom.show_details())