#Go to goal!
from pibot_client import PiBot
import math
import time
import cv2
from utility_functions import wrap_to_pi
bot = PiBot(ip="172.19.232.150", localiser_ip='egb439localiser2')

# Goal posisition
goal = [1.5, 1.5]
# Acceptable distance from goal to stop
acceptable_diff = 0.1

# Proportional gain for angular velocity
k = 15

max_speed = 60

W = 0.145 #width between wheels
R = 0.065 #radius of wheel

v_linear = 50 #target linear velocity

while(1):
    # Gets the localiser pose, which is a list of [x, y, theta]
    pose = bot.getLocalizerPose()
    
    # If the localiser fails to give a pose, skip this loop and try again
    if pose is None:
        print("Missed pose step\n")
        time.sleep(0.2)
        continue
    
    ## Stop condition
    distance_to_goal = math.sqrt((goal[0] - pose[0])**2 + (goal[1] - pose[1])**2)
    
    if distance_to_goal < acceptable_diff:
        bot.setVelocity(0, 0)
        print("Goal reached")
        break

    # Calculate the target angle to the goal (in radians)
    theta_targ = math.atan2((goal[1] - pose[1]), (goal[0] - pose[0]))
    
    # Calculate the difference between the target angle and the current angle
    theta_diff = wrap_to_pi(theta_targ - math.radians(pose[2]))
    
    # Calculate the target angular velocity using a proportional controller
    omega_targ = k * theta_diff

    # Calculate the wheel velocities needed to achieve the target velocity
    theta_dot_R = v_linear + omega_targ
    theta_dot_L = v_linear - omega_targ
    # Cap wheel velocity
    # theta_dot_R = max(min(theta_dot_R, max_speed), -max_speed)
    # theta_dot_L = max(min(theta_dot_L, max_speed), -max_speed)
    
    # Calculation using diff drive dimensions
    wheel_R = (v_linear + omega_targ * W / 2) / R
    wheel_L = (v_linear - omega_targ * W / 2) / R
    
    # Set the wheel velocities
    bot.setVelocity(int(theta_dot_L), int(theta_dot_R))
    print("L:", theta_dot_L, ", R:", theta_dot_R, "theta_diff:", theta_diff, "target_theta:", theta_targ)
    

    
