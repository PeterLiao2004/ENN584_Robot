from pibot_client import PiBot
import cv2
import numpy as np

bot = PiBot(ip="172.19.232.145", localiser_ip='egb439localiser2')

speed = 20

print("Controls:")
print("W = forward")
print("S = backward")
print("A = left")
print("D = right")
print("SPACE = stop")
print("Q = quit")

# Small blank window required for waitKey
img = np.zeros((200, 400, 3), dtype=np.uint8)

while True:

    cv2.imshow("PiBot Control", img)

    key = cv2.waitKey(50) & 0xFF

    left = 0
    right = 0

    # Forward
    if key == ord('w'):
        left = speed
        right = speed

    # Backward
    elif key == ord('s'):
        left = -speed
        right = -speed

    # Left
    elif key == ord('a'):
        left = -speed
        right = speed

    # Right
    elif key == ord('d'):
        left = speed
        right = -speed

    # Stop
    elif key == ord(' '):
        left = 0
        right = 0

    # Quit
    elif key == ord('q'):
        break

    bot.setVelocity(left, right)

    print(f"L={left}, R={right}")

bot.setVelocity(0, 0)
cv2.destroyAllWindows()