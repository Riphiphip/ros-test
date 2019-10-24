#!/usr/bin/env python

import rospy
from mpu_test.msg import test_msg

def test_node():
    pub = rospy.Publisher('test_topic',test_msg, queue_size=10)
    rospy.init_node('test_node', anonymous=True)
    rate = rospy.Rate(1)
    m = test_msg()
    m.message = "Hello there!"
    m.author = "Me"
    m.variation = 14
    while not rospy.is_shutdown():
        pub.publish(m)
        rate.sleep()

if __name__ == "__main__":
    try:
        test_node()
    except rospy.ROSInterruptException: pass