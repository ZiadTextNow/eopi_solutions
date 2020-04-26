from protocol.errors import EOPINotImplementedError


class Problem11P8Var3(object):
    def place_the_mailbox(self, buildings):
        raise EOPINotImplementedError()


class Building(object):
    def __init__(self, num_of_residents=None, distance=None):
        self.num_of_residents = num_of_residents
        self.distance = distance

    def __gt__(self, building_obj):
        return self.distance > building_obj.distance
