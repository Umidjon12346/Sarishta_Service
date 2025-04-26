# order_callbacks.py

from telebot import types
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

# MongoDB bilan ulanish
client = MongoClient(mongo_uri)
db = client.get_database()
collection = db.Sarista_service.Services

def register_order_callbacks(bot, user_language):
    @bot.callback_query_handler(
        func=lambda call: call.data.startswith('order_done_') or call.data.startswith('order_cancel_'))
    def handle_order_callback(call):
        user_id = call.data.split('_')[-1]
        message_id = call.message.message_id
        chat_id = call.message.chat.id

        # Faqat order_number va til kerak bo'ladi
        user_data = collection.find_one({'_id': int(user_id)})

        if not user_data:
            bot.answer_callback_query(call.id, "Foydalanuvchi ma'lumotlari topilmadi.", show_alert=True)
            return

        order_number = user_data.get('order_number', "Noma'lum")
        language = user_language.get(chat_id, "🌟 O'zbekcha") 
        print(language) # Parametr orqali kelyapti!

        if 'order_done' in call.data:
            collection.update_one({'_id': int(user_id)}, {'$set': {'order_status': 'bajarildi'}})
            bot.answer_callback_query(call.id, "Buyurtma bajarildi!", show_alert=True)

            user_messages = {
    '🌐 Русский': f"✅ Ваш заказ #{order_number} выполнен. Мы всегда готовы обслужить вас! Спасибо, что выбрали нас! 🙏",
    "🌟 O'zbekcha": f"✅ Sizning #{order_number} raqamli buyurtmangiz bajarildi. Doim sizga xizmat ko‘rsatishga tayyormiz! Bizni tanlaganingiz uchun tashakkur! 🙏",
    '🇬🇧 English': f"✅ Your order #{order_number} has been completed. We are always ready to serve you! Thank you for choosing us! 🙏"
}


            bot.send_message(user_id, user_messages.get(language, f"✅ Buyurtmangiz #{order_number} bajarildi. 😋🍽️"))
            bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
            bot.send_message(chat_id, f"✅ Buyurtma #{order_number} bajarildi! Foydalanuvchi xabardor qilindi. 🎉")

        elif 'order_cancel' in call.data:
            collection.update_one({'_id': int(user_id)}, {'$set': {'order_status': 'bekor qilingan'}})
            bot.answer_callback_query(call.id, "Buyurtma bekor qilindi!", show_alert=True)

            cancel_messages = {
    '🌐 Русский': f"❌ Ваш заказ #{order_number} был отменён. Надеемся снова вас увидеть! 🤝",
    "🌟 O'zbekcha": f"❌ Sizning #{order_number} raqamli buyurtmangiz bekor qilindi. Sizni yana kutib qolamiz! 🤝",
    '🇬🇧 English': f"❌ Your order #{order_number} has been canceled. Hope to see you again! 🤝"
}


            bot.send_message(user_id, cancel_messages.get(language, f"❌ Buyurtmangiz #{order_number} bekor qilindi. 😔"))
            bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
            bot.send_message(chat_id, f"❌ Buyurtma #{order_number} bekor qilindi! Foydalanuvchi xabardor qilindi. 🛑")
