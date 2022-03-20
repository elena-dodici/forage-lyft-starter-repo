# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:43:12 2022

@author: 吴佳琦
"""

from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self,sensorData):
        self.sensorData = sensorData
        
    def needs_service(self):
        sum = 0;
        for i in self.sensorData:
            sum = sum+i;
            
        return True if sum>=3 else False
