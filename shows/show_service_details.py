# from telebot import TeleBot, types
# from tinydb import Query
# from db import services_table
# from handlers.add_user import add_user

# def show_service_details(bot: TeleBot, chat_id: int, service_name: str, language: str = 'uz'):
#     """
#     Displays service details and requests location based on user's selected language
    
#     :param bot: TeleBot instance
#     :param chat_id: User's chat ID
#     :param service_name: Selected service name (with emoji, e.g., '💡 Elektrik')
#     :param language: Selected language ('uz', 'ru', 'en')
#     """
#     try:
#         # Avval emojini olib tashlash
#         clean_service_name = service_name.replace('🔧', '').replace('🧹', '').replace('💡', '')\
#                                        .replace('👷\u200d♂️', '').replace('👶', '')\
#                                        .replace('🩺', '').replace('🛠️', '')\
#                                        .replace('🎉', '').replace('🌿', '').strip()
        
#         # Language code to emoji mapping
#         language_map = {
#             'uz': "🌟 O'zbekcha",
#             'ru': "🌐 Русский",
#             'en': "🇬🇧 English"
#         }
#         selected_language = language_map.get(language, "🌟 O'zbekcha")
        
#         # Get service details from database
#         Service = Query()
#         service = services_table.get(Service.service_name == clean_service_name)
        
#         print(f"Tozalangan xizmat nomi: '{clean_service_name}'")
#         print(f"Topilgan xizmat: {service}")
        
#         if not service:
#             error_messages = {
#                 'uz': f"'{service_name}' xizmati topilmadi! Iltimos, qayta urinib ko'ring.",
#                 'ru': f"Услуга '{service_name}' не найдена! Пожалуйста, попробуйте снова.",
#                 'en': f"Service '{service_name}' not found! Please try again."
#             }
#             bot.send_message(chat_id, error_messages.get(language, "Service not found!"))
            
#             # Foydalanuvchiga mavjud xizmatlar ro'yxatini yuborish
#             available_services = [s['service_name'] for s in services_table.all()]
#             bot.send_message(chat_id, f"Mavjud xizmatlar:\n{', '.join(available_services)}")
#             return
        
#         # Qolgan kod o'zgarishsiz...
# def show_service_details(bot: TeleBot, chat_id: int, service_name: str, language: str = 'uz'):
#     try:
#         language_map = {
#             'uz': "🌟 O'zbekcha",
#             'ru': "🌐 Русский",
#             'en': "🇬🇧 English"
#         }
#         selected_language = language_map.get(language, "🌟 O'zbekcha")

#         all_services = services_table.all()
#         found_service = None

#         # Emoji olib tashlaydigan funksiya
#         def clean_text(text):
#             emojis = ['🔧', '🧹', '💡', '👷\u200d♂️', '👶', '🩺', '🛠️', '🎉', '🌿']
#             for emoji in emojis:
#                 text = text.replace(emoji, '')
#             return text.strip()

#         for service in all_services:
#             service_name_in_lang = service['service_name'].get(selected_language, "").strip()
#             clean_service_name_in_lang = clean_text(service_name_in_lang)
            
#             if clean_service_name_in_lang.lower() == service_name.strip().lower():
#                 found_service = service
#                 break
        
#         if not found_service:
#             # Error handling
#             error_messages = {
#                 'uz': f"'{service_name}' xizmati topilmadi! Iltimos, qayta urinib ko'ring.",
#                 'ru': f"Услуга '{service_name}' не найдена! Пожалуйста, попробуйте снова.",
#                 'en': f"Service '{service_name}' not found! Please try again."
#             }
#             bot.send_message(chat_id, error_messages.get(language, "Service not found!"))
#             return
        
