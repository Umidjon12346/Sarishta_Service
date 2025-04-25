# handlers/name_handler.py
from .add_user import add_user
from shows.show_services import show_services_categories

def handle_name(message, bot, user_language, user_profiles):
    chat_id = message.chat.id
    language = user_language.get(chat_id, '🌐 Русский')  # Foydalanuvchining tilini olish

    # Foydalanuvchi ismini qabul qilib olish
    user_profiles[chat_id] = {"name": message.text, "language": language}

    name = message.text  # Ismni olish
    # Ismni yangilab saqlash
    add_user(user_id=chat_id, phone_number=None, user_name=name)

    # Tilga mos xabar yuborish
    responses = {
        '🌐 Русский': "Отлично! Оформим заказ вместе? 😊",
        "🌟 O'zbekcha": "Ajoyib! Birgalikda buyurtma beramizmi? 😊",
        '🇬🇧 English': "Great! Shall we place the order together? 😊"
    }
    welcome_msg = responses.get(language, "Great! Shall we place the order together? 😊")
    bot.send_message(chat_id, welcome_msg)

    # Asosiy menyuni ko'rsatamiz
    show_services_categories(message, user_language,bot)
