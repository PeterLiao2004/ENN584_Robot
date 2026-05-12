#Go to goal!
from pibot_client import PiBot
import math
import time
import cv2
from utility_functions import wrap_to_180
bot = PiBot(ip="172.19.232.150", localiser_ip='egb439localiser2')

# Goal posisition
goal = [1.5, 1.5]
# Acceptable distance from goal to stop
acceptable_diff = 0.1

# Proportional gain for angular velocity
k = 10

W = 0.145 #width between wheels
R = 0.065 #radius of wheel

v = 10 #target velocity

while(1):
    # Gets the localiser pose, which is a list of [x, y, theta]
    pose = bot.getLocalizerPose()
    
    ## Stop condition
    # if (pose[0] > (goal[0] - acceptable_diff) or pose[0] < (goal[0] + acceptable_diff)) and (pose[1] > (goal[1] - acceptable_diff) or pose[1] < (goal[1] + acceptable_diff)):
    #     bot.setVelocity(0,0)
    #     break
    
    # If the localiser fails to give a pose, skip this loop and try again
    if pose is None:
        print("Missed pose step\n")
        time.sleep(0.2)
        continue

    # Calculate the target angle to the goal (in degrees)
    theta_targ = math.degrees(math.atan2((goal[1] - pose[1]), (goal[0] - pose[0])))
    
    # Calculate the difference between the target angle and the current angle
    theta_diff = wrap_to_180(theta_targ - pose[2])
    
    # Calculate the target angular velocity using a proportional controller
    omega_targ = k * theta_diff
    
    # Calculate the wheel velocities needed to achieve the target velocity
    theta_dot_R = v + omega_targ
    theta_dot_L = v - omega_targ
    
    # Calculation using diff drive dimensions
    # theta_dot_R = (((omega_targ*W) / 2) + (v/R))
    # theta_dot_L = ((v*R)/2 - theta_dot_R)
    
    # Set the wheel velocities
    bot.setVelocity(int(theta_dot_L), int(theta_dot_R))
    print("L:", theta_dot_L, ", R:", theta_dot_R)
    

    
