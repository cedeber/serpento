"""Racer"""

from microbit import *
import random

player_position = 2  # Start centered
lines = ['00000', '00000', '00000', '00000']  # No other cars on the road
cars = Image(':'.join(lines))  # Generate the cars image
collisions_line = '00000'  # No collisions at the moment
step = 0  # Used to slow down the frame rate

while True:
    # Move the cars / frame rate: higher == slower
    if step > 1:
        # Create a new empty line of cars
        new_line = list('00000')

        # Add some cars, randomly
        for i in range(1):
            rand = random.randint(0, 4)
            new_line[rand] = '5'

        # Add the new cars with the previous cars
        new_line = ''.join(new_line)
        lines = [new_line] + lines

        # Generate the image of all cars
        cars = Image(':'.join(lines))

        # Remove the last off-screen line of cars. Used to test collision
        collisions_line = lines.pop()

        # Reset the frame rate counter
        step = -1

    # Move the player
    if (button_a.is_pressed() and player_position > 0):
        player_position -= 1

    if (button_b.is_pressed() and player_position < 4):
        player_position += 1

    # Collision detection
    collision = False
    if int(list(collisions_line)[player_position]) > 0:
        collision = True

    # Clear the screen
    display.clear()

    if not collision:
        # Continue to play
        display.show(cars)
        display.set_pixel(player_position, 4, 9)
    else:
        # Show the explosion and stop the game
        display.show(Image.SAD)
        sleep(500)
        break

    # Continue the frame draw
    step += 1
    sleep(125)
