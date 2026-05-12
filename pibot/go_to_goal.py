#Go to goal!
from pibot_client import PiBot
import math
import numpy as np
import cv2
import time
bot = PiBot(ip="172.19.232.145", localiser_ip='egb439localiser2')


goal = [1.5, 1.5]
acceptable_diff = 0.1
# k = 20
k_omega = 0.2

W = 0.145 #width between wheels
R = 0.065 #radius of wheel

v = 2 # m/s target velocity

def wrap_to_180(x):
    while x < -180:
        x += 360
    while x > 180:
        x -= 360
    return x

while(1):
    pose = bot.getLocalizerPose()
    if pose is None:
        time.sleep(0.2)
        continue
    # if (pose[0] > (goal[0] - acceptable_diff) or pose[0] < (goal[0] + acceptable_diff)) and (pose[1] > (goal[1] - acceptable_diff) or pose[1] < (goal[1] + acceptable_diff)):
    #     bot.setVelocity(0,0)
    #     break

    x = pose[0]
    y = pose[1]
    theta = pose[2]
    # print(f'Theta" {theta}')

    # Distance to goal
    dx = goal[0] - x
    dy = goal[1] - y
    dist = math.sqrt(dx**2 + dy**2)

    # Stop condition
    if dist < acceptable_diff:
        print("Goal reached")
        bot.setVelocity(0, 0)
        break

    # Target heading
    theta_target = math.degrees(math.atan2(dy, dx))

    # Heading error
    theta_error = wrap_to_180(theta_target - theta)

    # Angular velocity command
    omega = k_omega * theta_error

    # Differential drive inverse kinematics
    wheel_right = (2*v + omega*W) / (2*R)
    wheel_left  = (2*v - omega*W) / (2*R)
    
    
    # theta_diff = wrap_to_pi(theta_targ - pose[2])
    # omega_targ = k * theta_diff
    # theta_dot_R = v + omega_targ
    # theta_dot_L = v - omega_targ
    # # theta_dot_R = (((omega_targ*W) / 2) + (v/R))
    # # theta_dot_L = ((v*R)/2 - theta_dot_R)
    
    
    
    # print("L:", theta_dot_L, ", R:", theta_dot_R)

    # bot.setVelocity(int(theta_dot_L), int(theta_dot_R))

    print("L:", wheel_left, ", R:", wheel_right)
    bot.setVelocity(int(wheel_left), int(wheel_right))
    
    # write a sensible stop condition here...
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     bot.setVelocity(0,0)
    #     break

    time.sleep(0.1)
