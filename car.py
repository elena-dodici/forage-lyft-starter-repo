from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery



class Car(ABC):
    # def __init__(self, last_service_date):
    #     self.last_service_date = last_service_date
    
    def __init__(self, engine: Engine, battery):
        self.engine=engine
        self.Battery = battery



    @abstractmethod
    def needs_service(self):
        pass
