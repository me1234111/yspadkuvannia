class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    def start_engine(self):
        pass
class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
    def start_engine(self):
        print(f"The car`s engine is starting...")
class Truck(Vehicle):
    def __init__(self, make, model, year, weight,cargo_capacity,towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def haul(self):
        print(f'The{self.model} is hauling')
    def start_engine(self):
        print(f"The truck`s engine is starting...")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def ride(self):
        print("The motorcycle is riding")
    def start_engine(self):
        print("The motorcycle's engine is starting...")
car1 = Car('Suzuki','X14','2012','1000kg',4,3)   
car1.start_engine()
truck1 = Truck('Ford','X100','2010','5000kg',1000,8000)   
truck1.start_engine()    
Moto1 = Motorcycle('Toyota','G54','2020','575kg',2,True)   
Moto1.start_engine() 
