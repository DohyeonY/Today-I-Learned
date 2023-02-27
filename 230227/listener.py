#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def my_name_lisener():
    # TODO:1
    rospy.init_node('listener', anonymous=True)
    # TODO:2
    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
# TODO:3
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

if __name__ == '__main__':
    my_name_lisener()
