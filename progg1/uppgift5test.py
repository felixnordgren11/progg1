
# Traffic system components

class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        self.destination = destination
        self.borntime = borntime
        self.name = 'caah'
        # Implement this constructor.
    
    def __str__(self):
        return self.name


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        self.length = length
        self.vehicle_occupation = [None for _ in range(length)]
        self.current_time = 0
        
        
        # Implement this constructor.

    def __str__(self):
        '''
        String representation of lane
        '''
        return '[' + ''.join([vehicle.destination if vehicle is not None else '.' for vehicle in self.vehicle_occupation]) + ']'

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        self.vehicle_occupation[-1] = vehicle
        
        # Implement this method.

    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        if not self.vehicle_occupation[-1] == None:
            
            
            
        
        # Implement this method.

    def step(self):
        """Execute one time step."""
        self.current_time += 1
        # Implement this method.

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        # Implement this method.

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        
        # Implement this method.

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        _num = 0
        for pos in self.vehicle_occupation:
            if not pos == None:
                _num += 1
        return _num
            
        # Implement this method.

