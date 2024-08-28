from core.data.models import FilterCriteria


class CarFilter:
    def __init__(self, criteria: FilterCriteria):
        self.criteria = criteria

    def apply(self, cars):
        filtered_cars = cars
        if self.criteria.make:
            filtered_cars = [car for car in filtered_cars if car.make == self.criteria.make]
        if self.criteria.year_from:
            filtered_cars = [car for car in filtered_cars if car.year >= self.criteria.year_from]
        if self.criteria.year_to:
            filtered_cars = [car for car in filtered_cars if car.year <= self.criteria.year_to]
        if self.criteria.price_from:
            filtered_cars = [car for car in filtered_cars if car.price >= self.criteria.price_from]
        if self.criteria.price_to:
            filtered_cars = [car for car in filtered_cars if car.price <= self.criteria.price_to]
        return filtered_cars
