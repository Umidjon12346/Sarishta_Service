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
load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
mongo_uri = os.getenv("MONGO_URI")

admin_id_1 = 8197516105
admin_id_2 = 5691080241
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
    user_id = message.chat.id
    handle_location(message,bot,user_language)
    start_order_processing(user_id,admin_id_1,bot)
    start_order_processing(user_id,admin_id_2,bot)

@bot.message_handler(func=lambda message: message.text in ["🔙 Bosh menu", "🔙 Главное меню", "🔙 Main menu"])
def handle_back_button(message):
    show_services_categories(message,user_language,bot)

bot.polling()
















# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler

# # Bosqichlar
# LANGUAGE, SERVICE = range(2)

# # Xizmatlar
# services = {
#     "uz": ["🧹 Tozalash ishlari", "👶 Enaga", "🔧 Ustalar", "🎉 Event manager", "🍽 Catering", "🚰 Santexnik", "💡 Elektrik", "🧰 Yordamchi ishchi", "🌳 Bog‘bon", "🌸 Florist"],
#     "ru": ["🧹 Уборка", "👶 Няня", "🔧 Мастера", "🎉 Организатор", "🍽 Кейтеринг", "🚰 Сантехник", "💡 Электрик", "🧰 Помощник", "🌳 Садовник", "🌸 Флорист"],
#     "en": ["🧹 Cleaning", "👶 Nanny", "🔧 Craftsmen", "🎉 Event Manager", "🍽 Catering", "🚰 Plumber", "💡 Electrician", "🧰 Helper", "🌳 Gardener", "🌸 Florist"]
# }

# # Til tanlash keyboard
# language_keyboard = ReplyKeyboardMarkup(
#     [["🇺🇿 O'zbek", "🇷🇺 Русский", "🇬🇧 English"]],
#     resize_keyboard=True, one_time_keyboard=True
# )

# # Xush kelibsiz komandasi
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Iltimos, tilni tanlang / Пожалуйста, выберите язык / Please select a language:",
#         reply_markup=language_keyboard
#     )
#     return LANGUAGE

# # Til tanlanganda xizmat menyusi
# async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_lang = update.message.text
#     if "O'zbek" in user_lang:
#         lang = "uz"
#     elif "Русский" in user_lang:
#         lang = "ru"
#     else:
#         lang = "en"

#     context.user_data["lang"] = lang
#     service_buttons = [[s] for s in services[lang]]

#     await update.message.reply_text(
#         "Quyidagi xizmatlardan birini tanlang:" if lang == "uz"
#         else "Выберите одну из следующих услуг:" if lang == "ru"
#         else "Please choose one of the services below:",
#         reply_markup=ReplyKeyboardMarkup(service_buttons, resize_keyboard=True)
#     )
#     return SERVICE

# # Xizmat tanlanganda
# async def selected_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     lang = context.user_data["lang"]
#     service = update.message.text

#     response = {
#         "uz": f"Siz tanlagan xizmat: {service}",
#         "ru": f"Вы выбрали услугу: {service}",
#         "en": f"You selected the service: {service}"
#     }

#     await update.message.reply_text(response[lang])
#     return ConversationHandler.END



# # Bekor qilish
# async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Bekor qilindi / Отменено / Cancelled")
#     return ConversationHandler.END




# # Main app
# app = ApplicationBuilder().token("8082376619:AAE8UkcYvm20xUYwCp-hw4NScQVw8LvfMFk").build()

# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler("start", start)],
#     states={
#         LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_language)],
#         SERVICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, selected_service)],
#     },
#     fallbacks=[CommandHandler("cancel", cancel)],
# )

# app.add_handler(conv_handler)
# app.run_polling()