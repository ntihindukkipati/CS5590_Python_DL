#This class inputs the journey details and gives the flight number
class Flight:
    def __init__(self, flightNumber):
        Flight.source = input('Enter Source : ')
        Flight.destination = input('Enter Destination : ')
        print('Available Airlines :')
        print('SouthWest')
        print('American')
        print('Spirit')
        Flight.airlinesName = input('Which Airlines do you prefer : ')
        self.flightNumber = flightNumber

#This method prints the airlines details
    def print_details(self):
        print('Airlines : ', Flight.airlinesName)
        print('Flight Number : ', self.flightNumber)
        print(Flight.source, '-->', Flight.destination)
        print('******************************************************************************')

#This class gives all the employee details (Inheritance)
class Employee(Flight):
    def __init__(self, emp_id, emp_name, emp_gender):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_gender = emp_gender

#Method Overriding
    def print_details(self):
        print("Name of employee: ", self.emp_name)
        print('Employee id: ', self.emp_id)
        print('Employee gender: ', self.emp_gender)

#This class inputs all the passenger details
class Passenger:
    def __init__(self):
        Passenger.passenger_fname = input('Enter first name : ')
        Passenger.passenger_lname = input('Enter last name : ')
        Passenger.passenger_passportNo = input('Enter passport number: ')
        Passenger.passenger_gender = input('Enter gender : ')
        Passenger.passenger_class = input('Business or Economy class? : ')

#This class calculates the baggage fare based on the number of bags
class Baggage:
    def __init__(self):
        Baggage.noOfBags = int(input('Number of bags you want to checkin : '))
        Baggage.totBagFare = 0;
        Baggage.noOfBags = Baggage.noOfBags
        if(Baggage.noOfBags > 2):
            for i in range(Baggage.noOfBags-2):
                Baggage.totBagFare += 60
        print('You can take two bags for free !!! Total bag fare is for ', Baggage.noOfBags,'is ',Baggage.totBagFare)

#This class calculates the ticket cost based on the class, flight and bags (Inheritance)
class TicketCost(Baggage, Passenger, Flight):
    def __init__(self):
        TicketCost.baseCost = 100
        TicketCost.baseCost = TicketCost.baseCost + Baggage.totBagFare
        if(Passenger.passenger_class == 'business'):
            TicketCost.baseCost = TicketCost.baseCost + 100
        print('Total ticket cost is : ',TicketCost.baseCost)

#This method displays all the details that are to be on the ticket
    def ticketDisplay(self):
        print('******************************************************************************')
        print('Ticket Details')
        print('******************************************************************************')
        print('Passenger Name : ',Passenger.passenger_fname,' ', Passenger.passenger_lname)
        print('Passenger Passport Number : ',Passenger.passenger_passportNo)
        print('Gender : ', Passenger.passenger_gender)
        print('Class : ', Passenger.passenger_class)
        print('Total number of bags checked in : ', Baggage.noOfBags)
        print('Total Fare for the trip is : ',TicketCost.baseCost)


employee = Employee(567, 'Bhuvana', 'Female')
employee.print_details()
flight = Flight('KX356')


passenger = Passenger()
bags = Baggage()

ticket = TicketCost()
ticket.ticketDisplay()
flight.print_details()



