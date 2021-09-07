# Package class
# Object to store package data for easier retrieval and passing.
# Attributes for getting/setting and printing functions
from datetime import datetime
class Package(object):
    def __init__(self, package_details):
        self.package_id = int(package_details[0])
        self.address = package_details[1]
        self.city = package_details[2]
        self.state = package_details[3]
        self.zip = package_details[4]
        self.deadline = package_details[5]
        self.weight = package_details[6]
        self.notes = package_details[7]
        self.delivery_time = datetime.now
        self.departure_time = datetime.now
        self.delivery_status = "At the hub"

    def print_delivered(self):
        print(" Package ID: " + str(self.package_id) +", Address: " + self.address + ", City: " + self.city + ", State: " + self.state + ", Zip: " + self.zip + ", Deadline: " + self.deadline + ", "
              "Weight: " + self.weight + ", Notes: " + self.notes +  ", Status: " + str(self.delivery_status))

    def print_not_delivered(self):
        print(" Package ID: " + str(
            self.package_id) + ", Address: " + self.address + ", City: " + self.city + ", State: " + self.state + ", Zip: " + self.zip + ", Deadline: " + self.deadline + ", "
"Weight: " + self.weight + ", Notes: " + self.notes + ", Expected delivery: " + str(self.delivery_time))


    def print_details (self):
        print("Package ID:" + str(self.package_id))
        print("Address: " + self.address)
        print("City: " + self.city)
        print("State: " + self.state)
        print("Zip: " + self.zip)
        print("Deadline: " + self.deadline)
        print("Weight: " + self.weight)
        print("Notes: " + self.notes)
        print("Expected delivery time: " + str(self.delivery_time))
        print("Status: At the hub")




