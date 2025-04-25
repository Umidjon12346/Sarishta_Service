from telebot.types import KeyboardButton, ReplyKeyboardMarkup

def request_phone_number(message, user_language, bot):
    chat_id = message.chat.id
    language = user_language.get(chat_id, '🌐 Русский')  # Foydalanuvchining tilini olish

    # Har bir til uchun kerakli xabar va tugma matnlarini belgilash
    prompts = {
        '🌐 Русский': (
            "Какой у Вас номер? Отправьте ваш номер телефона.\nЧтобы отправить номер нажмите на кнопку \"📱 Отправить мой номер\", или\nОтправьте номер в формате: +998 *** ****",
            "📱 Отправить мой номер"
        ),
        "🌟 O'zbekcha": (
            "Sizning raqamingiz qanday? Telefon raqamingizni yuboring.\nRaqamingizni yuborish uchun \"📱 Raqamimni yuborish\" tugmasini bosing, yoki\nRaqamingizni quyidagi formatda yuboring: +998 *** ****",
            "📱 Raqamimni yuborish"
        ),
        '🇬🇧 English': (
            "What is your phone number? Send your phone number.\nTo send your number, press the \"📱 Send my number\" button, or\nSend your number in the format: +998 ** *** ****",
            "📱 Send my number"
        )
    }

    # Har bir til uchun prompt va tugma matnini olish
    prompt, button_text = prompts.get(language, ("Default prompt", "📱 Send my number"))

    # Tugma yaratish
    button = KeyboardButton(button_text, request_contact=True)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button)

    # Foydalanuvchiga xabar yuborish
    bot.send_message(chat_id, prompt, reply_markup=keyboard)
