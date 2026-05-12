from pibot_client import PiBot
import time

bot = PiBot(ip="172.19.232.145", localiser_ip='egb439localiser1')

bot.resetEncoder()
enc_left_beg, enc_right_beg = bot.getEncoders()
print(f'Encoder starting values, L: {enc_left_beg}, R: {enc_right_beg}')
while(1):
    bot.setVelocity(20, 20)
    pose = bot.getLocalizerPose()
    enc_left_end, enc_right_end = bot.getEncoders()
    print(f'Encoder starting values, L: {enc_left_end}, R: {enc_right_end}')
    print(f'Encoder difference, L: {enc_left_end-enc_left_beg}, R: {enc_right_end-enc_right_beg}')
    time.sleep(1)
