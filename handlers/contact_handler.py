from telebot import TeleBot
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from .add_user import add_user  # Foydalanuvchini qo'shish funksiyasi




def handle_contact(message, bot, user_language, user_profiles):
    user_id = message.chat.id
    language = user_language.get(user_id, '🌐 Русский')  # Foydalanuvchining tilini olish

    # Foydalanuvchi telefon raqami yoki boshqa ma'lumot yuborganligini tekshirish
    if message.contact:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text  # Agar telefon raqami qo'lda kiritilgan bo'lsa

    if phone_number:
        # Foydalanuvchini telefon raqami bilan qo'shamiz, ammo ismni hozircha 'None' deb saqlaymiz
        add_user(user_id, phone_number=phone_number, user_name=None)

        # Foydalanuvchining tiliga mos xabarlarni yuborish
        responses = {
            '🌐 Русский': (f"Ваш номер: {phone_number} принят. Спасибо! 🙏", "Введите ФИО:"),
            "🌟 O'zbekcha": (
                f"Sizning raqamingiz: {phone_number} qabul qilindi. Rahmat! 🙏", "Ism va familiyangizni kiriting:"),
            '🇬🇧 English': (f"Your number: {phone_number} has been accepted. Thank you! 🙏", "Please enter your full name:")
        }

        # Foydalanuvchiga yuboriladigan xabarlar
        thank_you_msg, request_name_msg = responses.get(language, ("Thank you!", "Please enter your full name:"))

        # Xabarlarni foydalanuvchiga yuborish
        bot.send_message(user_id, thank_you_msg)
        bot.send_message(user_id, request_name_msg)

    else:
        bot.send_message(user_id, "Iltimos, telefon raqamingizni yuboring.")










# @bot.message_handler(func=lambda message: message.chat.id in user_language)
# def handle_name(message):
#     chat_id = message.chat.id
#     language = user_language.get(chat_id, '🌐 Русский')

#     # Foydalanuvchi ismini qabul qilib olamiz
#     user_profiles[chat_id] = {"name": message.text, "language": language}

#     name = message.text
#     # Ismni yangilab saqlaymiz
#     add_user(user_id=chat_id, phone_number=None, user_name=name)

#     # Foydalanuvchiga tilga mos xabar yuboriladi
#     responses = {
#         '🌐 Русский': "Отлично! Оформим заказ вместе? 😊",
#         "🌟 O'zbekcha": "Ajoyib! Birgalikda buyurtma beramizmi? 😊",
#         '🇬🇧 English': "Great! Shall we place the order together? 😊"
#     }
#     welcome_msg = responses.get(language, "Great! Shall we place the order together? 😊")
#     bot.send_message(chat_id, welcome_msg)
