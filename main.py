# Name: Kevin Trinh
# Student ID: #001538705

from ReadCSV import *
from datetime import datetime, timedelta


# Get data from ReadCSV
package_data = parse_package_csv()
distance_data = parse_distance_csv()
address_data = parse_address_csv()

# Manually load the trucks with packages according to its specifications
# Truck 1 contains packages that must be delivered together
# Truck 1 contains 1 package with deadline at 9:00AM
truck_1 = [2, 34, 7, 29, 33, 40, 4, 20, 13, 15, 21, 16, 19, 14, 39]
# Truck 2 contains packages that must be delivered by truck 2 and packages that
# arrived at the hub at 9:05AM
truck_2 = [3, 18, 36, 38, 37, 6, 5, 31, 10, 11, 12, 28, 23, 24, 1]
# Remaining packages without special requirements are loaded on truck 3
truck_3 = [32, 25, 26, 27, 35, 22, 17, 9, 30, 8]


total_distance_list = []

# Utilize datetime libraries to set start time for each delivery truck
# Earliest start time for truck 1 is 8:00AM
departure_1 = datetime.now().replace(hour=8, minute=0)
# Truck 2 leaves at 9:05AM to wait for late packages to arrive at the hub
departure_2 = datetime.now().replace(hour=9, minute=5)
# Truck 3 leaves at 10:20AM after the address for package #9 is updated
departure_3 = datetime.now().replace(hour=10, minute=20)

# Returns minutes it takes to travel x distance
# O(1)
def time_calculator(distance):
    minutes = (distance/18) * 60
    return minutes

# Utilize algorithm method to get the closest address and calculate the total distance
# Delete the package from truckload after the package is delivered
# Starting point is always at the hub
# O(n^2)
def go_next_location(truck, start_time):
    # Initiate the current location with 0 to represent the hub
    current_location = 0
    total_distance = 0

    # Update all packages departure time when the truck leaves the hub
    for p_id in truck:
        package_data.get(p_id).departure_time = start_time
        
    for i in range(len(truck)):
        # Package obj, address ID, and next distance returned
        pckg, current_location, distance = algorithm(current_location, truck)

        # Add the time it takes to travel to the next address
        # Assign the value to package delivery time in datetime format
        # Truck speed is 18 miles/hour
        pckg.delivery_time = start_time + timedelta(minutes = int(time_calculator(distance)))

        pckg.delivery_status = "Delivered at " + str(pckg.delivery_time)
        total_distance += distance
        # delete the package from truck once delivered
        truck.remove(pckg.package_id)

    # Record distance/time for return to Hub from last package stop
    hub_dist = float(distance_data[current_location][0])
    total_distance += hub_dist
    start_time += timedelta(minutes = int(time_calculator(total_distance)))

    return total_distance

# Utilizes Greedy algorithm
# Takes in the truckload with a list of preloaded packages
# The algorithm will compare each possible route between the current location and the packages on the truck
# The nearest_distance value will be determined after the algorithm went through all packages on truck
# O(n^2)
def algorithm(current_address_ID, truck_load):
    # According to the provided distance matrix, the farthest distance the trucks have to
    # to travel is 14.2 miles
    # We can initially set the shortest distance as 14.2 miles or bigger
    nearest_distance = 15

    # Loop through the truck load to find the shortest distance
    # Return the next package, next address ID and the shortest distance
    # Since this is a nested loop, the Big-O time complexity is O(n^2)
    for package_ID in truck_load:
        # Assign the package using the ID number in truck_load
        package = package_data.get(package_ID)
        package_address_ID = 0

        # Iterate through each address to find the address ID of the package
        for item in address_data:
            if item[2] == package.address:
                package_address_ID = item[0]


        if package_address_ID > current_address_ID:
            distance = float(distance_data[package_address_ID][current_address_ID])
        else:
            distance = float(distance_data[current_address_ID][package_address_ID])

        # Compare each distance with the next possible route and assign
        # it to nearest_distance when we find a shorter route

        if distance < nearest_distance:
            nearest_distance = distance
            next_package = package
            next_address_ID = package_address_ID

    return next_package, next_address_ID, nearest_distance



# Main method to run the program and interact with user via console application
if __name__ == '__main__':

    # Initiate the delivery process
    t1_distance = go_next_location(truck_1, departure_1)
    total_distance_list.append(t1_distance)
    t2_distance = go_next_location(truck_2, departure_2)
    total_distance_list.append(t2_distance)
    package_data.get(9).notes = "Address updated"
    t3_distance = go_next_location(truck_3, departure_3)
    total_distance_list.append(t3_distance)

    sum = t1_distance + t2_distance + t3_distance
    total_distance_list.append(sum)

    print("Today date: " + str(datetime.now()))
    # Option menu asks for user input
    option_menu = '''
        WGUPS Delivery Option Menu:
        
        1. Look up delivery status at a specific time
        2. View delivery route information
        3. Retrieve details about a package
        4. Exit the program
    '''
    option = ""

    # The loop will continue to run unless the user enter number "4" to exit the program
    while option != "4":
        option = input(option_menu)

        # user can enter a time to get delivery status at that time
        # user must enter time in correct format
        if option == '1':
            ask_user = input("Enter time in format [HH:MM] : ")

            delivered = []
            at_hub = []
            en_route = []
            format_checker = False

            while not format_checker:
                try:
                    hour, minute = ask_user.split(":")
                    time_input = datetime.now().replace(hour=int(hour), minute=int(minute))
                    format_checker = True
                except Exception:
                    ask_user = input("Please re-enter time in correct format [HH:MM]: ")

            for i in range(1, 41):
                p = package_data.get(i)
                if p.delivery_time <= time_input:
                    delivered.append(p)
                else:
                    if time_input >= p.departure_time:
                        en_route.append(p)
                    else:
                        at_hub.append(p)

            print("Packages delivered by %s:" % ask_user)
            for p in delivered:
                p.print_delivered()
            print("\n")

            print("Packages en route at %s:" % ask_user)
            for p in en_route:

                p.print_not_delivered()

            print("\n")
            print("Packages at the hub at %s:" % ask_user)
            for p in at_hub:

                p.print_not_delivered()

        # Show distance each truck traveled and total distance all 3 trucks traveled
        elif "2" == option:

            print("Truck 1 traveled " + str(round(total_distance_list[0], 2)) + " miles")
            print("Truck 2 traveled " + str(round(total_distance_list[1], 2)) + " miles")
            print("Truck 3 traveled " + str(round(total_distance_list[2], 2)) + " miles")
            print("Total distance: " + str(round(total_distance_list[3], 2)) + " miles")

        # View specific package info using package ID from 1-40
        elif option == "3":

            ask_user = input("Enter the package ID: ")

            if int(ask_user) in range(1, 40):
                package_data.get(int(ask_user)).print_details()
            else:
                print("Wrong input")


        elif option != "4":

            print("Wrong input")
