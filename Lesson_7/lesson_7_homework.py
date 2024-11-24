class Vehicle:
    """Vehicle class - main class"""
    def __init__(self, make, model, year):
        self.make = make
        self. model = model
        self. year = year

    def get_attr(self):
        print(self.__dict__)

    def display_info(self):
        print(f'Це {self.make} {self.model} {self.year} року виробництва.')

class Car(Vehicle):
    """Car class"""
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f'Engine of {self.make} {self.model} {self.year} starts')

    def display_info(self):
        print(f'Це {self.make} {self.model} {self.year} року виробництва з типом палива {self.fuel_type}.')

class Motorcycle(Vehicle):
    """Motorcycle class"""
    def __init__(self, make, model, year, fuel_volume):
        super().__init__(make, model, year)
        self.fuel_volume = fuel_volume

    def fuel_check(self):
        if self.fuel_volume < 10:
            print('Your tank is almost empty. Fill the tank at least to 10L')
        elif self.fuel_volume > 30:
            print(f'inappropriate volume for {self.model} {self.make} {self.year}')
        else:
            print('Your fuel is ok')

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва з об'ємом бака {self.fuel_volume}")

class Bicycle(Vehicle):
    """Bicycle Class"""
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def move(self):
        print("You are so fast")

    def display_info(self):
        print(f'Це {self.make} {self.model} {self.year} року виробництва, має {self.color} колір.')

car1 = Car('Toyota', 'Corolla', 2018, 'petrol')
car1.get_attr()
car1.start_engine()

motorcycle1 = Motorcycle('Yamaha', 'YZF-R7', 2022, 32)
motorcycle1.get_attr()
motorcycle1.fuel_check()

bicycle1 = Bicycle(model ='Crossride' , make = 'МТВ ST Bullet', year= 2021, color= 'black')
bicycle1.get_attr()
bicycle1.move()

#                                        Поліморфізм**

print("--------------------------------------------------")

vehicle_list = [
    car1,
    motorcycle1,
    bicycle1
    ]

for veh in vehicle_list:
    veh.display_info()
# Це Toyota Corolla 2018 року виробництва з типом палива petrol.
# Це Yamaha YZF-R7 2022 року виробництва з об'ємом бака 32
# Це МТВ ST Bullet Crossride 2021 року виробництва, має black колір.
