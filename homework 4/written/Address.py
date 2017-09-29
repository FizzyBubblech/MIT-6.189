class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
    
class CampusAddress(Address):
    def __init__(self, off_num):
        Address.__init__(self, "Massachusets Ave", "77")
        self.office_number = off_num

