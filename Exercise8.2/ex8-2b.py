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


###########################################################################
## Main Function
###########################################################################

def main():

    A = Time( 12, 25, 30 )

    print( A )
    print( repr( A ) )
    print( str( A ) )
    print()

    B = Time( 2, 25, 3 )

    print( B )
    print( repr( B ) )
    print( str( B ) )
    print()

    C = Time( 2, 25 )

    print( C )
    print( repr( C ) )
    print( str( C ) )
    print()

    D = Time()

    print( D )
    print( repr( D ) )
    print( str( D ) )
    print()

    D.from_str( "03:09:19" )

    print( D )
    print( repr( D ) )
    print( str( D ) )


if __name__ == "__main__":
    main()