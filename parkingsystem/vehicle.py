class owner(object):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        string = ("OWNER>>""Name:"+str(self.name))
        string += (", "+"Phone:"+str(self.phone))
        return string

class vehicle(owner):
    
    def __init__(self, idnum, model, entryTime, name,  phone):
        self.idnum = idnum
        self.model = model
        self.entryTime = entryTime
        self.exitTime = None
        owner.__init__(self, name, phone)

    def __str__(self):
        string = ("VEHICLE>>"+"Idnum:"+str(self.idnum))
        string += (","+"Model:"+str(self.model))
        string += (","+"EntryTime:"+str(self.entryTime)+","+"ExitTime:"+str(self.exitTime))
        print(super(vehicle,self).__str__())
        return string