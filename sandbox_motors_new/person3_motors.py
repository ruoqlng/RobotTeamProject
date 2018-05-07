"""
Functions for TURNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Zhengxiao Zou.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment turn_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for turn_left_by_time.
#   Then repeat for turn_left_by_encoders.
#   Then repeat for the turn_right functions.

import ev3dev.ev3 as ev3
import time


def test_turn_left_turn_right():
    """
    Tests the turn_left and turn_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs turn_left_by_time.
      3. Same as #2, but runs turn_left_by_encoders.
      4. Same as #1, 2, 3, but tests the turn_right functions.
    """
    print("--------------------------------------------")
    print("  Drive using input")
    print("--------------------------------------------")
    ev3.Sound.speak("Always look on the bright side of life").wait()

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    time_s = 1  # Any value other than 0.
    while time_s != 0:
        # turn left second
        print('turn left second')
        seconds = int(input("Enter a time in second for the right motor (second): "))
        speed = int(input("Enter a speed for the right motor (-100 to 100): "))
        stop_action = input("Enter a stop_action: ")
        print(seconds)
        turn_left_seconds(seconds, speed, stop_action)
        # turn left time(angle)
        degrees = int(input("Enter a time in degree for the right motor (degree): "))
        speed = int(input("Enter a speed for the right motor (-100 to 100): "))
        stop_action = input("Enter a stop_action: ")
        turn_left_by_time(degrees, speed, stop_action)
        # turn left encoder
        degrees = int(input("Enter a time in degree for the right motor (degree): "))
        speed = int(input("Enter a speed for the right motor (-100 to 100): "))
        stop_action = input("Enter a stop_action: ")
        turn_left_by_time(degrees, speed, stop_action)



    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()




def turn_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot turn in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the given stop_action.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor.run_forever(speed_sp=speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)




def turn_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    seconds = degrees / speed *10
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor.run_forever(speed_sp=speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)




def turn_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should turn to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor.run_to_rel_pos(position_sp = degrees*speed)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)



def turn_right_seconds(seconds, speed, stop_action=):
    """ Calls turn_left_seconds with negative speeds to achieve turn_right motion. """
    turn_left_seconds(seconds, -speed, stop_action)


def turn_right_by_time(degrees, speed, stop_action=):
    """ Calls turn_left_by_time with negative speeds to achieve turn_right motion. """
    turn_left_by_time(degrees, -speed, stop_action)

def turn_right_by_encoders(degrees, speed, stop_action=):
    """ Calls turn_left_by_encoders with negative speeds to achieve turn_right motion. """
    turn_left_by_encoders(degrees, -speed, stop_action)

test_turn_left_turn_right()