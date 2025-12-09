seat_type = input("Enter Your Preferred Seat Type (sleeper/ac/general/luxuary): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper Seat")
    case "ac":
        print("AC Seat")
    case "general":
        print("General Seat")
    case "luxuary":
        print("Luxuary Seat")
    case _:
        print("Invalid Seat")