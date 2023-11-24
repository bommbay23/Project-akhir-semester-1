import telebot 
from telebot import *
from youtubesearchpython import VideosSearch
import re
import random
from googlesearch import search
import pafy
import os
api = '6577127364:AAGmkPYkWE4qB649vtsAa5dc27VZA4Fpn-4'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message,'halo apa kabar??')
 chatid = message.chat.id
 bot.send_message(chatid, 'selamat datang user')
#youtube
@bot.message_handler(commands=['cari'])
def cari(message):
  data = message.text
  video = VideosSearch(data.replace("/cari",""),limit = 3)
  x = video.result()

  for i in range(3):
    judul = x['result'][i]['title']
    url = x['result'][i]['link']
    bot.send_message(message.chat.id,judul+"\n"+url)
#google
@bot.message_handler(commands=['google'])
def google(message):
  data = message.text.replace('/google',"")
  x = search(data,num_results=4)
  for i in x :
    bot.send_message(message.chat.id,i)
#foto
@bot.message_handler(commands=['foto'])
def kirim_foto(message):
    chatid = message.chat.id

    # Specify the path to the image file
    image_path ='C:\\Users\\ASUS\\OneDrive\\Desktop\\Program Coding MARIO\\project akhir\\picture.jpeg'


    # Use bot.send_photo to send the image
    with open(image_path, 'rb') as photo:
        bot.send_photo(chatid, photo)
#mp3
@bot.message_handler(commands=['mp3'])
def musik(message):
  url = pafy.new(message.text.replace("/mp3",""))
  bot.send_message(message.chat.id,url.title)
  bot.send_message(message.chat.id,"Haraptunggu sebentar")
  hasil = url.getbestaudio()
  hasil.download(f'{url.title}.mp3')

  for i in os.listdir():
    if i.endswith(".mp3"):
      print(i)
      bot.send_audio(message.chat.id,open(i,"rb"))
      os.remove(i)



@bot.message_handler(commands=['help'])
def send_welcome(message):
 bot.reply_to(message,'apa yang bisa saya bantu??')
 bot.reply_to(message,'silahkan dipilih :')
 markup = types.ReplyKeyboardMarkup()
 item1 = types.KeyboardButton('/bantuan')
 item2 = types.KeyboardButton('/start')
 item3 = types.KeyboardButton('a')
 item4 = types.KeyboardButton('/foto')
 item5 = types.KeyboardButton('/cari')
 item6 = types.KeyboardButton('/mp3')

 markup.row(item1,item2)
 markup.row(item3,item4,item5)
 markup.row(item6)
 bot.reply_to(message,'silahkan dipilih',reply_markup = markup )

@bot.message_handler(commands=['bantuan'])
def bantuan(message):
  bot.reply_to(message,"ada yang bisa saya bantu")



#chat interactive
sapa = ['hai juga','halo juga']
@bot.message_handler(content_types=['text'])
def chatbot(message):
  teks = message.text
  if re.findall('halo|hai',teks):
    chatid = message.chat.id
    bot.send_message(chatid,random.choice(sapa))
  else :
   chatid = message.chat.id
   bot.send_message(chatid,'saya tidak mengerti') 

bot.polling()







