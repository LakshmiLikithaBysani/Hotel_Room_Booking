print("🏨 Hotel Room Booking System")

rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    104: "Available",
    105: "Available"
}

while True:
    print("\n1. View Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nRoom Status:")

        for room, status in rooms.items():
            print("Room", room, "-", status)

    elif choice == "2":
        room = int(input("Enter room number: "))

        if room in rooms:
            if rooms[room] == "Available":
                name = input("Enter customer name: ")

                rooms[room] = "Booked"
                print("✅ Room booked successfully!")
                print("Customer:", name)
                print("Room Number:", room)
            else:
                print("❌ Room is already booked.")
        else:
            print("❌ Invalid room number.")

    elif choice == "3":
        room = int(input("Enter room number to cancel: "))

        if room in rooms:
            if rooms[room] == "Booked":
                rooms[room] = "Available"
                print("✅ Booking cancelled successfully!")
            else:
                print("Room is already available.")
        else:
            print("❌ Invalid room number.")

    elif choice == "4":
        print("Thank you for using Hotel Room Booking System!")
        break

    else:
        print("❌ Invalid choice!")
