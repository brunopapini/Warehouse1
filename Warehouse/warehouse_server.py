from Warehouse.position import *
from Warehouse.ping import *
from Warehouse.vehicle import *


class WarehouseServer(object):


    def __init__(self):
        # vehicles is a list of vehicle instances
        self.vehicles = []

    def get_average_speeds(self):
        """
        Returns a dictionary from vehicle name to that vehicle's average speed
        for all vehicles.
        """
        avg_speeds = {}
        for vehicle in self.vehicles:
            avg_speeds[vehicle.get_name()] = vehicle.get_average_speed()
        return avg_speeds

    def add_vehicles(self, vehicle):
        self.vehicles.append(vehicle)

    def __getitem__(self, x):
        return self.vehicles[x]

    def __str__(self):
        return "Vehicles of this Warehouse: {}".format(self.vehicles)


    def get_most_traveled_since(self, max_results, timestamp):
        """
        Returns a sorted list of size max_results of vehicle names
        corresponding to the vehicles that have traveled the most distance since
        the given timestamp.
        """
        most_traveled_since=[]
        distances=[]
        #since a given timestamp, check how many distance has each car done:
        vehicles_since_time_duration = {}
        #get a list of each car from the Warehouse:
        vehicles=self.vehicles
        for vehicle in vehicles:
            vehicle.get_pings()
            pings=[]
            for ping in vehicle.get_pings() :
                # get the pings between the timestamps:
                if timestamp >= ping.get_timestamp():
                    pings.append(ping)
            for i in pings:
                #remove each ping that is before the timestamp.
                vehicle.get_pings().remove(i)
            # now I do a dict with pairs of {distance since timestamp:vehicle name}
            vehicles_since_time_duration[vehicle.get_name()] = vehicle.get_total_distance()
        print(vehicles_since_time_duration)
        vehicles_since_time_duration_sorted=sorted(vehicles_since_time_duration.items(),key=lambda x:x[1],reverse=True)
        print(vehicles_since_time_duration_sorted)
        for i in range(max_results):
            most_traveled_since.append(vehicles_since_time_duration_sorted[i][0])

        return most_traveled_since

    def check_for_damage(self):

        """
        Returns a list of names identifying vehicles that might have been damaged
        through any number of risky behaviors, including collision with another
        vehicle and excessive acceleration.
        """

        #TODO
        #check aceleration: we can get the avg speed of a forklift:
        #instantainly get the speed variation of each forklift. we need the speed of the forklift in each point.
        #speed, timestamp.
        #we can supose that in the first point, speed=0. next point we have a speed of v=x/t and so on.
        #we check each speed vs avg speed. if there is a big variation we will have big variations of

        #First: get all pings for a vehicle, and each velocity for each ping:

        #Second: get the avg speed of the vehicle


        #thirD: compare avg_speed with each speed. if the speed is 25% bigger than normal, append vehicle to check damage list.


        #CHECK COLISION:
        #for each vehicle check if they have the same ping:
        vehicle_pings={}
        #make a dict with dict[vehicle_name]=[list of pings of vehicle]
        for vehicle in self.vehicles:
                vehicle_pings[vehicle.get_name()]=vehicle.get_pings()
        #compare the lists and check if they have the same ping
        all_pings=[]
        repeted=[]
        for key,values in vehicle_pings.items():
            for i in values:all_pings.append(i)
        for i in range(1,len(all_pings)):
            if all_pings[i-1]==all_pings[i]:
                repeted.append(all_pings[i])


        return repeted
        #TODO: check if are from diferent vehicles:



    def initialize_server(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for parsed_line in reader:
                self.process_ping(
                            parsed_line[0],
                            float(parsed_line[1]),
                            float(parsed_line[2]),
                            int(parsed_line[3]))


    def process_ping(self, vehicle_name, x, y, timestamp):
        ping = Ping(x, y, timestamp)
        if len(self.vehicles) == 0 or vehicle_name != self.vehicles[-1].get_name():
            self.vehicles.append(Vehicle(vehicle_name))
        self.vehicles[-1].get_pings().append(ping)
