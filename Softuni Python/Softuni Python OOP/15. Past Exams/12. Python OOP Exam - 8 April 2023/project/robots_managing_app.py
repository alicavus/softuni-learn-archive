from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

class RobotsManagingApp:
    SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    ROBOT_TYPES = {
        "FemaleRobot": FemaleRobot,
        "MaleRobot": MaleRobot
    }
    SERVICE_TYPES_FOR_ROBOT_TYPES = {
        FemaleRobot: [SecondaryService],
        MaleRobot: [MainService]
    }
    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []
    
    def add_service(self, service_type: str, name: str):
        service = self.SERVICE_TYPES.get(service_type, None)
        if service is None:
            raise Exception("Invalid service type!")
        self.services.append(service(name))
        return f"{service_type} is successfully added."
    
    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        robot = self.ROBOT_TYPES.get(robot_type, None)
        if robot is None:
            raise Exception("Invalid robot type!")
        self.robots.append(robot(name, kind, price))
        return f"{robot_type} is successfully added."
    
    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot: BaseRobot = self._get_item(self.robots, name=robot_name)
        service: BaseService = self._get_item(self.services, name=service_name)

        if service.__class__ not in self.SERVICE_TYPES_FOR_ROBOT_TYPES.get(robot.__class__, []):
            return "Unsuitable service."
        
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."
    
    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service: BaseService = self._get_item(self.services, name=service_name)
        robot: BaseRobot = self._get_item(service.robots, name=robot_name)

        if robot is None:
            raise Exception("No such robot in this service!")
        
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."
    
    def feed_all_robots_from_service(self, service_name: str):
        service: BaseService = self._get_item(self.services, name=service_name)
        cnt = 0
        for robot in self._get_items(service.robots):
            robot.eating()
            cnt += 1
        return f"Robots fed: {cnt}."
    
    def service_price(self, service_name: str):
        service: BaseService = self._get_item(self.services, name=service_name)
        price = 0.0
        for robot in self._get_items(service.robots):
            price += robot.price
        return f"The value of service {service.name} is {price:.2f}."
    
    def __str__(self):
        return "\n".join(service.details() for service in self._get_items(self.services))

    @staticmethod
    def _get_item(collection, **attributes):
        if not attributes:
            return next((item for item in collection), None)
        return next((item for item in collection if all(getattr(item, k, None) == v for k, v in attributes.items())), None)
    
    @staticmethod
    def _get_items(collection, **attributes):
        if not attributes:
            return (item for item in collection)
        return (item for item in collection if all(getattr(item, k, None) == v for k, v in attributes.items()))
    