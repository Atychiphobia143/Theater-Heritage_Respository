# Abstraction: Using simple and clear class interfaces to hide complex details from the user
class Play:
    # Encapsulation: Using the constructor to initialize instance variables
    def __init__(self, title, playwright, genre):
        self.title = title  # Encapsulation: These are instance variables
        self.playwright = playwright  # Encapsulation: These are instance variables
        self.genre = genre  # Encapsulation: These are instance variables

    # Abstraction: Providing a simple method to display play information
    def display_info(self):  
        print(f"Title: {self.title}")
        print(f"Playwright: {self.playwright}")
        print(f"Genre: {self.genre}")

# Inheritance: Musical is a subclass of Play, inheriting its properties and methods
class Musical(Play):  
    def __init__(self, title, playwright, genre, composer):
        super().__init__(title, playwright, genre)
        self.composer = composer  # Encapsulation: This is an instance variable specific to Musical

    # Polymorphism: Overriding the display_info method to include composer information
    def display_info(self):  
        super().display_info()
        print(f"Composer: {self.composer}")

# Inheritance: Comedy is a subclass of Play, inheriting its properties and methods
class Comedy(Play):  
    def __init__(self, title, playwright, genre, main_character):
        super().__init__(title, playwright, genre)
        self.main_character = main_character  # Encapsulation: This is an instance variable specific to Comedy

    # Polymorphism: Overriding the display_info method to include main character information
    def display_info(self):  
        super().display_info()
        print(f"Main Character: {self.main_character}")

# Classes and Objects: Creating objects (instances of the classes)
play1 = Play("Hamlet", "William Shakespeare", "Tragedy")  # Object instance of Play
musical1 = Musical("The Lion King", "Roger Allers", "Musical", "Elton John")  # Object instance of Musical
comedy1 = Comedy("The Importance of Being Earnest", "Oscar Wilde", "Comedy", "Jack Worthing")  # Object instance of Comedy

# Access methods
play1.display_info()
print()
musical1.display_info()
print()
comedy1.display_info()

