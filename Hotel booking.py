#Contain all the room's available
class HotelBookingSystem:
    def __init__(self):
        self.customers = {}
        self.rooms = {
            101: {"type": "Single", "beds": 1, "features": ["TV"]},
            102: {"type": "Double", "beds": 2, "features": ["TV", "WiFi", "Balcony"]},
            103: {"type": "Suite", "beds": 3, "features": ["TV", "WiFi", "Bath"]},
        }
#Menu system
    def show_menu(self):
        print("1. Book a room")
        print("2. View room details")
        print("3. Check availability")
        print("4. Check out")
        print("5. Exit")
#Booking room function
    def book_room(self, customer_name, room_number):
        if room_number in self.rooms.keys():
            self.customers[customer_name] = room_number
            print(f"{customer_name} has successfully booked room {room_number}")
        else:
            print("Room not available. Please choose another room.")
#View avaialble rooms 
    def view_room_details(self, room_number):
        if room_number in self.rooms.keys():
            print(f"Room Number: {room_number}")
            print(f"Type: {self.rooms[room_number]['type']}")
            print(f"Beds: {self.rooms[room_number]['beds']}")
            print(f"Features: {', '.join(self.rooms[room_number]['features'])}")
        else:
            print("Room not found.")

    def check_availability(self):
        available_rooms = [room_number for room_number in self.rooms.keys() if room_number not in self.customers.values()]
        print("Available rooms:")
        for room_number in available_rooms:
            print(room_number)
    #Check out system
    def check_out(self, customer_name):
        if customer_name in self.customers.keys():
            room_number = self.customers.pop(customer_name)
            print(f"{customer_name} has checked out of room {room_number}")
        else:
            print("Customer not found.")


hotel_system = HotelBookingSystem()

while True:
    hotel_system.show_menu()
    choice = input("Enter your choice: ")
#Get customers information and room numbers
    if choice == '1':
        customer_name = input("Enter customer name: ")
        room_number = int(input("Enter room number: "))
        hotel_system.book_room(customer_name, room_number)
    elif choice == '2':
        room_number = int(input("Enter room number: "))
        hotel_system.view_room_details(room_number)
    elif choice == '3':
        hotel_system.check_availability()
    elif choice == '4':
        customer_name = input("Enter customer name: ")
        hotel_system.check_out(customer_name)
    elif choice == '5':
        break
    else: #logic error 
        print("Invalid choice. Please try again.")