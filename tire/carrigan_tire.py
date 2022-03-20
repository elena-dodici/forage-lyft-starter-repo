# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:43:12 2022

@author: 吴佳琦
"""
# Tire is array 
from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self,sensorData):
        self.sensorData = sensorData
        
    def needs_service(self):
        for i in self.sensorData:
            return True if i>=0.9 else False

             