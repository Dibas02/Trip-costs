
days = int(input("Enter the number of days of the trip: "))
people = int(input("Enter the number of people: "))

hotel = 10000
food = 5000
transport = 8000
others = 5000

total_cost = (hotel+food+transport+others)*days*people

print("The total cost of the trip is: ", total_cost)