# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:43:12 2022

@author: 吴佳琦
"""

from abc import ABC,abstractmethod

class Tire (ABC):
    
    def Servicable(ABC):
        @abstractmethod
        def needs_service(self):
            pass
            