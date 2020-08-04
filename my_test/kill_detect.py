#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import json
import sys
from simonpic_msgs.msg import MultiPersons
from simonpic_msgs.msg import Person
from termcolor import colored

from time import sleep
import signal
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


def ros_kill_test():
    global pub
    rospy.init_node('ros_kill_test', anonymous=None)
    pub = rospy.Publisher('ros_kill_test', String, queue_size=100)
    # rospy.Subscriber("three_w/three_w", MultiPersons, callbackFromRecognition)
    rospy.Subscriber("two_w/who", MultiPersons, cb_recognition)
    signal(SIGINT, handler)

    # try:
    #     print "Hello"
    #     i = 0
    #     while True:
    #         i += 1
    #         print "Iteration #%i" % i
    #         sleep(1)
    # finally:
    #     print "Goodbye"

    print(rospy.is_shutdown())
    r = rospy.Rate(1)  # 10hz

    while not rospy.is_shutdown():
        print("running")
        if rospy.is_shutdown() is True:
            print("ttt")

        # print(jsonString)
        # print(jsonString)
        r.sleep()

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def cb_recognition(MultiPersons):
    conv_name = ""
    frame_id = ""
    loc_x = ""
    loc_y = ""
    loc_z = ""

    current_time = rospy.get_rostime()

#!/usr/bin/python



def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    print("kill")
    sys.exit(0)



if __name__ == '__main__':
    try:

        ros_kill_test()
    except KeyboardInterrupt as e:
        print(e)