#         # Agar topilsa
#         title = found_service['title'][selected_language]
#         description = found_service['description'][selected_language]
#         price = "{:,}".format(found_service['price'])        
#         # Translations dictionary
#         translations = {
#             'uz': {
#                 'request_location': "📍 Lokatsiyangizni yuboring yoki manzilni yozib yuboring",
#                 'service_info': "📌 Xizmat haqida ma'lumot:",
#                 'price': "💰 Narx:",
#                 'back': "🔙 Orqaga",
#                 'location_btn': "📍 Lokatsiyani yuborish"
#             },
#             'en': {
#                 'request_location': "📍 Please send your location or type your address",
#                 'service_info': "📌 Service information:",
#                 'price': "💰 Price:",
#                 'back': "🔙 Back",
#                 'location_btn': "📍 Send location"
#             },
#             'ru': {
#                 'request_location': "📍 Отправьте ваше местоположение или введите адрес",
#                 'service_info': "📌 Информация об услуге:",
#                 'price': "💰 Цена:",
#                 'back': "🔙 Назад",
#                 'location_btn': "📍 Отправить местоположение"
#             }
#         }
        
#         # Create keyboard markup
#         markup = types.ReplyKeyboardMarkup(
#             resize_keyboard=True, 
#             one_time_keyboard=True,
#             row_width=1
#         )
#         markup.add(
#             types.KeyboardButton(
#                 text=translations[language]['location_btn'],
#                 request_location=True
#             ),
#             types.KeyboardButton(text=translations[language]['back'])
#         )
        
#         # Prepare service information
#         title = service['title'].get(selected_language, service['title']["🌟 O'zbekcha"])
#         description = service['description'].get(selected_language, service['description']["🌟 O'zbekcha"])
#         price = "{:,}".format(service['price'])
        
#         add_user(chat_id, order=[clean_service_name])
#         # Format message text
#         message_text = (
#             f"{translations[language]['service_info']}\n\n"
#             f"🔹 {title}\n"
#             f"📝 {description}\n"
#             f"{translations[language]['price']} {price} so'm\n\n"
#             f"{translations[language]['request_location']}"
#         )
        
#         # Send message to user
#         bot.send_message(
#             chat_id,
#             message_text,
#             reply_markup=markup,
#             parse_mode='HTML'
#         )
#         # handle_location(message ,bot, user_language)
        
#     except Exception as e:
#         error_msg = {
#             'uz': "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.",
#             'ru': "Произошла ошибка. Пожалуйста, попробуйте снова.",
#             'en': "An error occurred. Please try again."
#         }
#         bot.send_message(chat_id, error_msg.get(language, "Error occurred"))
#         print(f"Error in show_service_details: {e}")
# from telebot import TeleBot, types
# from tinydb import Query
# from db import services_table
# from handlers.add_user import add_user

# def show_service_details(bot: TeleBot, chat_id: int, service_title: str, language: str = 'uz'):
#     """
#     Displays service details and requests location based on user's selected language
    
#     :param bot: TeleBot instance
#     :param chat_id: User's chat ID
#     :param service_title: Selected service title (with emoji, e.g., '💡 Elektrik')
#     :param language: Selected language ('uz', 'ru', 'en')
#     """
#     try:
#         # Language code to emoji mapping
#         # language_map = {
#         #     'uz': "🌟 O'zbekcha",
#         #     'ru': "🌐 Русский", 
#         #     'en': "🇬🇧 English"
#         # }
#         # selected_language = language_map.get(language, "🌟 O'zbekcha")
        
#         # Get all services and find matching title
#         Service = Query()
#         all_services = services_table.all()
        
#         found_service = None
#         for service in all_services:
#             # Check if the title in selected language matches
#             if service['title'].get(language, "").strip() == service_title.strip():
#                 found_service = service
#                 print(found_service)
#                 break
        
#         if not found_service:
#             error_messages = {
#                 "🌟 O'zbekcha": "Xizmat topilmadi! Iltimos, qayta urinib ko'ring.",
#                 "🌐 Русский": "Услуга не найдена! Пожалуйста, попробуйте снова.",
#                 "🇬🇧 English": "Service not found! Please try again."
#             }
#             bot.send_message(chat_id, error_messages.get(language, "Service not found!"))
#             return
#         print(found_service)
        
