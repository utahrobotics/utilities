#!/usr/bin/env python2

"""
intermediary node between teleop and sound board
"""

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Empty

def click_options_callback(empty):
    sound_pub.publish(Int64(0))
    
def click_share_callback(empty):
    sound_pub.publish(Int64(-1))

def main():
    global sound_pub
    rospy.init_node('sound_teleop')
    rospy.Subscriber('/click_options_button', Empty, click_options_callback, queue_size=1)
    rospy.Subscriber('/click_share_button', Empty, click_share_callback, queue_size=1)
    sound_pub = rospy.Publisher('/sound_listener', Int64, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    main()
