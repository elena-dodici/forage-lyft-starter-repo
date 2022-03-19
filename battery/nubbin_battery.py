# -*- coding: utf-8 -*-

from battery.battery import Battery
from add_year import addYears


class NubbinBattery(Battery):

    def __init__(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date



    def needs_service(self):
        return self.current_date > addYears(self.last_service_date,4)

