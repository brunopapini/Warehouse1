from Warehouse.position import *
#PING-->
"""A Ping represents a vehicle's position at a given timestamp."""

class Ping(object):

    def __init__(self, x, y, timestamp):
        self.position = Position(x, y)
        # Timestamp of the ping, in seconds since the epoch.
        self.timestamp = timestamp

    def get_position(self):
        return self.position

    def get_timestamp(self):
        # timestamp in seconds since a fixed (but arbitrary) epoch.
        return self.timestamp

    def __str__(self):
        return "{},{}".format(self.position,self.timestamp)

    def __eq__(self, other):
        if not isinstance(other, Ping):
            return False

        return (self.position == other.get_position() and self.timestamp== other.get_timestamp())

def seconds_between(ping1, ping2):
    """
    Determines the number of seconds between two given Pings. The result is
    positive if ping1 is earlier than ping2.
    """
    return ping2.get_timestamp() - ping1.get_timestamp()
