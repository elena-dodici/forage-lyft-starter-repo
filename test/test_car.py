import unittest
from datetime import datetime
import sys
sys.path.append("E:/WORKSPACE/forage-lyft-starter-repo")

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import  WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car_factory.carFactory import CarFactory


class TestCalliope(unittest.TestCase):
    #test all attributes have a correct method
    #test the correctness of attributes and method themself
    
    
    current_date = datetime.today().date()
    
    def test_battery_should_be_serviced(self):
        
        last_service_date = TestCalliope.current_date.replace(year=TestCalliope.current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(TestCalliope.current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
       
        last_service_date = TestCalliope.current_date.replace(year=TestCalliope.current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(TestCalliope.current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date=current_date
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
   
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car =CarFactory.create_glissade(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
   
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_on = False

        car = CarFactory.create_palindrome(current_date,last_service_date,warning_light_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_on = False

        car = CarFactory.create_palindrome(current_date,last_service_date,warning_light_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_on = True

        car = CarFactory.create_palindrome(current_date,last_service_date,warning_light_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_on = False

        car = CarFactory.create_palindrome(current_date,last_service_date,warning_light_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car =CarFactory. create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
  
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car =CarFactory.create_thovex(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main(exit=False)
