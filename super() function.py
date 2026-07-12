class animal():
    def __init__(self):
        print("animal constructor")
class dog(animal):
    def __init__(self):
        super().__init__()
        print("dog constructor")
dog=dog()
