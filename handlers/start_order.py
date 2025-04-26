# order_processing.py

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .add_user import add_user  # Foydalanuvchini qo'shish funksiyasi (agar kerak bo'lsa)
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")


# MongoDB bilan ulanish
client = MongoClient(mongo_uri)  # MongoDB'ga ulanish

# To'g'ri ma'lumotlar bazasini olish
db = client.get_database()  # MongoDB ma'lumotlar bazasini olish

# "Sarista_service" nomli ma'lumotlar bazasi ichidan "Services" kolleksiyasini olish
collection = db.Sarista_service.Services  # Kolleksiyani olish

# Kolleksiyadagi barcha hujjatlarni topish
documents = collection.find()

def start_order_processing(user_id, admin_id, bot):
    # Foydalanuvchi ma'lumotlarini olish
    user_data = collection.find_one({'_id': user_id})

    if user_data:
        # Foydalanuvchining nomi, telefon raqami va manzilini olish
        name = user_data.get('name', 'Ism kiritilmagan')
        phone = user_data.get('phone_number', 'Telefon raqami kiritilmagan')
        address = user_data.get('address', 'Manzil kiritilmagan')
        location = user_data.get('location', {})
        latitude = location.get('latitude', None)
        longitude = location.get('longitude', None)

        # Servislarni olish
        services = user_data.get('services', [])

        # Servislar haqida xabarni tayyorlash
        services_text = ""
        if services:
            for service in services:
                services_text += f"🌟 {service}\n"
        else:
            services_text = "Hozirda tanlangan xizmatlar mavjud emas."

        # Lokatsiya manzili
        location_text = ""
        if latitude and longitude:
            maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
            location_text = (
                f"<b>Yetkazib berish manzili:</b>\n"
                f"🏠 Manzil: {address}\n"
                f"📍 <a href='{maps_link}'>Google Maps'da ko'rish</a>\n\n"
            )
        else:
            location_text = "<b>Manzil kiritilmagan!</b>\n\n"

        # Buyurtma haqida xabar
        order_message = (
            f"🛒 <b>Yangi buyurtma:</b>\n\n"
            f"<b>Ism:</b> {name}\n"
            f"<b>Telefon:</b> {phone}\n"
            f"{location_text}"  # Yetkazib berish manzili (agar bo'lsa)
            f"<b>Xizmatlar:</b>\n{services_text}\n\n"
        )

        # Tugmalarni yaratish
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("✅ Bajarildi", callback_data=f"order_done_{user_id}"))
        markup.add(InlineKeyboardButton("❌ Bekor qilish", callback_data=f"order_cancel_{user_id}"))

        # Admin yoki yetkazib beruvchiga buyurtma xabarini jo'natish
        bot.send_message(admin_id, order_message, parse_mode='HTML', reply_markup=markup)

    else:
        print("Buyurtma ma'lumotlari topilmadi.")
