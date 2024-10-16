#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Command_sub:
    def __init__(self) -> None:
        rospy.init_node("Command_subscript", anonymous=True)

        self.pub=rospy.Publisher('/cmd_vel', Twist, queue_size=1)

        rospy.Subscriber('/sending_command_topic', String, self.command_callback)
    
    def command_callback(self, data):
        rospy.loginfo("Command received: {}".format(data.data))


        velocity = Twist()

        if data.data.lower() == "forward":
            velocity.linear.x=5
        elif data.data.lower() == "backward":
            velocity.linear.x=-2
        elif data.data.lower() == "right":
            velocity.angular.z=-2
        elif data.data.lower() == "left":
            velocity.angular.z=1

        self.pub.publish(velocity)



if __name__=='__main__':
    node=Command_sub()
    rospy.spin()