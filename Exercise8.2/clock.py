###########################################################################
## Class Clock
###########################################################################

class Time(object):
    def __init__(self, hour=0, mins=0, secs=0):
        '''Construct a time using three integers'''

        self.__hour = hour
        self.__mins = mins
        self.__secs = secs
    
    def __repr__(self):
        '''Returns a formal representation of the time'''

        out_str =  "Class Time: {:02d}:{:02d}:{:02d}" \
            .format(self.__hour, self.__mins, self.__secs)
        return out_str
    
    def __str__(self):
        '''Returns a string (hh:mm:ss) that shows time'''

        out_str = "{:02d}:{:02d}:{:02d}" \
            .format(self.__hour, self.__mins, self.__secs)

        return out_str
    
    def from_str(self, input_str):
        """ Convert a string (hh:mm:ss) into a time. """

        hour, mins, secs = [ int( n ) for n in input_str.split(":")]
            
        self.__hour = hour
        self.__mins   = mins
        self.__secs  = secs


if __name__ == "__main__":
    A = Time()
    A.from_str("10:20:03")
    print(A)