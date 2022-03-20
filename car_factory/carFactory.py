# -*- coding: utf-8 -*-
#from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import  WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
#from tire.octoprime_tire import OctoprimeTire


class CarFactory():
    #need constructor as new type of data return

    @staticmethod   
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage,sensorData):
        #order sensitive
        capulet = CapuletEngine(current_mileage,last_service_mileage);
        spindler = SpindlerBattery(last_service_date,current_date);   
        tire = CarriganTire(sensorData);
        calliope = Car(capulet,spindler,tire);
        return calliope;

    @staticmethod 
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage,sensorData):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage);
        spindler = SpindlerBattery(last_service_date,current_date);  
        tire = CarriganTire(sensorData);
        glissade= Car(willoughby,spindler,tire);
        return glissade;
    
    @staticmethod    
    def create_palindrome(current_date,last_service_date,warning_light_on,sensorData):
        stern = SternmanEngine(warning_light_on);
        spindler = SpindlerBattery(last_service_date,current_date); 
        tire = CarriganTire(sensorData);
        palindrome = Car(stern,spindler,tire)
        return palindrome;
         
    @staticmethod
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage,sensorData):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage);
        nubbin = NubbinBattery(last_service_date,current_date); 
        tire = CarriganTire(sensorData);
        rorscheache = Car(willoughby,nubbin,tire)
        return rorscheache;
    @staticmethod     
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage,sensorData):
        capulet = CapuletEngine(current_mileage,last_service_mileage);
        nubbin = NubbinBattery(last_service_date,current_date); 
        tire = CarriganTire(sensorData);
        thovex = Car(capulet,nubbin,tire);
        return  thovex;