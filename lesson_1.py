class Car:
    #иницилизатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to_location(self, location):
        print(f'Car {self.model} driving to {location}')



car_honda = Car('honda', 'red')
car_subaru = Car('subaru', 'black')


print(car_subaru)
print(f"Car model: {car_honda.model}, {car_subaru.model}")
print(car_honda)

car_honda.drive_to_location('osh')

