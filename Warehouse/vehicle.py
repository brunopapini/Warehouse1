from Warehouse.position import *
from Warehouse.ping import *


class Vehicle(object):

    def __init__(self, name):
        self.name = name
        self.pings = []

    def __str__(self):
        return "{},{}".format(self.name,self.pings)

    def get_name(self):
        """
        The name of the vehicle.
        """
        return self.name

    def get_pings(self):
        """
        The pings for the vehicle, in chronological order (earliest first).
        """
        pings=self.pings
        return pings

    def add_pings(self,ping):
        self.pings.append(ping)

    def __getitem__(self, x):
         return self.pings[x]

    def get_total_distance(self):
        positions = []
        distance = 0
        for ping in self.pings:
            positions.append(ping.get_position())
        for i in range(1,len(positions)):
            distance += get_distance(positions[i-1],positions[i])
        return distance

    def get_average_speed(self):
        distance= self.get_total_distance()
        sum_time=0
        pings= self.get_pings()
        for i in range(1,len(pings)):
            sum_time+=seconds_between(pings[i-1],pings[i])

        if sum_time!=0:
            avg_speed= (distance/sum_time)
        else:
            avg_speed="Lapse time is 0 between pings"

        return avg_speed
