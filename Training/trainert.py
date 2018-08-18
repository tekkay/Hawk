# -*- coding: utf-8 -*-

from chatterbot import ChatBot
import twitter
import logging


api= api.TWITTER = {
    "CONSUMER_KEY": "RJYKFipMgNnwrFj63WaG1h0CI",
    "CONSUMER_SECRET": "1iISLNx1slKBzJtoyjFSJ2g9hPZzbJUgAllEFjOqKJk9A80aVk",
    "ACCESS_TOKEN": "929348089856524293-3jOe3mbj0D1bDyaMRyihi6CkfdtjKt7",
    "ACCESS_TOKEN_SECRET": "hvo6UpLSHo9EQKbUPdefUisTSxIRkyDbBY2qHlwJeCgR4"
}


logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "TwitterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./twitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"
)

chatbot.train()

chatbot.logger.info('Trenoooo!')
