from telebot import TeleBot, types
from db import get_service_titles  # TinyDB operatsiyalari uchun import

def show_services_categories(message, user_language: dict, bot: TeleBot):
    chat_id = message.chat.id  # Foydalanuvchi chat ID'sini olish

    # Foydalanuvchining tilini olish
    language = user_language.get(chat_id, "🌟 O'zbekcha")

    # Har bir til uchun tarjimalarni belgilang
    translations = {
        "🌟 O'zbekcha": {
            'select_category': "Xizmat kategoriyalaridan tanlang:",
            'cart': "📦 Savat",
            'order': "🚖 Buyurtma berish"
        },
        '🇬🇧 English': {
            'select_category': "Selec a service category:",
            'cart': "📦 Cart",
            'order': "🚖 Place Order"
        },
        "🌐 Русский": {
            'select_category': "Выберите категорию услуги:",
            'cart': "📦 Корзина",
            'order': "🚖 Оформить заказ"
        }
    }
    print(language)
    # Xizmat kategoriyalarini olish
    categories = list(get_service_titles(language))  # `get_services_categories()` funksiyasini chaqiramiz

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # Tugmalarni qayta o'lchash

    # Avval "Savat" va "Buyurtma berish" tugmalarini qo'shamiz

    # Kategoriyalarni ikki ustunli qilish
    for i in range(0, len(categories), 2):
        if i + 1 < len(categories):
            markup.row(types.KeyboardButton(categories[i]), types.KeyboardButton(categories[i + 1]))
        else:
            markup.row(types.KeyboardButton(categories[i]))

    # Foydalanuvchiga xabar yuborish
    bot.send_message(chat_id, translations[language]['select_category'], reply_markup=markup)
