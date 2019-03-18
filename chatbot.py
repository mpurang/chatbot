from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("Bot") # define bot
bot.set_trainer(ListTrainer)      # set trainer to train the bot