#         # Get service name in selected language
#         service_name = found_service['service_name'].get(language, found_service['service_name']["🌟 O'zbekcha"])
        
#         # Translations dictionary
#         translations = {
#             'uz': {
#                 'request_location': "📍 Lokatsiyangizni yuboring yoki manzilni yozib yuboring",
#                 'service_info': "📌 Xizmat haqida ma'lumot:",
#                 'price': "💰 Narx:",
#                 'back': "🔙 Orqaga",
#                 'location_btn': "📍 Lokatsiyani yuborish"
#             },
#             'en': {
#                 'request_location': "📍 Please send your location or type your address",
#                 'service_info': "📌 Service information:",
#                 'price': "💰 Price:",
#                 'back': "🔙 Back",
#                 'location_btn': "📍 Send location"
#             },
#             'ru': {
#                 'request_location': "📍 Отправьте ваше местоположение или введите адрес",
#                 'service_info': "📌 Информация об услуге:",
#                 'price': "💰 Цена:",
#                 'back': "🔙 Назад",
#                 'location_btn': "📍 Отправить местоположение"
#             }
#         }
        
#         # Create keyboard markup
#         markup = types.ReplyKeyboardMarkup(
#             resize_keyboard=True, 
#             one_time_keyboard=True,
#             row_width=1
#         )
#         markup.add(
#             types.KeyboardButton(
#                 text=translations[language]['location_btn'],
#                 request_location=True
#             ),
#             types.KeyboardButton(text=translations[language]['back'])
#         )
        
#         # Prepare service information
#         title = found_service['title'].get(language, found_service['title']["🌟 O'zbekcha"])
#         description = found_service['description'].get(language, 
#                                                      found_service['description']["🌟 O'zbekcha"])
#         price = "{:,}".format(found_service['price'])
        
#         add_user(chat_id, order=[service_name])  # <-- service_name is used here
        
#         # Format message text
#         message_text = (
#             f"{translations[language]['service_info']}\n\n"
#             f"🔹 {title}\n"
#             f"📝 {description}\n"
#             f"{translations[language]['price']} {price} so'm\n\n"
#             f"{translations[language]['request_location']}"
#         )
        
#         # Send message to user
#         bot.send_message(
#             chat_id,
#             message_text,
#             reply_markup=markup,
#             parse_mode='HTML'
#         )
        
#     except Exception as e:
#         error_msg = {
#             "🌟 O'zbekcha": "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.",
#             "🌐 Русский":  "Произошла ошибка. Пожалуйста, попробуйте снова.",
#             "🇬🇧 English":  "An error occurred. Please try again."
#         }
#         bot.send_message(chat_id, error_msg.get(language, "Error occurred"))
#         print(f"Error in show_service_details: {e}")


# from telebot import types
# import logging

# def show_service_details(bot: TeleBot, chat_id: int, service_title: str, language: str = 'uz'):
#     """
#     Displays service details and requests location based on user's selected language.
    
#     :param bot: TeleBot instance
#     :param chat_id: User's chat ID
#     :param service_title: Selected service title (with emoji, e.g., '💡 Elektrik')
#     :param language: Selected language ('uz', 'ru', 'en')
#     """
#     try:
#         # Til kodlarini JSONdagi kalitlarga moslashtirish
#         language_map = {
#             'uz': "🌟 O'zbekcha",
#             'ru': "🌐 Русский",
#             'en': "🇬🇧 English"
#         }
#         selected_language = language_map.get(language, "🌟 O'zbekcha")
        
