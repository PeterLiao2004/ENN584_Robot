from pibot_client import PiBot
bot = PiBot(ip="172.19.232.150")

bot.resetEncoder()
enc_left_beg, enc_right_beg = bot.getEncoders()
print(f'Encoder starting values, L: {enc_left_beg}, R: {enc_right_beg}')
bot.setVelocity(100,100,5)
enc_left_end, enc_right_end = bot.getEncoders()
print(f'Encoder starting values, L: {enc_left_end}, R: {enc_right_end}')
print(f'Encoder difference, L: {enc_left_end-enc_left_beg}, R: {enc_right_end-enc_right_beg}')

