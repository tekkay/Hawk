import os
import pyttsx3
import scrapy

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
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

for voice in voices:
    if voice.name == 'brazil':
        speaker.setProperty('voice', voice.id)
        voices = speaker.getProperty('voices')

os.system("espeak 'yield'")
