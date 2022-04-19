class Car:
    def __init__(self, title, model):
        self.title = title
        self.model = model

class Create_car(Car):
    def start_engine(self):
        print(f"Engine on {self.title} {self.model} started!")
    def stop_engine(self):
        print(f"Engine on {self.title} {self.model} stoped!\n")
    def get_car_info(self):
        print (f'\n{self.title} {self.model}')