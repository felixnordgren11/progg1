
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
        self.lane_slot = [None for _ in range(length)]
        self.current_time = 0
        
        
        # Implement this constructor.

    def __str__(self):
        '''
        String representation of lane
        '''
        return '[' + ''.join([vehicle.destination if vehicle is not None else '.' for vehicle in self.lane_slot]) + ']'

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        self.lane_slot[-1] = vehicle
        
        # Implement this method.

    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        if not self.lane_slot[-1] == None:
            return ("Last space is occupied")
        else:
            return("Last space is free")
        # Implement this method.

    def step(self):
        """Execute one time step.
        self.current_time += 1
        for pos in range(self.length - 1, 0, -1):
            if not self.lane_slot[pos] == None:
                self.lane_slot[pos] = self.lane_slot[pos - 1]
        """
        self.current_time += 1
        for pos in range(self.length - 1):  # Start from the back and move to the front
            self.lane_slot[pos] = self.lane_slot[pos + 1]
        self.lane_slot[-1] = None
        
        # Implement this method.

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        if not self.lane_slot[0] == None:
            return self.lane_slot[0]
        else:
            return None
        
        # Implement this method.

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        removed_vehicle = self.lane_slot[0]
        self.lane_slot[0] = None
        return removed_vehicle
            
        
        # Implement this method.

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        _num = 0
        for pos in self.lane_slot:
            if not pos == None:
                _num += 1
        return _num
            
        # Implement this method.
        
        
def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())
    
demo_lane()






class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        self.period = period
        self.green_period = green_period
        self.current_time = 0
        self.green = True
        
    # uppdatera alla komponenter
    # presentera tillståndet (eventuellt)
        # Implement this method.

    def __str__(self):
        """Report current state of the light."""
        if not self.green == True:
            return ('(R)')
        else:
            return('(G)')
        

    def step(self):
        """Take one light time step."""
        self.current_time += 1
        if self.current_time % self.period >= self.green_period:
            self.green = False
        else:
            self.green = True
            

    def is_green(self):
        """Return whether the light is currently green."""
        if self.green == True:
            return 'True'
        else:
            return 'False'
        
            
        
def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()

'''
def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()

if __name__ == '__main__':
    main()
'''

class DestinationGenerator:
    """ Generates a sequence of destinations (None, 'W', 'S') """

    def __init__(self):
        """Add internal data."""
        self._arrivals = (  # 0:52, 1:26, 2:22
            2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1,
            2, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1,
            2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0,
            1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1)

        self._internal_time = 0
        self._total_cycle = len(self._arrivals)

    def step(self):
        """Make one time step, reporting the desination of the next vehicle
        (or None)."""
        ind = self._arrivals[self._internal_time]
        self._internal_time = (self._internal_time + 1) % len(self._arrivals)
        return 'W' if ind == 1 else 'S' if ind == 2 else None

