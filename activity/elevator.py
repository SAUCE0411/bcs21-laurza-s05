def elevator_simulation():
    num_floors = 15
    elevator_position = 0
    target_floor = 4

    while elevator_position != target_floor:
        print("Elevator is currently on floor {}".format(elevator_position))

        if elevator_position < target_floor:
            elevator_position += 1
        else:
            elevator_position -= 1

    print("Elevator has arrived at floor {}.".format(elevator_position))
    print("Simulation complete.")

elevator_simulation()



