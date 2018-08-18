#-*- coding: utf-8 -*-

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot('Hawk', read_only=True)
bot.train(
	"chatterbot.corpus.portuguese.greetings",
	"chatterbot.corpus.portuguese.conversations"
)
