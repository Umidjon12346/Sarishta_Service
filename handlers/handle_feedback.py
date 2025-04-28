# feedback_handler.py
from telebot import TeleBot
from shows.show_services import show_services_categories
from handlers.add_user import add_user

def handle_feedback(bot, message, language):
    chat_id = message.chat.id
    feedback = message.text
    
    thank_you_msgs = {
        '🌐 Русский': "Спасибо за ваш отзыв!",
        "🌟 O'zbekcha": "Fikr va mulohazalaringiz uchun rahmat!",
        '🇬🇧 English': "Thank you for your feedback!"
    }
    
    add_user(chat_id, user_name=None, phone_number=None, location=None, feedback=feedback)


    bot.send_message(chat_id, thank_you_msgs.get(language, "Thank you for your feedback!"))
    
    
#     # Asosiy menyuni chaqirish
# feedback_handler.py
# from telebot import TeleBot
# from shows.show_services import show_services_categories
# from handlers.add_user import add_user

# def handle_feedback(bot, message, language):
#     if isinstance(message, str):
#         # If message is just a string, it indicates an error
#         return  # Or handle the error accordingly

#     chat_id = message.chat.id
#     feedback = message.text

#     thank_you_msgs = {
#         '🌐 Русский': "Спасибо за ваш отзыв!",
#         "🌟 O'zbekcha": "Fikr va mulohazalaringiz uchun rahmat!",
#         '🇬🇧 English': "Thank you for your feedback!"
#     }

#     # Send a thank you message based on the user's language
#     bot.send_message(chat_id, thank_you_msgs.get(language, "Thank you for your feedback!"))

#     # Here, you should ensure the add_user function also handles other necessary user details
#     # If you don't have user name and other details, you can pass them as None or fetch them if possible
#     add_user(chat_id, user_name=None, phone_number=None, location=None, feedback=feedback)

#     # Optionally, you can show services categories after feedback
#     show_services_categories(bot, chat_id, language)
