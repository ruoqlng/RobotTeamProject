"""
Functions for SPINNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Bowen Li.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment spin_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for spin_left_by_time.
#   Then repeat for spin_left_by_encoders.
#   Then repeat for the spin_right functions.


import ev3dev.ev3 as ev3
import time


def test_spin_left_spin_right():
    """
    Tests the spin_left and spin_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs spin_left_by_time.
      3. Same as #2, but runs spin_left_by_encoders.
      4. Same as #1, 2, 3, but tests the spin_right functions.
    """
    print("--------------------------------------------")
    print("spin_left_seconds")
    print("--------------------------------------------")
    ev3.Sound.speak("spin left seconds is now initiating").wait()

    seconds = 1  # Any value other than 0.
    while seconds != 0:
        speed = int(input("Enter a speed for the motor (-100 to 100 dps): "))
        seconds = int(input("Enter a time to drive (seconds): "))
        stop_action = input('Enter the stop_action: ')
        spin_left_seconds(seconds,speed,stop_action)
        print("--------------------------------------------")
        print("type in speed = 0, seconds = 0, and stop_action = brake to enter next stage")
        print("--------------------------------------------")
    print("spin_left_seconds done!")
    ev3.Sound.speak("Entering next stage").wait()

    print("--------------------------------------------")
    print("spin_left_by_time")
    print("--------------------------------------------")
    ev3.Sound.speak("spin left by time is now initiating").wait()

    degrees = 1  # Any value other than 0.
    while degrees != 0:
        degrees = int(input("Enter a degrees for spining : "))
        speed = int(input("Enter a speed for the motor (-100 to 100 dps): "))
        stop_action = input('Enter the stop_action: ')
        spin_left_by_time(degrees, speed, stop_action)
        print("--------------------------------------------")
        print("type in degrees = 0, speed = 0, and stop_action = brake to enter next stage")
        print("--------------------------------------------")
    print("spin left by time!")
    ev3.Sound.speak("Entering next stage").wait()

def spin_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot spin in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the given stop_action.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=-speed*9,stop_action=stop_action)
    right_motor.run_forever(speed_sp=speed*9,stop_action=stop_action)

    time.sleep(seconds)

    left_motor.stop()
    right_motor.stop()


def spin_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    assert left_motor.connected
    assert right_motor.connected

    degrees_in_motor = 4.5 * degrees
    time = degrees_in_motor/(abs(speed)*9)

    left_motor.run_forever(speed_sp=-speed * 9, stop_action=stop_action)
    right_motor.run_forever(speed_sp=speed * 9, stop_action=stop_action)

    time.sleep(time)

    left_motor.stop()
    right_motor.stop()

def spin_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """


def spin_right_seconds(seconds, speed, stop_action):
    """ Calls spin_left_seconds with negative speeds to achieve spin_right motion. """


def spin_right_by_time(degrees, speed, stop_action):
    """ Calls spin_left_by_time with negative speeds to achieve spin_right motion. """


def spin_right_by_encoders(degrees, speed, stop_action):
    """ Calls spin_left_by_encoders with negative speeds to achieve spin_right motion. """


test_spin_left_spin_right()