#         # Tarjimalar lug'ati
#         translations = {
#             "🌟 O'zbekcha": {
#                 'service_info': "📌 Xizmat haqida ma'lumot:",
#                 'price': "💰 Narxi:",
#                 'request_location': "📍 Joylashuvingizni yuboring",
#                 'back': "🔙 Orqaga",
#                 'location_btn': "📍 Joylashuvni yuborish",
#                 'error': "Xizmat topilmadi! Iltimos, qayta urinib ko'ring."
#             },
#             "🌐 Русский": {
#                 'service_info': "📌 Информация об услуге:",
#                 'price': "💰 Цена:",
#                 'request_location': "📍 Отправьте ваше местоположение",
#                 'back': "🔙 Назад",
#                 'location_btn': "📍 Отправить местоположение",
#                 'error': "Услуга не найдена! Пожалуйста, попробуйте снова."
#             },
#             "🇬🇧 English": {
#                 'service_info': "📌 Service information:",
#                 'price': "💰 Price:",
#                 'request_location': "📍 Send your location",
#                 'back': "🔙 Back",
#                 'location_btn': "📍 Send location",
#                 'error': "Service not found! Please try again."
#             }
#         }
        
#         # Barcha xizmatlarni olish
#         all_services = services_table.all()
        
#         # Kerakli xizmatni topish
#         found_service = next(
#             (service for service in all_services if service['title'].get(selected_language, "").strip() == service_title.strip()), 
#             None
#         )
        
#         if not found_service:
#             bot.send_message(chat_id, translations[selected_language]['error'])
#             return
        
#         # service_name tekshiruv bilan olish
#         service_name = found_service.get('service_name', {}).get(selected_language) or found_service.get('service_name', {}).get("🌟 O'zbekcha", "")
        
#         # Xizmat detallari
#         title = found_service['title'].get(selected_language, "")
#         description = found_service['description'].get(selected_language, "")
#         price = "{:,}".format(found_service.get('price', 0))
        
#         # Klaviatura yaratish
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#         markup.add(
#             types.KeyboardButton(
#                 text=translations[selected_language]['location_btn'],
#                 request_location=True
#             ),
#             types.KeyboardButton(text=translations[selected_language]['back'])
#         )
        
#         # Xabar matni
#         message_text = (
#             f"{translations[selected_language]['service_info']}\n\n"
#             f"🔹 {title}\n"
#             f"📝 {description}\n"
#             f"{translations[selected_language]['price']} {price} so'm"
#         )
        
#         # Foydalanuvchiga xabar yuborish
#         bot.send_message(
#             chat_id,
#             message_text,
#             reply_markup=markup
#         )
        
#         # Foydalanuvchini bazaga qo'shish (agar add_user funksiyasi mavjud bo'lsa)
#         if 'add_user' in globals():
#             add_user(chat_id, order=[service_name])
        
#     except Exception as e:
#         error_message = translations.get(selected_language, translations["🌟 O'zbekcha"])['error']
#         bot.send_message(chat_id, error_message)
#         logging.error(f"Xatolik show_service_details funksiyasida: {e}")



# def show_service_details(bot: TeleBot, chat_id: int, service_title: str, language: str = 'uz'):
#     """
#     Displays service details and requests location based on user's selected language
    
#     :param bot: TeleBot instance
#     :param chat_id: User's chat ID
#     :param service_title: Selected service title (with emoji, e.g., '💡 Elektrik')
#     :param language: Selected language ('uz', 'ru', 'en')
#     """
#     try:
#         # Til kodlarini JSONdagi kalitlarga moslashtirish
#         language_map = {
#             'uz': "🌟 O'zbekcha",
#             'ru': "🌐 Русский",
#             'en': "🇬🇧 English"
#         }
#         selected_language = language_map.get(language, "🌟 O'zbekcha")
        
#         # Barcha xizmatlarni olish
#         all_services = services_table.all()
        
#         found_service = None
#         for service in all_services:
#             # Tanlangan tildagi sarlavhani olish
#             title_in_selected_lang = service['title'].get(selected_language, "")
            
