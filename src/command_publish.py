#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class publishing_node:
    def __init__(self) -> None:
        rospy.init_node("Publishing_node", anonymous=True)
        self.pub=rospy.Publisher('/sending_command_topic', String, queue_size=1)
    
    def send(self,command):
        self.pub.publish(command)
        rospy.loginfo("Sending commnd: {}".format(command))

    def run(self):
        rospy.loginfo("Publishing_node is running")

        while not rospy.is_shutdown():
            command=input("Enter commmand: (Forward, Backward, Right, Left): ")
            self.send(command)
            rospy.sleep(1)

if __name__=='__main__':
    node=publishing_node()
    node.run()