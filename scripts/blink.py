#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty

def blink():
  pub = rospy.Publisher('toggle_led', Empty, queue_size=10)
  rospy.init_node('blink', anonymous=True)
  rate = rospy.Rate(1)
  while not rospy.is_shutdown():
    str = 'blink'
    rospy.loginfo(str)
    pub.publish()
    rate.sleep()

if __name__ == '__main__':
  try:
    blink()
  except rospy.ROSInterruptException:
    pass