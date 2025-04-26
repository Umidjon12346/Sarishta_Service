# from datetime import datetime
# from dotenv import load_dotenv
# import os
# from pymongo import MongoClient
# load_dotenv()
# mongo_uri = os.getenv("MONGO_URI")


# # MongoDB bilan ulanish
# client = MongoClient(mongo_uri)  # MongoDB'ga ulanish

# # To'g'ri ma'lumotlar bazasini olish
# db = client.get_database()  # MongoDB ma'lumotlar bazasini olish

# # "Sarista_service" nomli ma'lumotlar bazasi ichidan "Services" kolleksiyasini olish
# collection = db.Sarista_service.Services  # Kolleksiyani olish

# # Kolleksiyadagi barcha hujjatlarni topish
# documents = collection.find()

# from datetime import datetime

# def add_user(user_id, user_name=None, phone_number=None, location=None, payment_status='Tolanmagan',
#                order_status='bajarilmadi', order=None):
#     # Bugungi sanani datetime formatida olish
#     now = datetime.now()

#     try:
#         # Mavjud foydalanuvchini qidiramiz
#         existing_user = collection.find_one({'_id': user_id})

#         if not existing_user:
#             # Foydalanuvchi mavjud bo'lmasa, yangi hujjat qo'shamiz
#             user_data = {
#                 '_id': user_id,
#                 'name': user_name,
#                 'phone_number': phone_number,
#                 'date_added': now,
#                 'payment_status': payment_status,
#                 'order_status': order_status,  # Buyurtma holati default bo'lib 'bajarilmadi'
#                 'services': order or []  # Foydalanuvchi tanlagan servislar
#             }
#             # Agar lokatsiya mavjud bo'lsa, uni ham saqlaymiz
#             if location:
#                 user_data['location'] = location

#             # Ma'lumotlarni MongoDB'ga kiritish
#             collection.insert_one(user_data)
#             print("Foydalanuvchi qo'shildi!")

#         else:
#             # Foydalanuvchi mavjud bo'lsa, ma'lumotlarini yangilaymiz
#             update_data = {}
#             if user_name:
#                 update_data['name'] = user_name
#             if phone_number:
#                 update_data['phone_number'] = phone_number
#             update_data['date_updated'] = now

#             # Agar lokatsiya mavjud bo'lsa, uni yangilaymiz
#             if location:
#                 update_data['location'] = location

#             # Servislar ro'yxatini yangilash (masalan, yangi servisni qo'shish)
#             if order is not None:
#                 update_data['services'] = order  # Yangilangan servislarni qo'shish
#             else:
#                 # Agar servislar ro'yxati bo'lmasa, mavjud servislarni saqlaymiz
#                 existing_services = existing_user.get('services', [])
#                 update_data['services'] = existing_services  # Mavjud servislarni saqlaymiz

#             # Buyurtma holatini yangilash
#             update_data['order_status'] = existing_user.get('order_status', 'bajarilmadi')

#             # MongoDB'dagi foydalanuvchini yangilash
#             collection.update_one(
#                 {'_id': user_id},  # Qidiriladigan hujjat
#                 {'$set': update_data}  # Yangilanadigan ma'lumotlar
#             )
#             print("Foydalanuvchi ma'lumotlari yangilandi!")

#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")






from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

# MongoDB bilan ulanish
client = MongoClient(mongo_uri)
db = client.get_database()
collection = db.Sarista_service.Services

documents = collection.find()

def add_user(user_id, user_name=None, phone_number=None, location=None, payment_status='Tolanmagan',
             order_status='bajarilmadi', order=None, order_number=None):
    now = datetime.now()

    try:
        existing_user = collection.find_one({'_id': user_id})

        if not existing_user:
            user_data = {
                '_id': user_id,
                'name': user_name,
                'phone_number': phone_number,
                'date_added': now,
                'payment_status': payment_status,
                'order_status': order_status,
                'services': order or [],
                'order_number': order_number  # ✅ YANGI: order_number qo‘shildi
            }
            if location:
                user_data['location'] = location

            collection.insert_one(user_data)
            print("Foydalanuvchi qo'shildi!")

        else:
            update_data = {}
            if user_name:
                update_data['name'] = user_name
            if phone_number:
                update_data['phone_number'] = phone_number
            update_data['date_updated'] = now

            if location:
                update_data['location'] = location

            if order is not None:
                update_data['services'] = order
            else:
                existing_services = existing_user.get('services', [])
                update_data['services'] = existing_services

            update_data['order_status'] = existing_user.get('order_status', 'bajarilmadi')

            if order_number:
                update_data['order_number'] = order_number  # ✅ YANGI: order_numberni yangilash

            collection.update_one(
                {'_id': user_id},
                {'$set': update_data}
            )
            print("Foydalanuvchi ma'lumotlari yangilandi!")

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

