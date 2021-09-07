import csv
from HashTable import HashTable
from Package import Package

# Open CSV and save each row as a Package object into a HashTable
# Since this function contains 1 for loop, Big O is O(n)
# Returns hashtable with data loaded
def parse_package_csv():
    package_data = HashTable()
    with open("packages.csv", 'r', encoding="utf-8-sig") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            p = Package(row)
            package_data.add(p.package_id, p)
        return package_data
# Open file and save the data as a 2 dimensional array
# Since this function contains 1 "for" loop, Big O is O(n)
def parse_distance_csv():
    distance_data = []
    with open("distances.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            distance_data.append(row)
        return distance_data


# Open file and save the data as a 2 dimensional array
# Big O: O(n)
def parse_address_csv():
    address_data = []
    with open("addresses.csv", 'r', encoding="utf-8-sig") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            address_data.append([int(row[0]), row[1], row[2]])
        return address_data
