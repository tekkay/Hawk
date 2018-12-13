# -*- coding: utf-8 -*-
import random
import time
import pyautogui
import smtplib

import comtypes.client as ct
import requests as rq
import speech_recognition as sr
from selenium import webdriver
import imaplib
import email
from twython import Twython

import os
import mimetypes
from bs4 import BeautifulSoup as bs
from chatterbot import ChatBot
"""from chatterbot.trainers import ListTrainer"""
from chatterbot.trainers import ChatterBotCorpusTrainer
from googlesearch import search
import webbrowser

consumer_key = "",
consumer_secret = "",
access_token = "",
access_token_secret = ""

"""from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)"""

tts = ct.CreateObject("sapi.SPVoice")
r = sr.Recognizer()

def recVoz(r):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            speech = r.recognize_google(audio,language='pt-BR')
            return speech
    except sr.UnknownValueError:
        print('Erro de reconhecimento de fala')
        time.sleep(2)
        main()

def twit():

    twitter = Twython (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    texto = (u"O que deseja twitar?")
    tts.Speak (texto)
    speech = recVoz (r)
    message = speech
    twitter.update_status(status=message)
    print(message)

    main()


def piadas():
        aleatorio = random.randint(1, 7)
        url = 'https://www.piadas.com.br'
        page = rq.get(url=url, timeout=2)
        soup = bs(page.content, 'html.parser')
        if aleatorio == 1:
            conteudo = soup.find(class_="views-row views-row-2 views-row-even")
        elif aleatorio == 2:
            conteudo = soup.find(class_="views-row views-row-3 views-row-even")
        elif aleatorio == 3:
            conteudo = soup.find(class_="views-row views-row-4 views-row-even")
        elif aleatorio == 4:
            conteudo = soup.find(class_="views-row views-row-5 views-row-even")
        elif aleatorio == 5:
            conteudo = soup.find(class_="views-row views-row-6 views-row-even")
        elif aleatorio == 6:
            conteudo = soup.find(class_="views-row views-row-7 views-row-even")
        elif aleatorio == 7:
            conteudo = soup.find(class_="views-row views-row-8 views-row-even")
        piada = conteudo.get_text()
        print('Hawk: ...')
        texto = (u""+piada)
        tts.Speak(texto)
        main()


def noticias():
    print ('Hawk: Jaja lhe digo as últimas notícias')
    pesquisa = (u"Jaja lhe digo as últimas notícias")
    tts.Speak (pesquisa)
    speech = recVoz (r)
    print ('Você: ', speech)
    url = "https://g1.globo.com"
    page = rq.get (url=url, timeout=3)
    soup = bs (page.content, 'html.parser')
    conteudo = soup.find(class_="feed-post")
    paragrafo = conteudo.find('a')
    texto = paragrafo.get_text()
    print ('Hawk: ' + texto)
    pesquisa = (u"" + texto)
    tts.Speak(pesquisa)
    main()

def pesqGoogle():
    print("Hawk:Pesquisar sobre?")
    sobre = (u"pesquisar sobre?")
    tts.Speak(sobre)
    speech = recVoz(r)
    print('Você: ', speech)
    result = speech.replace(" ", '')
    pesquisa = (u"Pesquisando"+speech)
    tts.Speak (pesquisa)
    if result is not None:
        for url in search(speech, stop=3):
            webbrowser.open_new_tab(url)
            break
    main()

def wikipedia_search():
    print('Hawk: Qual tema deseja pesquisar?')
    pesquisa = (u"Qual tema deseja pesquisar?")
    tts.Speak(pesquisa)
    speech = recVoz(r)
    print('Você: ', speech)
    busca = speech.replace(" ", '_')
    url = "https://pt.wikipedia.org/wiki/"+busca
    page = rq.get(url=url)
    soup = bs(page.content, 'html.parser')
    conteudo = soup.find(id="mw-content-text")
    paragrafo = conteudo.find('p')
    texto = paragrafo.get_text()
    print('Hawk: '+texto)
    pesquisa = (u""+texto)
    tts.Speak(pesquisa)
    def write(texto, busca, encoding='utf-8', errors='strict'):
        data = str(texto).encode(encoding, errors=errors)
        try:
            with open(busca, 'wb') as f:
                f.write(data)
        except IOError as e:
            if e.errno == 2:
                os.makedirs(os.path.dirname(busca), exist_ok=True)
                return write(texto, busca, encoding, errors)
            else:
                raise e
    main()

def email():
    fromaddr="tekkaay@gmail.com"
    deseja = (u"Deseja mandar email para quem?")
    tts.Speak (deseja)
    speech = recVoz (r)
    toaddr=(speech+ "@unipam.edu.br")
    msg = (u"Qual a mensagem?")
    tts.Speak (msg)
    speechm = recVoz (r)
    message=speechm
    password=''
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddr, message)
    enviado = (u"Mensagem enviada")
    tts.Speak (enviado)
    server.quit()

    main()
