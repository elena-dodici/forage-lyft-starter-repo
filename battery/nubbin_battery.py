# -*- coding: utf-8 -*-
from abc import ABC

#from car import Car
from battery import Battery


class NubbinBattery(Battery, ABC):

    def __init(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date



    def need_service(self):
        return self.current_date - self.last_service_date > 300

