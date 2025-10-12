class Car:
    #иницилизатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to_location(self, location):
        print(f'Car {self.model} is driving to {location}')

class Bus(Car):
    def __init__(self, model, color, seats):
        super().__init__(model, color)
        self.seats = seats



    def test_bus(self):
        print(f'bus test bus {self.color}')

    def drive_to_location(self, location):
        print(f'Bus {self.model} is driving to {location}')

print('hello world')




bus1 = Bus('Volvo', 'Red', 12 )
print(bus1.model, bus1.color, bus1.seats )
bus1.drive_to_location('Osh')
bus1.test_bus()