def ler():
    username = 'tekkaay@gmail.com'
    password = ''

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)

    mail.select("inbox")

    result, data = mail.uid('search', None, "ALL")

    inbox_item_list = data[0].split()

    for item in inbox_item_list:
        result2, email_data = mail.uid('fetch', item, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        to_ = email_message['To']
        from_ = email_message['From']
        subject_ = email_message['Subject']
        date_= email_message['date']
        counter = 1
        for part in email_message.walk():
            if part.get_content_maintype() == "multipart":
                continue
            filename = part.get_filename()
            content_type = part.get_content_type ()
            if not filename:
                ext = mimetypes.guess_extension(part.get_content_type())
            if not ext:
                ext = '.bin'
            if 'text' in content_type:
                ext = '.txt'
            elif 'html' in content_type:
                ext = '.html'
                filename = 'msg-part-%08d%s' %(counter, ext)
            counter += 1



        if "plain" in content_type:

            pass
        elif "html" in content_types:
            html_ = part.get_payload()
            soup = bs(html_, "html.parser")
            text = soup.get_text()
            print(subject_)
            print(text)
            texto = (u"" + text)
            tts.Speak (texto)
        else:
            pass
    main()

def facebook():
    print ("Hawk:Procurar por quem?")
    sobre = (u"procurar por quem?")
    tts.Speak (sobre)
    speech = recVoz (r)
    print ('Você: ', speech)
    result = speech
    pesquisa = (u"Pesquisando" + speech)
    tts.Speak (pesquisa)

    if result is not None:
        for url in search (speech, stop=3):
            browser = webdriver.Firefox()
            browser.get('https://www.facebook.com')
            pyautogui.typewrite('wellington-vzt@hotmail.com')
            pyautogui.press('tab')
            pyautogui.typewrite('')
            pyautogui.press ('enter')
            time.sleep(5)
            browser.get('https://www.facebook.com/' + speech)
            retorno = (u"Encontrado")
            tts.Speak (retorno)
            time.sleep(5)
        """""""""
        btn = browser.find_element_by_xpath ('//*[@id="u_0_18"]')
        pyautogui.click (btn)
        retornoM = (u"Qual sua mensagen?")
        tts.Speak (retornoM)
        speechm = recVoz (r)
        pyautogui.typewrite (speechm)
        time.sleep (5)
        pyautogui.press ('enter')"""
    main()

def traduzir():
    print('Fale o que deseja traduzir...')
    speech = recVoz(r)
    print('Você: ', speech)
    texto = speech.replace(" ", '%20')
    origem = 'pt'
    destino = 'en'
    url = "https://translate.google.com.br/?hl=pt-BR#"+origem+"/"+destino+"/"+texto
    os.system(
        "cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "+url)
    main()

bot = ChatBot('Hawk')

"""
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
	"chatterbot.corpus.portuguese.greetings",
	"chatterbot.corpus.portuguese.conversations",
    "chatterbot.corpus.portuguese.compliment",
    "chatterbot.corpus.portuguese.proverbs",
    "chatterbot.corpus.portuguese.suggestions",
    "chatterbot.corpus.portuguese.linguistic_knowledge",
    "chatterbot.corpus.portuguese.trivia"
)"""

def treinoExtra(bot):
    print('Treinando Diálogo\n')
    titulo = (u"Treinando Diálogo")
    tts.Speak(titulo)

    print('\nFale uma pergunta: ')
    pergunta = (u"Fale uma pergunta")
    tts.Speak(pergunta)
    print('Bot: ...')
    speech = recVoz(r)
    print('Você: ', speech)
    pergunta = speech

    print('\nFale a resposta: ')
    resposta = (u"Fale a resposta")
    tts.Speak(resposta)
    print('Bot: ...')
    speech = recVoz(r)
    print('\nVocê: ', speech)
    resposta = speech

    extra = [pergunta, resposta]
    bot.set_trainer(ChatterBotCorpusTrainer)
    bot.train(extra)

def main():
    os.system('cls')
    print('\n\t\t.:: Hawk 0.2 - Beta - by Tekkay Teck ::.\n\n')



    while True:
                print('Fale algo...')
                speech = recVoz(r)
                print('Você: ', speech)

                if speech == "pesquisar" or speech == "pesquisar no google" or speech == "pesquisar no Google":
                    pesqGoogle()
                elif speech == "Facebook" or speech == "procure":
                    facebook()
                elif speech == "Email" or speech == "e-mail":
                    email()
                elif speech == "ler e-mail" or speech == "Ler e-mail":
                    ler()
                elif speech == "notícias" or speech == "quais as notícias":
                    noticias()
                elif speech == "pesquisar no Wikipédia" or speech == "Wikipédia":
                    wikipedia_search()
                elif speech == "traduzir" or speech == "translate" or speech == "Translator":
                    traduzir()
                elif speech == "treinar" or speech == "treinar dialogo":
                    treinoExtra(bot)
                elif speech == "Tuiter" or speech == "Twitter":
                    twit ()
                elif speech == "estou com fome":
                    url = "https://www.google.com.br/maps/search/restaurantes+perto+de+Patos+de+Minas,+MG/@-18.5803453,-46.5229059,15z/data=!3m1!4b1"
                    os.system('cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe '+url)
                    main()
                elif speech == "procurar" or speech == "search for" or speech == "Google maps" or speech == "mapa" or speech == "maps" or speech == "procurar em Patos de Minas" or speech == "procurar nas proximidades":
                    print('Hawk: ...')
                    speech = recVoz(r)
                    print('Você: ', speech)
                    busca = speech.replace(" ", '+')
                    url = 'https://www.google.com.br/maps/search/'+busca+'/@-18.6352307,-46.9768357,9z'
                    os.system('cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "'+url+'" ')
                    main()
                elif speech == "clima para hoje" or speech == "clima" or speech == "weather":
                    time.sleep(2)
                    url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/84/vazante-mg"
                    page = rq.get(url=url, timeout=2)
                    soup = bs(page.content, 'html.parser')
                    content = soup.find(id="tempMin0")
                    minima = content.get_text()
                    content = soup.find(id="tempMax0")
                    maxima = content.get_text()
                    content = soup.find(id="content0")
                    classe = content.find(class_="small-4 left rain-block")
                    prob = classe.get_text()
                    content = soup.find(id="content0")
                    classe = content.find(class_="left font14 txt")
                    descricao = classe.get_text()
                    tempo = (u"Minima de "+minima +" e máxima de "+maxima)
                    tts.Speak(tempo)
                    print(tempo)
                    chuva = (u"Probabilidade de "+prob)
                    tts.Speak(chuva)
                    desc = (u""+descricao)
                    tts.Speak(desc)
                    print(desc)
                    main()
                elif speech == "clima para amanhã" or speech == "clima para amanhã em Vazante" or speech == "clima amanhã":
                    time.sleep(2)
                    url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/84/vazante-mg"
                    page = rq.get(url=url, timeout=2)
                    soup = bs(page.content, 'html.parser')
                    content = soup.find(id="tempMin1")
                    minima = content.get_text()
                    content = soup.find(id="tempMax1")
                    maxima = content.get_text()
                    content = soup.find(id="content1")
                    classe = content.find(class_="small-4 left rain-block")
                    prob = classe.get_text()
                    content = soup.find(id="content1")
                    classe = content.find(class_="left font14 txt")
                    descricao = classe.get_text()
                    tempo = (u"Minima de "+minima +" e máxima de "+maxima)
                    tts.Speak(tempo)
                    print(tempo)
                    chuva = (u"Probabilidade de "+prob)
                    tts.Speak(chuva)
                    desc = (u""+descricao)
                    tts.Speak(desc)
                    print(desc)
                    main()
                elif speech == "curiosidades do dia" or speech == "curiosidades":
                    url = 'https://pt.wikipedia.org/wiki/Wikipédia:Página_principal'
                    page = rq.get(url=url)
                    soup = bs(page.content, 'html.parser')
                    conteudo = soup.find(id="mf-efemérides")
                    texto = conteudo.get_text()
                    print('Hawk: ...')
                    pesquisa = (u""+texto)
                    tts.Speak(pesquisa)
                    main()
                elif speech == "comparar preços" or speech == "pesquisar produto" or speech == "comparar preço" or speech == "pesquisar produtos":
                    pesquisa = (u"Qual o produto desejado?")
                    tts.Speak(pesquisa)
                    speech = recVoz(r)
                    print('Você: ', speech)
                    busca = speech.replace(" ", '+')
                    url = "https://www.google.com.br/search?tbm=shop&q="+busca
                    print("Segue lista com comparação de preços de "+speech+"")
                    pesquisa = (u"Segue lista com comparação de preços de "+speech)
                    tts.Speak(pesquisa)
                    os.system('cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "'+url+'" ')
                    main()
                elif speech == "tocar músicas" or speech == "reproduzir músicas":
                    os.system('cd C:\\Program Files\\MPC-HC.1.7.13.x64 && .\\mpc-hc64.exe C:\\Users\\Coêlho\\Desktop\\Music\\*.mp3')
                    main()
                elif speech == "tocar música para relaxar" or speech == "tocar uma música calma" or speech == "tocar música relaxante":
                    os.system(
                        'cd C:\\Program Files\\MPC-HC.1.7.13.x64 && .\\mpc-hc64.exe C:\\Users\\Coêlho\\Desktop\\Music\\Musica_Relaxante.mp3')
                    main()
                elif speech == "digitar" or speech == "escrever" or speech == "digite" or speech == "ditado":
                    notas = (u"Abrindo programa de digitação")
                    tts.Speak(notas)
                    os.startfile('cd C:\\Windows\\system32 && .\\notepad.exe')
                    time.sleep (5)
                    res = (u"O que devo digitar?")
                    tts.Speak (res)
                    speech = recVoz (r)
                    pyautogui.typewrite (speech)
                    main()
                elif speech == "me conte uma piada" or speech == "Me conte uma piada" or speech == "piada":
                    piadas()
                    main()
                elif speech == "fechar" or speech == "sair" or speech == "close":
                    saindo = (u"Encerrando sessão...")
                    tts.Speak(saindo)
                    exit()
                else:
                    response = bot.get_response(speech)
                    print('Hawk:', response)
                    resposta = (u""+str(response))
                    tts.Speak(resposta)
                    main()




if __name__ == "__main__":
    main()
