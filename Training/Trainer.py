#-*- coding: utf-8 -*-

from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


"""bot = ChatBot('Hawk', read_only=True)
bot.train(
	"chatterbot.corpus.portuguese.greetings"
)

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'C:/Users/XXX/Desktop/chatterbot-corpus-master/chatterbot_corpus/data/portuguese/'
"""

bot = ChatBot(
    'Default Response Example Bot', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
			'default_response': 'Me desculpe, não compreendi!.',
            'threshold': 0.90
            
        }
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.portuguese.greetings",
	'chatterbot.corpus.portuguese.compliment',
	'chatterbot.corpus.portuguese.conversations',
	'chatterbot.corpus.portuguese.games',
	'chatterbot.corpus.portuguese.linguistic_knowledge',
	'chatterbot.corpus.portuguese.money',
	'chatterbot.corpus.portuguese.proverbs',
	'chatterbot.corpus.portuguese.suggestions',
	'chatterbot.corpus.portuguese.trivia',
	'chatterbot.corpus.portuguese.unilab'	
)

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)
corpus_path = 'C:/Users/Usuario/AppData/Local/Programs/Python/Python37/Lib/site-packages/chatterbot_corpus/data/portuguese/dic.json'




