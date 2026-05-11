import cv2
from pibot_client import PiBot

bot = PiBot('172.19.232.188', localiser_ip='egb439localiser2')

pose = bot.getLocalizerPose()



image = bot.getLocalizerImage()
print(f"image size {image.shape[0]} by {image.shape[1]}")


cv2.imshow("windowName",image) # Display it
cv2.waitKey()