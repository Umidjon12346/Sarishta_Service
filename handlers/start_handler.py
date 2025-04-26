from telebot import types
from shows.show_services import show_services_categories

# def register_start_handler(bot, collection, user_language, show_services_categories):
#     @bot.message_handler(commands=['start'])
#     def start(message):
#         chat_id = message.chat.id

#         user = collection.find_one({"_id": chat_id})

#         if user:
#             language = user_language.get(chat_id, '🌐 Русский')
#             if not language:
#                 language = '🌐 Русский'

#             welcome_msgs = {
#                 '🌐 Русский': "С возвращением!",
#                 "🌟 O'zbekcha": "Yana qaytganingizdan xursandmiz!",
#                 '🇬🇧 English': "Welcome back!"
#             }

#             welcome_back_msg = welcome_msgs.get(language, "Welcome back!")
#             bot.send_message(chat_id, welcome_back_msg)

#             show_services_categories(chat_id, language,bot)

#         else:
#             keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#             keyboard.add(
#                 KeyboardButton('🌐 Русский'),
#                 KeyboardButton("🌟 O'zbekcha"),
#                 KeyboardButton('🇬🇧 English')
#             )

#             bot.send_message(
#                 chat_id,
#                 '👋 Salom! Sizni SARISHTA SERVICE botida ko‘rganimdan xursandman! 😊\n\n'
#                 'Tilni tanlash orqali davom eting va biz sizga qanday yordam bera olishimizni ko‘ring.',
#                 reply_markup=keyboard
#             )



def start(message, bot, collection, user_language):
    chat_id = message.chat.id

    user = collection.find_one({"_id": chat_id})

    if user:
        # Foydalanuvchi mavjud bo'lsa, tilni olish
        language = user_language.get(chat_id, '🌐 Русский')
        if not language:
            language = '🌐 Русский'

        # Tilga mos xabarlarni yuborish
        welcome_msgs = {
            '🌐 Русский': "С возвращением! Мы рады видеть вас снова! 😊",
            "🌟 O'zbekcha": "Yana qaytganingizdan xursandmiz! 😊",
            '🇬🇧 English': "Welcome back! We're happy to see you again! 😊"
        }

        welcome_back_msg = welcome_msgs.get(language, "Welcome back!")
        bot.send_message(chat_id, welcome_back_msg)

        # Xizmat kategoriyalarini ko'rsatish
        show_services_categories(message, user_language, bot)  # Bu yerda message obyektini yuborish kerak

    else:
        # Foydalanuvchi yangi bo'lsa, tilni tanlash uchun tugmalarni ko'rsatish
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(
            types.KeyboardButton('🌐 Русский'),
            types.KeyboardButton("🌟 O'zbekcha"),
            types.KeyboardButton('🇬🇧 English')
        )

        bot.send_message(
            chat_id,
            '👋 Salom! Sizni SARISHTA SERVICE botida ko‘rganimdan xursandmiz!\n' \
            '👋 Привет! Рад видеть вас в SARISHTA SERVICE боте! 😊\n\nTilni tanlang \ Выберите язык:',
            reply_markup=keyboard
        )
