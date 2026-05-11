#Go to goal!
from pibot_client import PiBot
import math
import numpy as np
import cv2
import time
bot = PiBot(ip="172.19.232.145", localiser_ip='egb439localiser2')


goal = [1.5, 1.5]
acceptable_diff = 0.1
k = 10

W = 0.145 #width between wheels
R = 0.065 #radius of wheel

v = 25 #target velocity

def wrap_to_pi(x):
    while x < -np.pi:
        x += 2*np.pi
    while x > np.pi:
        x -= 2*np.pi
    return x

while(1):
    pose = bot.getLocalizerPose()
    if pose is None:
        time.sleep(0.5)
        continue
    # if (pose[0] > (goal[0] - acceptable_diff) or pose[0] < (goal[0] + acceptable_diff)) and (pose[1] > (goal[1] - acceptable_diff) or pose[1] < (goal[1] + acceptable_diff)):
    #     bot.setVelocity(0,0)
    #     break


    theta_targ = math.atan2((goal[1] - pose[1]), (goal[0] - pose[0]))
    
    
    theta_diff = wrap_to_pi(theta_targ - pose[2])
    omega_targ = k * theta_diff
    theta_dot_R = v + omega_targ
    theta_dot_L = v - omega_targ
    # theta_dot_R = (((omega_targ*W) / 2) + (v/R))
    # theta_dot_L = ((v*R)/2 - theta_dot_R)
    
    
    
    print("L:", theta_dot_L, ", R:", theta_dot_R)

    bot.setVelocity(int(theta_dot_L), int(theta_dot_R))
    
    # write a sensible stop condition here...
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     bot.setVelocity(0,0)
    #     break

    time.sleep(0.1)
