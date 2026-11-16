has_good_credit = True
has_high_income = False

if has_good_credit and not has_high_income:
    print("Eligible for load")


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
command = ""
started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
           print("Car is already started!")
        else:
           started = True
           print("Car started.")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit 
              """)
    elif command == "quit":
        break
    else:
        print("I dan't understand that!!!")
