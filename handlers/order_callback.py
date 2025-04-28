# order_callbacks.py

from telebot import types
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from shows.show_feedback import show_feedback_menu
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

# MongoDB bilan ulanish
client = MongoClient(mongo_uri)
db = client.get_database()
collection = db.Sarista_service.Services

# def register_order_callbacks(bot, language):
#     @bot.callback_query_handler(
#     func=lambda call: call.data.startswith('order_done_') or call.data.startswith('order_cancel_') or call.data.startswith('order_pending_'))
#     def handle_order_callback(call):
#         user_id = call.data.split('_')[-1]
#         message_id = call.message.message_id
#         message = call.message
#         chat_id = call.message.chat.id

#         # Faqat order_number va til kerak bo'ladi
#         user_data = collection.find_one({'_id': int(user_id)})

#         if not user_data:
#             bot.answer_callback_query(call.id, "Foydalanuvchi ma'lumotlari topilmadi.", show_alert=True)
#             return

#         order_number = user_data.get('order_number', "Noma'lum")
       
#         print(language) # Parametr orqali kelyapti!

#         if 'order_done' in call.data:
#             collection.update_one({'_id': int(user_id)}, {'$set': {'order_status': 'bajarildi'}})

#             collection.update_one({'_id': int(user_id)}, {'$set': {'services': []}})

#             bot.answer_callback_query(call.id, "Buyurtma bajarildi!", show_alert=True)

#             user_messages = {
#     '🌐 Русский': f"✅ Ваш заказ #{order_number} выполнен. Мы всегда готовы обслужить вас! Спасибо, что выбрали нас! 🙏",
#     "🌟 O'zbekcha": f"✅ Sizning #{order_number} raqamli buyurtmangiz bajarildi. Doim sizga xizmat ko‘rsatishga tayyormiz! Bizni tanlaganingiz uchun tashakkur! 🙏",
#     '🇬🇧 English': f"✅ Your order #{order_number} has been completed. We are always ready to serve you! Thank you for choosing us! 🙏"
# }


#             bot.send_message(user_id, user_messages.get(language, f"✅ Buyurtmangiz #{order_number} bajarildi. 😋🍽️"))
#             bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
#             bot.send_message(chat_id, f"✅ Buyurtma #{order_number} bajarildi! Foydalanuvchi xabardor qilindi. 🎉")

#             show_feedback_menu(bot,chat_id,language)

#         elif 'order_cancel' in call.data:
#             collection.update_one({'_id': int(user_id)}, {'$set': {'order_status': 'bekor qilingan'}})
#             bot.answer_callback_query(call.id, "Buyurtma bekor qilindi!", show_alert=True)

#             cancel_messages = {
#     '🌐 Русский': f"❌ Ваш заказ #{order_number} был отменён. Надеемся снова вас увидеть! 🤝",
#     "🌟 O'zbekcha": f"❌ Sizning #{order_number} raqamli buyurtmangiz bekor qilindi. Sizni yana kutib qolamiz! 🤝",
#     '🇬🇧 English': f"❌ Your order #{order_number} has been canceled. Hope to see you again! 🤝"
# }
        

#             bot.send_message(user_id, cancel_messages.get(language, f"❌ Buyurtmangiz #{order_number} bekor qilindi. 😔"))
#             bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
#             bot.send_message(chat_id, f"❌ Buyurtma #{order_number} bekor qilindi! Foydalanuvchi xabardor qilindi. 🛑")

#         elif 'order_pending' in call.data:
#             collection.update_one({'_id': int(user_id)}, {'$set': {'order_status': 'kutilmoqda'}})
#             bot.answer_callback_query(call.id, "Buyurtma holati: Kutilmoqda.", show_alert=True)

            # pending_messages = {
            #     '🌐 Русский': f"⏳ Ваш заказ #{order_number} ожидается. Мы работаем над ним! 🙌",
            #     "🌟 O'zbekcha": f"⏳ Sizning #{order_number} raqamli buyurtmangiz kutilmoqda. Biz buyurtmangiz ustida ishlayapmiz 🙌",
            #     '🇬🇧 English': f"⏳ Your order #{order_number} is pending. We are working on it! 🙌"
            # }

#             # ❌ bot.edit_message_reply_markup YO‘Q!
#             # ❌ Hech nima o‘zgartirilmaydi tugmalarda.

#             # Foydalanuvchiga va adminga xabar yuborish
            # bot.send_message(user_id, pending_messages.get(language, f"⏳ Buyurtmangiz #{order_number} kutilmoqda. 😊"))
            # bot.send_message(chat_id, f"⏳ Buyurtma #{order_number} holati: Kutilmoqda! 📦")


# admin_messages dict import qilinadi


# admin_messages = {}

