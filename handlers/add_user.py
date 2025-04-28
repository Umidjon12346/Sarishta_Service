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
             order_status='bajarilmadi', order=None, order_number=None, feedback=None):
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
                'order_number': order_number,
                'feedbacks': [feedback] if feedback else []  # Qo‘shilgan feedback
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
                update_data['order_number'] = order_number  # order_numberni yangilash

            if feedback:
                # Agar yangi feedback kiritilgan bo'lsa, uni qo'shish
                if 'feedbacks' not in existing_user:
                    update_data['feedbacks'] = [feedback]
                else:
                    existing_feedbacks = existing_user.get('feedbacks', [])
                    existing_feedbacks.append(feedback)
                    update_data['feedbacks'] = existing_feedbacks

            collection.update_one(
                {'_id': user_id},
                {'$set': update_data}
            )
            print("Foydalanuvchi ma'lumotlari yangilandi!")

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
