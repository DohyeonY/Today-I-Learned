#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    # TODO:1
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # TODO:2
    rospy.init_node('talker', anonymous=True)
    # TODO:3
    rate = rospy.Rate(1) # 10hz
    # TODO:4
    while not rospy.is_shutdown():
        my_name_talker = "/ssafy %s" % rospy.get_time()
        rospy.loginfo(my_name_talker)
        # TODO:5
        pub.publish(my_name_talker)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
