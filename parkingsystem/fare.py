#fare.py
"""Consists methods and entities to work upon fare(s) for parking lot."""
import pickle
from datetime import datetime

#FUNCTIONS

class ParkingLot:
    def __init__(self, fare=0):
        self.fare = fare
        self.entries = []
        self.current_state = "state.pl"

    def originator(self, memento=None, file='state.pl'):
        if memento is not None:
            previous_state = pickle.loads(memento)
            vars(self).clear()
            vars(self).update(previous_state)
            return pickle.dumps(vars(self))
        else:
            print(vars(self))
            return pickle.dumps(vars(self))

    def undo(self, file):
        """
        delete previous action and restore previous state
        """
        return self.originator(memento=file[-2])

    def load_state_from_file(self, file=None):
        if file is None:
            file = self.current_state

        data = []
        with open(file, 'rb') as file:
            try:
                while True:
                    data += pickle.load(file)
            except EOFError:
                while True:
                    if not isinstance(data[0][0], vehicle):
                        data = data[0]

    def setFare(self, fare):
        """Shows the current fare saved(None at first),
        and asks the user to change it."""
        print("CURRENT FARE: ", fare, "per hour")
        self.fare = fare

    def calcFare(self, inTime, outTime, type):
        """Calculate fare on time for which the vehicle has been parked.
        Use a 24-hour time formats for operation on time calculation."""
        fmt = '%H:%M'
        intrvl = str(datetime.strptime(outTime,fmt) - datetime.strptime(inTime,fmt))
        intrvl = intrvl[::-1][3:8][::-1]
        intrvl = intrvl.split(':')
        amt = int(intrvl[0])*self.fare + int(intrvl[1])/60.0*self.fare*type/2
        return amt

    def getTime(self):
        """Returns a string object of current timestamp in format(24-hour) HH:MM"""
        k = str(datetime.time(datetime.now()))
        k = k[:5]
        return k

    def get_occupancy(self):
        return len(self.entries)

    def entry(self, name, phone, type, id):
        entrytime = self.getTime()
        self.entries.append(vehicle(idnum=id, type=type, entryTime=entrytime, name=name, phone=phone))
        print("\n{:40}\n".format("VEHICLE ENTERED"))
        return self.originator()

    def exit(self, id):
        exID = self.search(id)
        if exID is not None:
            it = exID.entryTime
            ot = self.getTime()
            exID.exitTime = ot
            print("Vehicle entered at %s and is exiting at %s" % (it, ot))
            print("Collect %.2f from owner!" % self.calcFare(it, ot, exID.type))
            print("\n{:40}\n".format("VEHICLE EXITED"))
            try:
                self.entries.remove(exID)
                return self.originator()

            except:
                return self.originator()
        else:
            return self.originator()


    def search(self, seID):
        for x in self.entries:
            print(x.__dict__)
            print(x)
            if x.idnum == seID:
                return x
        return None


class owner(object):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        string = ("OWNER>>""Name:" + str(self.name))
        string += (", " + "Phone:" + str(self.phone))
        return string


class vehicle(owner):

    def __init__(self, idnum, type, entryTime, name, phone):
        self.idnum = idnum
        self.type = type
        self.entryTime = entryTime
        self.exitTime = None
        owner.__init__(self, name, phone)

    def __str__(self):
        string = ("VEHICLE>>" + "Idnum:" + str(self.idnum))
        string += ("," + "type:" + str(self.type))
        string += ("," + "EntryTime:" + str(self.entryTime) + "," + "ExitTime:" + str(self.exitTime))
        print(super(vehicle, self).__str__())
        return string


#MAIN
from datetime import datetime
