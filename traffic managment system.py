import time
import random

class Vehicle:
    def __init__(self, vehicle_id, speed):
        self.vehicle_id = vehicle_id
        self.speed = speed

    def move(self):
        print(f"Vehicle {self.vehicle_id} is moving at {self.speed} km/h")

class TrafficLight:
    def __init__(self):
        self.state = "green"

    def change_state(self):
        self.state = "red" if self.state == "green" else "green"

def simulate_traffic(num_vehicles, simulation_time):
    vehicles = [Vehicle(i, random.randint(30, 100)) for i in range(1, num_vehicles + 1)]
    traffic_light = TrafficLight()

    start_time = time.time()
    while time.time() - start_time < simulation_time:
        # Simulate traffic light changes every 10 seconds
        if int(time.time() - start_time) % 10 == 0:
            traffic_light.change_state()

        for vehicle in vehicles:
            if traffic_light.state == "green":
                vehicle.move()
            else:
                print(f"Vehicle {vehicle.vehicle_id} is waiting at the red light")

            # Simulate vehicle speed
            time.sleep(1 / vehicle.speed)

if __name__ == "__main__":
    num_vehicles = 5
    simulation_time = 60  # seconds

    print("Starting Traffic Simulation...")
    simulate_traffic(num_vehicles, simulation_time)
    print("Simulation completed.")
