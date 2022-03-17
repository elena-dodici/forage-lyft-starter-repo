from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
# =============================================================================
#     def __init__(self, last_service_date, warning_light_is_on):
#         super().__init__(last_service_date)
#         self.warning_light_is_on = warning_light_is_on
# =============================================================================

    def __init(self,current_mileage,last_service_mileage,warning_light_on):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on=warning_light_on

    def need_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
