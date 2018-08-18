#-*- coding: utf-8 -*-

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot 
from selenium import webdriver

import pyautogui
import time
import os
import sys
import subprocess as s
import speech_recognition as sr
import pyttsx3
import webbrowser

speaker = pyttsx3.init()

voices = speaker.getProperty('voices')

bot = ChatBot('Hawk', read_only=True)


def facebook_search(text):
	resultf = None
	resultM = None
	
	if text is not None:
		for key in facebook_keywords:
			if text.startswith('facebook'):
				resultf = text.replace('facebook', '')
				
	if resultf is not None:
		for url in search(text, stop=3):
			browser = webdriver.Firefox()
			browser.get('https://www.facebook.com/public/' + resultf)
			btn = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div/a/img')
			btn.click()
			break
	return 'Encontrado'
	return resultf
	
	if text.startswith('mensagem'):
		resultM = text.replace('mensagem', '')
		btn = browser.find_element_by_xpath('//*[@id="u_0_1f"]')
		btn.click()
		pyautogui.typewrite(resultM)
	if text.startswith('enviar'):
		pyautogui.press('enter')
					
	return 'Pode dizer a sua mensagen'
	return resultM


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
				response = facebook_search(speech)	
				if response == None:
					response = bot.get_response(speech)
					
			print('Você: ', speech)
					
			print('Hawk: ', response)
			speak(response)
		
