from wxpy import *

bot = Bot()
my_friends = bot.friends(update=False)
print(my_friends.stats_text())