# def register_order_callbacks(bot, language):
#     @bot.callback_query_handler(
#         func=lambda call: call.data.startswith('order_done_') or call.data.startswith('order_cancel_') or call.data.startswith('order_pending_'))
#     def handle_order_callback(call):
#         user_id = int(call.data.split('_')[-1])
#         message = call.message
#         chat_id = call.message.chat.id

#         user_data = collection.find_one({'_id': user_id})

#         if not user_data:
#             bot.answer_callback_query(call.id, "Foydalanuvchi ma'lumotlari topilmadi.", show_alert=True)
#             return

#         order_number = user_data.get('order_number', "Noma'lum")

#         if 'order_done' in call.data:
#             collection.update_one({'_id': user_id}, {'$set': {'order_status': 'bajarildi'}})
#             bot.answer_callback_query(call.id, "Buyurtma bajarildi!", show_alert=True)

#             # HAR IKKALA ADMIN XABARINI HAM O'ZGARTIRAMIZ
#             if user_id in admin_messages:
#                 for admin_id, msg_id in admin_messages[user_id]:
#                     try:
#                         bot.edit_message_reply_markup(chat_id=admin_id, message_id=msg_id, reply_markup=None)
#                     except Exception as e:
#                         print(f"Error editing message for admin {admin_id}: {e}")

#             # Foydalanuvchiga habar jo‘natish
#             user_messages = {
#                 '🌐 Русский': f"✅ Ваш заказ #{order_number} выполнен. Мы всегда готовы обслужить вас! Спасибо, что выбрали нас! 🙏",
#                 "🌟 O'zbekcha": f"✅ Sizning #{order_number} raqamli buyurtmangiz bajarildi. Doim sizga xizmat ko‘rsatishga tayyormiz! Bizni tanlaganingiz uchun tashakkur! 🙏",
#                 '🇬🇧 English': f"✅ Your order #{order_number} has been completed. We are always ready to serve you! Thank you for choosing us! 🙏"
#             }
#             bot.send_message(user_id, user_messages.get(language, f"✅ Buyurtmangiz #{order_number} bajarildi."))

#             # Feedback menyusi ko'rsatish
#             show_feedback_menu(bot, chat_id, language)

#         elif 'order_cancel' in call.data:
#             # xuddi shunaqa qilib bekor qilishda ham ikki admin xabari o'chiriladi
#             collection.update_one({'_id': user_id}, {'$set': {'order_status': 'bekor qilingan'}})
#             bot.answer_callback_query(call.id, "Buyurtma bekor qilindi!", show_alert=True)

#             if user_id in admin_messages:
#                 for admin_id, msg_id in admin_messages[user_id]:
#                     try:
#                         bot.edit_message_reply_markup(chat_id=admin_id, message_id=msg_id, reply_markup=None)
#                     except Exception as e:
#                         print(f"Error editing message for admin {admin_id}: {e}")

#             cancel_messages = {
#                 '🌐 Русский': f"❌ Ваш заказ #{order_number} был отменён. Надеемся снова вас увидеть! 🤝",
#                 "🌟 O'zbekcha": f"❌ Sizning #{order_number} raqamli buyurtmangiz bekor qilindi. Sizni yana kutib qolamiz! 🤝",
#                 '🇬🇧 English': f"❌ Your order #{order_number} has been canceled. Hope to see you again! 🤝"
#             }

#             bot.send_message(user_id, cancel_messages.get(language, f"❌ Buyurtmangiz bekor qilindi."))

#         elif 'order_pending' in call.data:
#             # pending holatda ham
#             collection.update_one({'_id': user_id}, {'$set': {'order_status': 'kutilmoqda'}})
#             bot.answer_callback_query(call.id, "Buyurtma holati: Kutilmoqda.", show_alert=True)

#             if user_id in admin_messages:
#                 for admin_id, msg_id in admin_messages[user_id]:
#                     try:
#                         bot.edit_message_reply_markup(chat_id=admin_id, message_id=msg_id, reply_markup=None)
#                     except Exception as e:
#                         print(f"Error editing message for admin {admin_id}: {e}")

#             pending_messages = {
#                 '🌐 Русский': f"⏳ Ваш заказ #{order_number} ожидается. Мы работаем над ним! 🙌",
#                 "🌟 O'zbekcha": f"⏳ Sizning #{order_number} raqamli buyurtmangiz kutilmoqda. Biz buyurtmangiz ustida ishlayapmiz 🙌",
#                 '🇬🇧 English': f"⏳ Your order #{order_number} is pending. We are working on it! 🙌"
#             }

#             bot.send_message(user_id, pending_messages.get(language, f"⏳ Buyurtmangiz kutilmoqda."))

