#!/usr/bin/env python

"""
Takes a number for a track on the sound board and plays it over serial
"""

import rospy
from std_msgs.msg import Int64
import serial

ser = serial.Serial('/dev/ttyTHS2', 9600)
def callback(data):
    if data.data == -1:
        ser.write('q\n') # stops playback
    else:
        ser.write('#' + str(data.data) + '\n')

def sound_fx():
    rospy.init_node('sound_board_node')
    rospy.Subscriber('sound_listener', Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    sound_fx()