#             # Agar sarlavha mos kelsa
#             if title_in_selected_lang.strip() == service_title.strip():
#                 found_service = service
#                 break
        
#         if not found_service:
#             error_messages = {
#                 "🌟 O'zbekcha": "Xizmat topilmadi! Iltimos, qayta urinib ko'ring.",
#                 "🌐 Русский": "Услуга не найдена! Пожалуйста, попробуйте снова.",
#                 "🇬🇧 English": "Service not found! Please try again."
#             }
#             bot.send_message(chat_id, error_messages.get(selected_language, "Service not found!"))
#             return
        
#         # Xizmat nomini tanlangan tilda olish
#         if isinstance(found_service['service_name'], dict):
#             service_name = found_service['service_name'].get(selected_language, 
#                                                           found_service['service_name']["🌟 O'zbekcha"])
#         else:
#             service_name = found_service['service_name']
        
#         # Tarjimalar lug'ati
#         translations = {
#             "🌟 O'zbekcha": {
#                 'service_info': "📌 Xizmat haqida ma'lumot:",
#                 'price': "💰 Narxi:",
#                 'request_location': "📍 Joylashuvingizni yuboring",
#                 'back': "🔙 Orqaga",
#                 'location_btn': "📍 Joylashuvni yuborish"
#             },
#             "🌐 Русский": {
#                 'service_info': "📌 Информация об услуге:",
#                 'price': "💰 Цена:",
#                 'request_location': "📍 Отправьте ваше местоположение",
#                 'back': "🔙 Назад",
#                 'location_btn': "📍 Отправить местоположение"
#             },
#             "🇬🇧 English": {
#                 'service_info': "📌 Service information:",
#                 'price': "💰 Price:",
#                 'request_location': "📍 Send your location",
#                 'back': "🔙 Back",
#                 'location_btn': "📍 Send location"
#             }
#         }
        
#         # Klaviatura yaratish
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#         markup.add(
#             types.KeyboardButton(
#                 text=translations[selected_language]['location_btn'],
#                 request_location=True
#             ),
#             types.KeyboardButton(text=translations[selected_language]['back'])
#         )
        
#         # Xizmat ma'lumotlarini tayyorlash
#         title = found_service['title'].get(selected_language)
#         description = found_service['description'].get(selected_language)
#         price = "{:,}".format(found_service['price'])
        
#         # Xabar matni
#         message_text = (
#             f"{translations[selected_language]['service_info']}\n\n"
#             f"🔹 {title}\n"
#             f"📝 {description}\n"
#             f"{translations[selected_language]['price']} {price} so'm"
#         )
        
#         # Foydalanuvchiga xabar yuborish
#         bot.send_message(
#             chat_id,
#             message_text,
#             reply_markup=markup,
#             parse_mode='HTML'
#         )
        
#         # Foydalanuvchini bazaga qo'shish
#         add_user(chat_id, order=[service_name])
        
#     except Exception as e:
#         error_msg = {
#             "🌟 O'zbekcha": "Xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.",
#             "🌐 Русский": "Произошла ошибка. Пожалуйста, попробуйте позже.",
#             "🇬🇧 English": "An error occurred. Please try again later."
#         }
#         bot.send_message(chat_id, error_msg.get(selected_language, error_msg["🌟 O'zbekcha"]))
#         print(f"Xatolik: {e}")


from telebot import TeleBot, types
from db import services_table
from handlers.add_user import add_user

