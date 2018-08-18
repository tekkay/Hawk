
from selenium import webdriver
import main1

def facebook_search(text):
	result = None
	
	if text is not None:	
		if text.startswith('facebook'):
			result = text.replace('facebook', '')
		
	if result is not None:		
		browser = webdriver.Firefox()
		browser.get('https://www.facebook.com/public/' + '')
		btn = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div/a/img')
		btn.click()
			


def speak(text):
    speaker.say(text)
    speaker.runAndWait()
    
    
def evaluate(text):
    result = None
    
def run_cmd(cmd_type):
    result = None
