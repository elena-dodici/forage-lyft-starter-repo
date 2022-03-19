# -*- coding: utf-8 -*-
#from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import  WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory():
    #need constructor as new type of data return

    @staticmethod   
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage):
        #order sensitive
        capulet = CapuletEngine(current_mileage,last_service_mileage);
        spindler = SpindlerBattery(last_service_date,current_date);     
        calliope = Car(capulet,spindler);
        return calliope;

    @staticmethod 
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage);
        spindler = SpindlerBattery(last_service_date,current_date);    
        glissade= Car(willoughby,spindler);
        return glissade;
    
    @staticmethod    
    def create_palindrome(current_date,last_service_date,warning_light_on):
        stern = SternmanEngine(warning_light_on);
        spindler = SpindlerBattery(last_service_date,current_date);    
        palindrome = Car(stern,spindler)
        return palindrome;
         
    @staticmethod
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage);
        nubbin = NubbinBattery(last_service_date,current_date); 
        rorscheache = Car(willoughby,nubbin)
        return rorscheache;
    @staticmethod     
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage):
        capulet = CapuletEngine(current_mileage,last_service_mileage);
        nubbin = NubbinBattery(last_service_date,current_date);     
        thovex = Car(capulet,nubbin);
        return  thovex;