def show_service_details(bot: TeleBot, chat_id: int, service_name: str, language: str = 'uz'):
    try:
        # Til mapping
        language_map = {
            'uz': "🌟 O'zbekcha",
            'ru': "🌐 Русский",
            'en': "🇬🇧 English"
        }
        selected_language = language_map.get(language, "🌟 O'zbekcha")

        # Servicelarni olish
        data = services_table.all()
        print(data)
        all_services = data if data else []

        # Emoji tozalovchi funksiya
        def clean_text(text):
            emojis = ['🔧', '🧹', '💡', '👷‍♂️', '👶', '🩺', '🛠️', '🎉', '🌿','🧑‍⚕️']
            for emoji in emojis:
                text = text.replace(emoji, '')
            return text.strip()

        # Kirgan user xizmatini tozalash
        cleaned_user_service_name = clean_text(service_name).lower()
        found_service = None

        # Servicelarni qidirish
        for service in all_services:
            service_name_in_lang = service['service_name']
            if isinstance(service_name_in_lang, dict):
                service_name_in_lang = service_name_in_lang.get(language, "").strip()
            clean_service_name_in_lang = clean_text(service_name_in_lang).lower()

            if clean_service_name_in_lang == cleaned_user_service_name:
                found_service = service
                break

        # Agar xizmat topilmasa
        if not found_service:
            error_messages = {
                "🌟 O'zbekcha": f"'{service_name}' xizmati topilmadi! Iltimos, qayta urinib ko'ring.",
                "🌐 Русский": f"Услуга '{service_name}' не найдена! Пожалуйста, попробуйте снова.",
                "🇬🇧 English": f"Service '{service_name}' not found! Please try again."
            }
            bot.send_message(chat_id, error_messages.get(language, "Service not found!"))
            return
        print(found_service)
        # Topilgan xizmat ma'lumotlari
        title_raw = found_service['title']
        description_raw = found_service['description']

        title = title_raw.get(language, title_raw.get(language, ""))
        description = description_raw.get(language, description_raw.get(language, ""))

        # User uchun eslab qolish (order uchun)
        service_name_raw = found_service['service_name']
        if isinstance(service_name_raw, dict):
            service_name_to_save = clean_text(service_name_raw.get(selected_language, ""))
        else:
            service_name_to_save = clean_text(service_name_raw)

        add_user(chat_id, order=[service_name_to_save])

        # Tarjimalar
        translations = {
    "🌟 O'zbekcha": {
        'request_location': "📍 Lokatsiyangizni yuboring",
        'service_info': "📌 Xizmat haqida ma'lumot:",
        'price': "💰 Narx:",
        'back': "🔙 Bosh menu",  # O'zgartirildi: "Orqaga" -> "Bosh menu"
        'location_btn': "📍 Lokatsiyani yuborish"
    },
    "🌐 Русский": {
        'request_location': "📍 Отправьте ваше местоположение",
        'service_info': "📌 Информация об услуге:",
        'price': "💰 Цена:",
        'back': "🔙 Главное меню",  # O'zgartirildi: "Назад" -> "Главное меню"
        'location_btn': "📍 Отправить местоположение"
    },
    "🇬🇧 English": {
        'request_location': "📍 Please send your location",
        'service_info': "📌 Service information:",
        'price': "💰 Price:",
        'back': "🔙 Main menu",  # O'zgartirildi: "Back" -> "Main menu"
        'location_btn': "📍 Send location"
    }
}

        trans = translations.get(language, translations["🌟 O'zbekcha"])

        # Klaviatura tayyorlash
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
        markup.add(
            types.KeyboardButton(text=trans['location_btn'], request_location=True),
            types.KeyboardButton(text=trans['back'])
        )

        # Xabar matni
        message_text = (
            f"{trans['service_info']}\n\n"
            f"🔹 {title}\n"
            f"📝 {description}\n"
            f"{trans['request_location']}"
        )

        # Xabar yuborish
        bot.send_message(
            chat_id,
            message_text,
            reply_markup=markup,
            parse_mode='HTML'
        )

    except Exception as e:
        # Xatolikni ushlash
        error_messages = {
            "🌟 O'zbekcha": "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.",
            "🌐 Русский" : "Произошла ошибка. Пожалуйста, попробуйте снова.",
            "🇬🇧 English" : "An error occurred. Please try again."
        }
        bot.send_message(chat_id, error_messages.get(language, "Error occurred"))
        print(f"Error in show_service_details: {e}")
