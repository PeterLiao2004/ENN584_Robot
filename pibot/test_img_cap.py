import cv2
import time
from pibot_client import PiBot

bot = PiBot(ip="172.19.232.188")

print("Code starting!")


if bot.camera.available:
    print("initialise camera")
    image = bot.getImage()
    print(f"image size {image.shape[0]} by {image.shape[1]}")

    img = bot.getImage() # Grab an image from the robot
    cv2.imshow("windowName",img) # Display it
    cv2.waitKey()