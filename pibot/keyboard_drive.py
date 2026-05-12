from pibot_client import PiBot
import cv2
import numpy as np
import time

bot = PiBot(ip="172.19.232.150", localiser_ip="egb439localiser2")

speed = 60
turn_speed = 25

# Create a small window so OpenCV can read keyboard input
cv2.namedWindow("Keyboard Control")

print("Keyboard controls:")
print("W = forward")
print("S = backward")
print("A = turn left")
print("D = turn right")
print("SPACE = stop")
print("Q = quit")

while True:
    # Show blank image so the window stays active
    img = np.zeros((200, 400, 3), dtype=np.uint8)
    cv2.putText(img, "Click this window, then use WASD", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("Keyboard Control", img)

    key = cv2.waitKey(50) & 0xFF

    if key == ord('w'):
        # Forward: both wheels forward
        bot.setVelocity(speed, speed)
        print("Forward")

    elif key == ord('s'):
        # Backward: both wheels backward
        bot.setVelocity(-speed, -speed)
        print("Backward")

    elif key == ord('a'):
        # Turn left: left wheel backward, right wheel forward
        bot.setVelocity(-turn_speed, turn_speed)
        print("Turn left")

    elif key == ord('d'):
        # Turn right: left wheel forward, right wheel backward
        bot.setVelocity(turn_speed, -turn_speed)
        print("Turn right")

    elif key == ord(' '):
        # Stop
        bot.setVelocity(0, 0)
        print("Stop")

    elif key == ord('q'):
        # Quit safely
        bot.setVelocity(0, 0)
        print("Quit")
        break
    
    time.sleep(0.1)

cv2.destroyAllWindows()