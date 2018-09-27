#-*- coding: utf-8 -*-

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot 
from selenium import webdriver

import scrapy
import pyautogui
import time
import os
import sys
import subprocess as s
import speech_recognition as sr
import pyttsx3
import wikipedia
from googlesearch import search
import webbrowser


wikipedia.set_lang('pt')

speaker = pyttsx3.init()

voices = speaker.getProperty('voices')

bot = ChatBot('Hawk', read_only=True)
"""
bot.train(
	"chatterbot.corpus.portuguese.greetings",
	"chatterbot.corpus.portuguese.conversations"
)"""

Noticias_keywords = ['noticias', 'noticia']



for voice in voices:
    if voice.name == 'brazil':
        speaker.setProperty('voice', voice.id)
        voices = speaker.getProperty('voices')
    
def search_noticia(text):
	result = None
	
	if text is not None:
		for key in Noticias_keywords:
			if text.startswith(key):
				result = text(key)
                
                class GloboNoticiasSpider(scrapy.Spider):
                    name = "Noticias_Spider"
                    start_urls = ['https://g1.globo.com/']

                        def parse(sel, response):
                        SET_SELECTOR= 'div.feed-post-body-title.gui-color-primary.gui-color-hover'
                        for a in response.css(SET_SELECTOR):

                            NAME_SELECTOR = 'a ::text'
                            yield {
                                'Noticia': a.css(NAME_SELECTOR).extract()
                            }
	
	return 'pesquisando'
	return result + yield

def speak(text):
    speaker.say(text)
    speaker.runAndWait()
    
    
def evaluate(text):
    result = None
    
def run_cmd(cmd_type):
    result = None
    

r = sr.Recognizer()

with sr.Microphone() as sr:
	r. adjust_for_ambient_noise(sr)
	
	while True:
		
			audio = r.listen(sr)
					
			speech = r.recognize_google(audio , language = 'pt').lower()
					
			response = run_cmd(evaluate(speech))
	
				if response == None:
					response = search_noticia(speech)	
					if response == None:
						response = bot.get_response(speech)
					
			print('Você: ', speech)
					
			print('Hawk: ', response)
			speak(response)
