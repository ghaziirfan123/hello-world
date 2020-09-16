# my name is mohammad irfan and my peoplesoft is 1626488
service_schedule = {"-": 0, "Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")
first_service = input("Select first service:")
print("")
second_service = input("Select second service:")
print("")
print("Davy's auto shop invoice")
print("")
if (first_service == "-"):
    print("Service 1: No service")
else:
    print("Service 1: {:s}, ${:d}".format (first_service, service_schedule.get(first_service)))
if (second_service == "-"):
    print("Service 2: No service")
else:
    print("Service 2: {:s}, ${:d}".format (second_service, service_schedule.get(second_service)))
invoice_total = service_schedule.get(first_service) + service_schedule.get(second_service)
print("Total: ${:d}".format(invoice_total))