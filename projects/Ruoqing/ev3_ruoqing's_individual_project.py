"""
This is a game for SpongeBob to find Patrick. It will send data from the EV3 to the PC.
Authors: Ruoqing Ouyang. May 2018.
"""

import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()

main()
