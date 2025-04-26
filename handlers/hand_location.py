# from telebot import types
# from handlers.add_user import add_user


# def handle_location(message,bot,user_language):
#         chat_id = message.chat.id
#         location = message.location
#         language = user_language.get(chat_id, '🌐 Русский')

#         if location:
#             latitude = location.latitude
#             longitude = location.longitude
#             user_id = message.from_user.id

#             # Lokatsiyani lug'at ko‘rinishida saqlash
#             location_data = {
#                 'latitude': latitude,
#                 'longitude': longitude
#             }

#             # Foydalanuvchini yangilash
#             add_user(user_id, None, None, location=location_data)

#             responses = {
#                 '🌐 Русский': f"Ваше местоположение получено. Спасибо!\n\n📞 С вами скоро свяжется наш оператор:\n\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  +998 95 229 88 99\n  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  +998 95 339 88 99",
#                 "🌟 O'zbekcha": f"Joylashuvingiz qabul qilindi. Rahmat!\n\n📞 Operatorlarimiz tez orada siz bilan bog‘lanadi. \n \t\t\t\t\t\t\t\t\t\t\t\t\t\t+998 95 229 88 99 \n \t\t\t\t\t\t\t\t\t\t\t\t\t\t+998 95 339 88 99",
#                 '🇬🇧 English': f"Your location has been received. Thank you!\n\n📞 Our operator will contact you shortly. \n +998 95 229 88 99 \n +998 95 339 88 99"
#             }

#             bot.send_message(chat_id, responses.get(language))

#         else:
#             bot.send_message(chat_id, "📍 Lokatsiya olinmadi. Iltimos, qayta urinib ko‘ring.")


# from telebot import types
# from handlers.add_user import add_user

# from telebot import types
# from handlers.add_user import add_user

# def handle_location(message, bot, user_language):
#     chat_id = message.chat.id
#     language = user_language.get(chat_id, '🌐 Русский')

#     if message.location:
#         # Telefon orqali lokatsiya yuborilgan
#         latitude = message.location.latitude
#         longitude = message.location.longitude

#         user_id = message.from_user.id

#         # Lokatsiyani lug'at ko‘rinishida saqlash
#         location_data = {
#             'latitude': latitude,
#             'longitude': longitude
#         }

#         # Foydalanuvchini yangilash
#         add_user(user_id, None, None, location=location_data)

#         responses = {
#             '🌐 Русский': f"Ваше местоположение получено. Спасибо!\n\n📞 С вами скоро свяжется наш оператор:\n\n+998 95 229 88 99\n+998 95 339 88 99",
#             "🌟 O'zbekcha": f"Joylashuvingiz qabul qilindi. Rahmat!\n\n📞 Operatorlarimiz tez orada siz bilan bog‘lanadi.\n+998 95 229 88 99\n+998 95 339 88 99",
#             '🇬🇧 English': f"Your location has been received. Thank you!\n\n📞 Our operator will contact you shortly.\n+998 95 229 88 99\n+998 95 339 88 99"
#         }

#         bot.send_message(chat_id, responses.get(language))

#     elif message.text:
#         # Matndan kelganda, tugma va xabar tilini tanlaymiz
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#         location_buttons = {
#             '🌐 Русский': '📍 Отправить локацию',
#             "🌟 O'zbekcha": '📍 Lokatsiyani yuborish',
#             '🇬🇧 English': '📍 Send location'
#         }

#         location_button_text = location_buttons.get(language, '📍 Отправить локацию')
#         location_button = types.KeyboardButton(location_button_text, request_location=True)
#         markup.add(location_button)

#         warning_messages = {
#             '🌐 Русский': "📍 Пожалуйста, отправьте своё местоположение через кнопку ниже.",
#             "🌟 O'zbekcha": "📍 Iltimos, lokatsiyani pastdagi tugma orqali yuboring.",
#             '🇬🇧 English': "📍 Please send your location using the button below."
#         }

#         bot.send_message(chat_id, warning_messages.get(language), reply_markup=markup)

#     else:
#         bot.send_message(chat_id, "📍 Lokatsiya olinmadi. Iltimos, qayta urinib ko‘ring.")

from telebot import types
from handlers.add_user import add_user

def handle_location(message, bot, user_language):
    chat_id = message.chat.id
    location = message.location
    language = user_language.get(chat_id, '🌐 Русский')

    if location:
        latitude = location.latitude
        longitude = location.longitude
        user_id = message.from_user.id

        # Lokatsiyani lug'at ko‘rinishida saqlash
        location_data = {
            'latitude': latitude,
            'longitude': longitude
        }

        # Foydalanuvchini yangilash
        add_user(user_id, None, None, location=location_data)

        responses = {
            '🌐 Русский': f"Ваше местоположение получено. Спасибо!\n\n📞 С вами скоро свяжется наш оператор:\n\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t+998952298899\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t+998953398899",
            "🌟 O'zbekcha": f"Joylashuvingiz qabul qilindi. Rahmat!\n\n📞 Operatorlarimiz tez orada siz bilan bog‘lanadi.\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t+998952298899\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t+998 95 339 88 99",
            '🇬🇧 English': f"Your location has been received. Thank you!\n\n📞 Our operator will contact you shortly.\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t+998 95 229 88 99\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t+998 95 339 88 99"
        }

        bot.send_message(chat_id, responses.get(language))

    else:
        # Agar foydalanuvchi location emas, matn yuborsa: 3 tilda javob
        responses = {
            '🌐 Русский': "❗ Пожалуйста, отправьте ваше местоположение через кнопку ниже!",
            "🌟 O'zbekcha": "❗ Iltimos, joylashuvingizni pastdagi tugma orqali yuboring!",
            '🇬🇧 English': "❗ Please send your location using the button below!"
        }

        bot.send_message(chat_id, responses.get(language, "❗ Please send your location using the button below!"))
