import telebot
import os
import random
from confice import token

images = os.listdir('dragons')
images2 = os.listdir('catos')
images3 = os.listdir("eco")
images4 = os.listdir("progg")
vide = os.listdir("vid")
bot = telebot.TeleBot(token)
i = 0
classs = ""

@bot.message_handler(commands=['menu'])
def menu(message):
    #name = bot.get_me()
    bot.send_message(message.chat.id, '''Привет! Это Мемный бот. Вот что я могу:
    /mem_menu - смотреть мемы
    /mem_video - смотреть видео мемы
    /send_mem - добавить свой мем в коллекцию
                     ''')
@bot.message_handler(commands=['mem_menu'])
def mem_menu(message):
    bot.send_message(message.chat.id, ''' Категории мемов:
/dragon_mem - мемы про драконов
/cat_mem - кошачьи мемы
/eco_mem - мемы про экологию
/progg_mem - мемы про программирование
                     ''')

@bot.message_handler(commands=['dragon_mem'])
def dragon_mem(message):
    random_image = random.choice(images)
    with open(f'dragons/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['cat_mem'])
def cat_memm(message):
    random_image = random.choice(images2)
    with open(f'catos/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['eco_mem'])
def eco_memm(message):
    random_image = random.choice(images3)
    with open(f'eco/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['progg_mem'])
def зкщпп_memm(message):
    random_image = random.choice(images4)
    with open(f'progg/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['mem_video'])
def зкщпп_memm(message):
    random_video = random.choice(vide)
    with open(f'vid/{random_video}', 'rb') as f:  
        bot.send_video(message.chat.id, f) 


@bot.message_handler(commands=['send_mem'])
def send_memm(message):
    global i
    i=1
    bot.send_message(message.chat.id, '''Пожалуйста, выберите категорию мема:
    /1mem - драконы
    /2mem - коты
    /3mem - экология
    /4mem - программисты
                     ''')
    
@bot.message_handler(commands=['1mem'])
def uylihg (message):
    global classs
    classs = "dragons/"
    bot.send_message(message.chat.id, '''Вы выбрали категорию мема 'драконы'. 
Отправтье мем(ы) в чат. Просим НЕ отправлять мемы с матами, черным юмором и т.п.''')

@bot.message_handler(commands=['2mem'])
def uyuihg (message):
    global classs
    classs = "catos/"
    bot.send_message(message.chat.id, '''Вы выбрали категорию мема 'коты'. 
Отправтье мем(ы) в чат. Просим НЕ отправлять мемы с матами, черным юмором и т.п.''')

@bot.message_handler(commands=['3mem'])
def uyihg (message):
    global classs
    classs = "eco/"
    bot.send_message(message.chat.id, '''Вы выбрали категорию мема 'экология'. 
Отправтье мем(ы) в чат. Просим НЕ отправлять мемы с матами, черным юмором и т.п.''')
    
@bot.message_handler(commands=['4mem'])
def uyihg (message):
    global classs
    classs = "progg/"
    bot.send_message(message.chat.id, '''Вы выбрали категорию мема 'прогграмисты'. 
Отправтье мем(ы) в чат. Просим НЕ отправлять мемы с матами, черным юмором и т.п.''')

@bot.message_handler(commands=['stop_send_mem'])
def stop_send_memm(message):
    global i
    i=0

@bot.message_handler(content_types=['photo']) # Бот будет реагировать, когда ему отправляют картинку
def send_class(message): 
    if i == 1:
        file_info = bot.get_file(message.photo[-1].file_id) # Получаем информацию о картинке
        file_name = file_info.file_path.split('/')[-1] # Получаем имя картинки
        downloaded_file = bot.download_file(file_info.file_path) # Скачиваем картику в фай
        with open(classs + file_name, 'wb') as new_file: # Создаем новый файл
            new_file.write(downloaded_file) # Сохраняем в файл картинку
        bot.send_message(message.chat.id, "Мем успешно добавлен! Чтобы закончить отправку мемов введите /stop_send_mem")
    else:
        bot.send_message(message.chat.id, "Сначала введите /send_mem")


bot.infinity_polling()
