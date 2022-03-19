# -*- coding: utf-8 -*-


from abc import ABC,abstractmethod


class Battery(ABC):
    
    def Serviceable(ABC):
        @abstractmethod
        def needs_service(self):
            pass

