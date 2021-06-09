import datetime

# Datetime python lib useful for this mini project
# https://docs.python.org/3/library/datetime.html

# This class represents a node in the BST.
class Node:

    def __init__(self, start_time, end_time, flight_number):
        self.start_time = datetime.datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.datetime.strptime(end_time, "%H:%M")
        self.flight_number = flight_number
        # Left and right child
        self.left = None
        self.right = None


# This class inserts a node in the BST based on key as start_time.
class ReservationBST:

    
        """Write your code here. This class inserts a new node is BST."""
        def __init__(self, parent, child):
            self.parent = parent
            self.child = child
            insert(self, self.parent, child)
# Here we create a insert class which takes timestamp and key as start_time as parameters.
# We just check if timestamp is None if it is return key or if its less than key insert it at right or else left and return timestamp.
def insert(self, timestamp, key):
    if timestamp is None:
        return key
    else:
        if timestamp.start_time < key.start_time:
            timestamp.right = insert(self, timestamp.right, key)
        elif timestamp.start_time > key.start_time:
            timestamp.left = insert(self, timestamp.left, key)
        else:
            return timestamp
    return timestamp


# This method checks if the requested interval overlaps any existing interval. This returns the list [root.flight_number, root.start_time, root.end_time]
# if an overlap is found. Returns None otherwise.
# You need to use datetime strptime to convert string to Date object. And then perform comparisons on datetime objects.
def runway_busy(root, request_interval):
    """This method checks for interval overlap in the BST. This takes root and interval as input and checks for collision across the tree."""
    """Write your code here"""
    # Here we declare root.start_time,root.end_time and there datetime objects with variables.  
    Interval1= root.start_time
    Interval2 = root.end_time
    Interval3 = datetime.datetime.strptime(request_interval[0], "%H:%M")
    Interval4= datetime.datetime.strptime(request_interval[1], "%H:%M")
    # Now this is used to compare whether given start_time is less than the original start time similarly we check for end_time too.
    if (Interval3<Interval1 or Interval3>Interval2) and (Interval4<Interval1 or Interval4>Interval2):
        return None
    # If the condition is staisfied it will return None if not it will return "Runway is booked for flight number" and the list given below.
    else:
        return (root.flight_number, root.start_time, root.end_time)


# This method validates the interval duration to be 30 mins exact.
# You need to use datetime strptime to convert string to Date object. And then perform comparisons on datetime objects.
def interval_validation(request_interval):
    """This method validates the requested interval duration to be exact 30 mins."""
    """Write your code here"""
    # Here we just declare the two variables with datetime object and the method to validate the interval duration for 30mins.
    t1 = datetime.datetime.strptime(request_interval[0], "%H:%M")
    t2 = datetime.datetime.strptime(request_interval[1], "%H:%M")
    # Method:
    if ((t2 - t1).seconds) / 60 == 30:
        return True
    else:
        return False


# Driver method which makes the reservation and calls all the helper methods.
def make_reservation(root, request_interval, flight_number):
    if interval_validation(request_interval):
        busy_runway = runway_busy(root, request_interval)
        if not busy_runway:
            ReservationBST(root, Node(request_interval[0], request_interval[1], flight_number))
            print("Runway reservation made for flight number " + str(flight_number) + " from " + str(request_interval[0]) + " to " + str(request_interval[1]))
        else:
            print("Runway is booked for flight number: " + str(busy_runway[0]) + " from " + str(busy_runway[1]) + " to " + str(busy_runway[2]))
    else:
        print("Please provide a half an hour interval, in 24 Hour clock military format.")



if __name__ == '__main__':

	# Root node of BST
    root = Node('11:00', '11:30', 'IND6543')

    # Making initial reservations in the BST
    make_reservation(root, ['11:35', '12:05'], 'JET9874')
    make_reservation(root, ['12:45', '13:15'], 'JET9243')

    # Following case should fail. Runway is busy
    make_reservation(root, ['10:45', '11:15'], 'VIS9000')

    # New booking. Should pass
    make_reservation(root, ['12:10', '12:40'], 'DEC6754')



