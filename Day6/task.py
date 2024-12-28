def making_a_function():
    function = "Do something"
    print(function)
# Run the function. Call the function
making_a_function()


# https://reeborg.ca/index_en.html

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

def run_jump_land():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Hurdle 1
jumps = 6
while jumps > 0:
    run_jump_land()
    jumps -= 1
# #OR
#for steps in range(jumps):
#    run_jump_land()

# Hurdle 2
while not at_goal():
    run_jump_land()


# #problem_world 1,2 & 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
        if front_is_clear():
            move()
    else:
        turn_left()
