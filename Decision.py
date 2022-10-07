#!/usr/bin/env python2

import rospy
from std_msgs.msg import String
from std_msgs.msg import Time
from nav_msgs.msg import Odometry

class Decision():
    def __init__(self):
        rospy.init_node('Decision', anonymous=True)
        rospy.Subscriber('/timer', Time, self.Time_call)
        rospy.Subscriber('/S2D', Odometry, self.Sensing_call)
        
        self.pub = rospy.Publisher('/D2S', String, queue_size=1)
        self.data_D2S = String()
        self.x_loc = 0
        self.y_loc = 0
        self.z_loc = 0

    def Time_call(self, time):
        self.data_D2S = "Hello"
        self.pub.publish(self.data_D2S)

    def Sensing_call(self, data):
        self.x_loc = data.pose.pose.position.x
        self.y_loc = data.pose.pose.position.y
        self.z_loc = data.pose.pose.position.z

        print(self.x_loc, " ",  self.y_loc, " ", self.z_loc)




Dec = Decision()
rospy.spin()