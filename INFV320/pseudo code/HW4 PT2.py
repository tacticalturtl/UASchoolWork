trip = open('C:/Users/Cyberbuffer/Documents/trip.txt', 'r')
export = open('C:/Users/Cyberbuffer/Documents/export.txt', 'w')

miles = 0
gallons = 0

for line in trip:
    rows = line.split()
    try:
        miles += int(rows[1])
        gallons += int(rows[2])
    except ValueError:
        pass

export.write("""total mileage: {} 
overall gas mileage: {:0.2f}""".format(miles, miles / gallons))

trip.close()
export.close()
print("All proper data has been exported to file export.txt")
