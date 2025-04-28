from telebot import TeleBot, types
from shows.show_services import show_services_categories  # `categories_handler.py` dan import
from handlers.start_handler import start
# from handlers.language_handler import choose_language
from handlers.contact_handler import handle_contact
from handlers.name_handler import handle_name
from pymongo import MongoClient
from dotenv import load_dotenv
from handlers.hand_location import handle_location
from db import get_service_titles
from handlers.start_order import start_order_processing
import os
from shows.request_phone_number import request_phone_number
from shows.show_service_details import show_service_details
from shows.show_feedback import show_feedback_menu
from handlers.handle_feedback import handle_feedback
from handlers.order_callback import register_order_callbacks

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
mongo_uri = os.getenv("MONGO_URI")

admin_ids = [1806482236, 5691080241]

# MongoDB bilan ulanish
client = MongoClient(mongo_uri)  # MongoDB'ga ulanish

# To'g'ri ma'lumotlar bazasini olish
db = client.get_database()  # MongoDB ma'lumotlar bazasini olish

# "Sarista_service" nomli ma'lumotlar bazasi ichidan "Services" kolleksiyasini olish
collection = db.Sarista_service.Services  # Kolleksiyani olish

# Kolleksiyadagi barcha hujjatlarni topish
documents = collection.find()

bot = TeleBot(bot_token)
user_language = {}
user_profiles = {}
orders = {}
user_steps = {}  

bot.message_handler(commands=['start'])(lambda message: start(message, bot, collection, user_language))

@bot.message_handler(func=lambda message: message.text in ['🌐 Русский', "🌟 O'zbekcha", '🇬🇧 English'])
def choose_language(message):
    chat_id = message.chat.id
    user_language[chat_id] = message.text

    greetings = {
        '🌐 Русский': "Добро пожаловать в SARISHTA SERVICE! 🎉",
        "🌟 O'zbekcha": "Xush kelibsiz! O'zbek tilini tanladingiz. 🌟",
        '🇬🇧 English': "Welcome! You have chosen English. 🎉"
    }
    bot.send_message(chat_id, greetings.get(message.text, "Welcome!"))
    request_phone_number(message,user_language,bot)


@bot.message_handler(content_types=['contact'])
def request_phone_numbers(message):
    handle_contact(message,bot,user_language,user_steps)



@bot.message_handler(func=lambda message: message.text in get_service_titles(user_language.get(message.chat.id, "🌟 O'zbekcha")))
def handle_service_selection(message):
    chat_id = message.chat.id
    service_name = message.text
    language = user_language.get(chat_id, "🌟 O'zbekcha")  # Foydalanuvchi tilini olish
    
    show_service_details(bot, chat_id, service_name, language)  



@bot.message_handler(func=lambda message: user_steps.get(message.chat.id) == 'waiting_for_name')
def handle_name_wrapper(message):
    handle_name(message, bot, user_language, user_profiles, user_steps)
    print("Ism qabul qilindi!")

@bot.message_handler(content_types=['location'])
def register_location_handler(message):
    chat_id = message.chat.id
    user_id = message.chat.id
    language = user_language.get(chat_id, "🌟 O'zbekcha") 
    handle_location(message,bot,user_language)
    start_order_processing(user_id,admin_ids,bot,user_language)
    register_order_callbacks(bot, language)
    

@bot.message_handler(func=lambda message: message.text.endswith('⭐️'))
def feedback_received(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id, '🌐 Русский')
    handle_feedback(bot, message, language)
    show_services_categories(message,user_language,bot)


@bot.message_handler(func=lambda message: message.text in ["🔙 Bosh menu", "🔙 Главное меню", "🔙 Main menu"])
def handle_back_button(message):
    show_services_categories(message,user_language,bot)

# @bot.callback_query_handler(func=lambda call: call.data.startswith('order_done_'))
# def handle_order_done(call):
#     user_id = call.data.split('_')[-1]  # user_id ni olamiz
#     chat_id = call.message.chat.id
#     user_id = int(user_id)  # Ehtiyotkorlik uchun int ga o'girib olamiz
#     language = user_language.get(chat_id, '🌐 Русский')

#     # Admin xabarini yangilash yoki o'chirish (agar kerak bo'lsa)
#     bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)

#     # Foydalanuvchiga "show_feedback" yuborish
#     show_feedback_menu(bot, user_id,language)


# @bot.message_handler(func=lambda message: message.text.endswith('⭐️'))
# def feedback_callback(message):
#     chat_id = message.chat.id
#     language = user_language.get(chat_id, '🌐 Русский')
    
#     # Fikr-mulohaza uchun xabarlarni yaratish
#     feedback_request_message = {
#         '🌐 Русский': "Оставьте свой отзыв и комментарии.",
#         "🌟 O'zbekcha": "Fikr va mulohazalaringizni jo'nating.",
#         '🇬🇧 English': "Please send your feedback and comments."
#     }
    
#     # Foydalanuvchiga tilga mos fikr yuborish
#     bot.send_message(chat_id, feedback_request_message.get(language, "Please send your feedback and comments."))
    
    # handle_feedback(bot,message,language)



bot.polling()





