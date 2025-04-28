# feedback_menu.py
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.handle_feedback import handle_feedback

def show_feedback_menu(bot, chat_id, language):
    # ReplyKeyboardMarkup uchun yangi klaviatura yaratish
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    
    # Foydalanuvchi uchun feedback tugmalari
    feedback_buttons = {
        '🌐 Русский': [("ОЧЕНЬ КРАСИВЫЙ ⭐️⭐️⭐️⭐️⭐️", "5_stars"), ("  ХОРОШИЙ ⭐️⭐️⭐️⭐️", "4_stars"),
                      ("  СРЕДНИЙ ⭐️⭐️⭐️", "3_stars"), ("ПЛОХОЙ ⭐️⭐️", "2_stars"), ("⬅️ Назад", "back")],
        "🌟 O'zbekcha": [("JUDA AJOYIB ⭐️⭐️⭐️⭐️⭐️", "5_stars"), ("YAXSHI ⭐️⭐️⭐️⭐️", "4_stars"),
                        ("O'RTACHA ⭐️⭐️⭐️", "3_stars"), (" YOMON ⭐️⭐️", "2_stars"), ("⬅️ Orqaga", "back")],
        '🇬🇧 English': [("BEAUTEOUS⭐️⭐️⭐️⭐️⭐️", "5_stars"), ("GOOD ⭐️⭐️⭐️⭐️", "4_stars"), ("MEDIUM⭐️⭐️⭐️", "3_stars"),
                       (" BAD ⭐️⭐️", "2_stars"), ("⬅️ Back", "back")]
    }

    # Tilga mos "Please rate our service" xabarini yaratish
    rate_message = {
        '🌐 Русский': "Пожалуйста, оцените наш сервис:",
        "🌟 O'zbekcha": "Iltimos, xizmatimizni baholang:",
        '🇬🇧 English': "Please rate our service:"
    }

    # Foydalanuvchi uchun tanlangan tilga mos tugmalarni qo'shish
    for text, _ in feedback_buttons.get(language, []):
        print(text)
        keyboard.add(KeyboardButton(text))

    bot.send_message(chat_id, rate_message.get(language, "Please rate our service:"), reply_markup=keyboard)