from shows.show_feedback import show_feedback_menu

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_database()
collection = db.Sarista_service.Services

admin_messages ={}

# Admin xabarlarini tozalovchi funksiya
def remove_admin_buttons(bot, user_id):
    if user_id in admin_messages:
        for admin_id, msg_id in admin_messages[user_id]:
            try:
                bot.edit_message_reply_markup(chat_id=admin_id, message_id=msg_id, reply_markup=None)
            except Exception as e:
                print(f"Error editing message for admin {admin_id}: {e}")
        del admin_messages[user_id]

# Asosiy callback funksiyalarni registratsiya qilish
def register_order_callbacks(bot, language):

    @bot.callback_query_handler(func=lambda call: call.data.startswith(('order_done_', 'order_cancel_', 'order_pending_')))
    def handle_order_callback(call):
        user_id = int(call.data.split('_')[-1])
        chat_id = call.message.chat.id

        user_data = collection.find_one({'_id': user_id})
        if not user_data:
            bot.answer_callback_query(call.id, "Foydalanuvchi ma'lumotlari topilmadi.", show_alert=True)
            return

        order_number = user_data.get('order_number', "Noma'lum")

        action = call.data.split('_')[1]  # done, cancel yoki pending

        status_mapping = {
            'done': ('bajarildi', "✅", {
                '🌐 Русский': f"✅ Ваш заказ #{order_number} выполнен. Мы всегда готовы обслужить вас! Спасибо, что выбрали нас! 🙏",
                "🌟 O'zbekcha": f"✅ Sizning #{order_number} raqamli buyurtmangiz bajarildi. Doim sizga xizmat ko‘rsatishga tayyormiz! Bizni tanlaganingiz uchun tashakkur! 🙏",
                '🇬🇧 English': f"✅ Your order #{order_number} has been completed. We are always ready to serve you! Thank you for choosing us! 🙏"
            }),
            'cancel': ('bekor qilingan', "❌", {
                '🌐 Русский': f"❌ Ваш заказ #{order_number} был отменён. Надеемся снова вас увидеть! 🤝",
                "🌟 O'zbekcha": f"❌ Sizning #{order_number} raqamli buyurtmangiz bekor qilindi. Sizni yana kutib qolamiz! 🤝",
                '🇬🇧 English': f"❌ Your order #{order_number} has been canceled. Hope to see you again! 🤝"
            }),
            'pending': ('kutilmoqda', "⏳", {
                '🌐 Русский': f"⏳ Ваш заказ #{order_number} ожидается. Мы работаем над ним! 🙌",
                "🌟 O'zbekcha": f"⏳ Sizning #{order_number} raqamli buyurtmangiz kutilmoqda. Biz buyurtmangiz ustida ishlayapmiz 🙌",
                '🇬🇧 English': f"⏳ Your order #{order_number} is pending. We are working on it! 🙌"
            })
        }

        if action not in status_mapping:
            bot.answer_callback_query(call.id, "Nomaʼlum amal.", show_alert=True)
            return

        new_status, emoji, messages = status_mapping[action]

        # MongoDBdagi holatni yangilash
        collection.update_one({'_id': user_id}, {'$set': {'order_status': new_status}})
        bot.answer_callback_query(call.id, f"Buyurtma holati: {new_status.replace('_', ' ')}", show_alert=True)

        # Adminlar xabarini yangilash
        remove_admin_buttons(bot, user_id)

        # Foydalanuvchiga habar yuborish
        user_message = messages.get(language, messages.get("🌟 O'zbekcha"))
        bot.send_message(user_id, user_message)

        # Agar "done" bo'lsa, foydalanuvchiga feedback menyu ko'rsatamiz
        if action == 'done':
            show_feedback_menu(bot, user_id, language)







        # elif 'order_pending' in call.data:
        #     collection.update_one({'_id': int(user_id)}, {'$set': {'order_status': 'kutilmoqda'}})
        #     bot.answer_callback_query(call.id, "Buyurtma holati: Kutilmoqda.", show_alert=True)

        #     pending_messages = {
        #         '🌐 Русский': f"⏳ Ваш заказ #{order_number} ожидается. Мы работаем над ним! 🙌",
        #         "🌟 O'zbekcha": f"⏳ Sizning #{order_number} raqamli buyurtmangiz kutilmoqda. Tez orada tayyor bo'ladi! 🙌",
        #         '🇬🇧 English': f"⏳ Your order #{order_number} is pending. We are working on it! 🙌"
        #     }

        #     bot.send_message(user_id, pending_messages.get(language, f"⏳ Buyurtmangiz #{order_number} kutilmoqda. 😊"))
        #     bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
        #     bot.send_message(chat_id, f"⏳ Buyurtma #{order_number} holati: Kutilmoqda! 📦")