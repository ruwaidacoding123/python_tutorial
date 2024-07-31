command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("hey! what are you doing the car is already stared")
        else:
            started = True
            print("car started")
    
        
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit

              """)
    elif command == "quit":
        break
    else:
        print("sorry we dont understand that!")

