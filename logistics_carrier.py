from abc import ABC, abstractmethod
from datetime import datetime
class LogisticsCarrier(ABC):
    @abstractmethod
    def verify_route(self):
        pass
    
    @abstractmethod
    def initiate_dispatch(self):
        pass
    
    def log_timestamp(self):
        tracking_number = "ITEM" + datetime.now().strftime("%d%Y")
        timestamp = datetime.now()
        return f"Tracking Number: {tracking_number} | Timestamp: {timestamp}"
    
class DroneDelivery(LogisticsCarrier):
    def verify_route(self):
        return "Drone Delivery\nVerifying Route: Checking airspace regulatory restrictions and battery range requirements."
    
    def initiate_dispatch(self):
        return "Initiating Dispatch: Spools up electronic rotors and takes off vertically toward the target waypoint."
    
class FreightShipping(LogisticsCarrier):
    def verify_route(self):
        return "Freight Shipping\nVerifying Route: Evaluating marine channel depth and port congestion logs."
    
    def initiate_dispatch(self):
        return "Initiating Dispatch: Clearing customs documentation and fires up diesel marine propulsion engines."
    
class AutonomousTruck(LogisticsCarrier):
    def verify_route(self):
        return "Autonomous Truck\nVerifying Route: Cross-referencing highway traffic databases and toll network systems."
    
    def initiate_dispatch(self):
        return "Initiating Dispatch: Engaging highway cruise driving systems and leaves the local distribution bay."

print("--------------- Logistics Process ---------------")
logistics = [DroneDelivery(), FreightShipping(), AutonomousTruck()]
for logistic in logistics:
    print(logistic.verify_route())
    print(logistic.initiate_dispatch())
    print(logistic.log_timestamp())
    print()
