from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("Bot") # define bot
bot.set_trainer(ListTrainer)      # set trainer to train the bot

# load files available in the local system. Have already downloaded chatterbot-corpus
for files in os.listdir("C:/Users/Owner\Downloads\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/"):
    # open data using the same path
    data = open("C:/Users/Owner\Downloads\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/" + files, "r").readlines()

