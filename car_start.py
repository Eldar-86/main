def car():
    car = False
    while True:
        commands = ["start", "stop", "exit"]
        car_start = input("> ").lower()

        if car_start == "start" and car == False:
            print("car started")
            car = True
        elif car_start == "start" and car == True:
            print("car already started")

        if car_start == "stop" and car == True:
            print("car stopped")
            car = False
        elif car_start == "stop" and car == False:
            print("car already stopped")


        if car_start == "exit":
            print("getting out of the car")
            break
        elif car_start not in commands:
            raise ValueError(1)


car()
